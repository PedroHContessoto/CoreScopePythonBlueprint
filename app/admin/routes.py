from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user
from app import db
from app.admin import bp_admin
from app.auth.models import User
from app.admin.decorators import admin_required

@bp_admin.route('/user_approval')
@admin_required
def user_approval():
    if not current_user.is_admin:
        flash('Acesso restrito a administradores.')
        return redirect(url_for('main.index'))

    users = User.query.filter_by(is_approved=False, on_waiting_list=True).all()
    return render_template('admin/user_approval.html', users=users)

@bp_admin.route('/approve_user/<int:user_id>', methods=['POST'])
@admin_required
def approve_user(user_id):
    if not current_user.is_admin:
        flash('Acesso restrito a administradores.')
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(user_id)
    user.is_approved = True
    user.on_waiting_list = False
    db.session.commit()
    flash('Usuário aprovado com sucesso.')
    return redirect(url_for('admin.user_approval'))
