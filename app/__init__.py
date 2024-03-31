from flask import Flask, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from config import Config
from datetime import timedelta


# Inicializações de extensões
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()
oauth = OAuth()

def create_app():
    app = Flask(__name__)
    app.run(debug=True)
    app.config.from_object(Config)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limita o tamanho das requisições a 1 MB

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)

    # Configuração do cliente OAuth2 para o Google
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile',
    },
)


    # Carregamento do usuário para Flask-Login
    from app.auth.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registro dos Blueprints
    from app.auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    from app.admin import bp_admin
    app.register_blueprint(bp_admin, url_prefix='/admin')

    from app.main import bp_main, register_blueprints_main
    app.register_blueprint(bp_main)
    register_blueprints_main(app)

    # Adicionando manipulador de erro 404 para redirecionar para a página de login
    @app.errorhandler(404)
    def page_not_found(e):
        # Redireciona para a página de login se um endpoint não for encontrado
        return redirect(url_for('auth.login'))


    return app
