from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_user, logout_user
from app import db, oauth
from app.auth import bp_auth
from app.auth.models import User
#from flask import current_app


@bp_auth.route('/login')
def login():
    if current_user.is_authenticated:
        if hasattr(current_user, 'is_admin') and current_user.is_admin:
            return redirect(url_for('admin.user_approval'))
        return render_template('main/dashboard.html')
    return render_template('auth/login.html')


@bp_auth.route('/check')
def check():
    if current_user.is_authenticated:
        return render_template('main/dashboard.html')
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@bp_auth.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    email = token['userinfo']['email']
    domain = email.split('@')[1]
    
    if domain != 'madeiramadeira.com.br':
        flash('Apenas emails do domínio @madeiramadeira.com.br são permitidos.')
        return redirect(url_for('auth.login'))
    
    user = User.query.filter_by(email=email).first()
    if not user:
        # Aqui você adiciona o usuário à lista de espera e não faz login imediatamente
        user = User(email=email, is_approved=False, on_waiting_list=True)
        db.session.add(user)
        db.session.commit()
        flash('Seu email foi adicionado à lista de espera para aprovação.')
        return render_template('auth/login.html')
    
    if user.is_approved:
        login_user(user)
        return redirect(url_for('admin.user_approval'))
    else:
        flash('Sua conta ainda não foi aprovada.')
        return render_template('auth/login.html')

@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
