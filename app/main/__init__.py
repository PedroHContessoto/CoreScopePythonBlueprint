from flask import Blueprint

bp_main = Blueprint('main', __name__)

from .apli1 import bp_apli1 as apli1_blueprint
from .apli2 import bp_apli2 as apli2_blueprint
from .apli3 import bp_apli3 as apli3_blueprint


def register_blueprints_main(app):
    app.register_blueprint(apli1_blueprint, url_prefix='/apli1')
    app.register_blueprint(apli2_blueprint, url_prefix='/apli2')
    app.register_blueprint(apli3_blueprint, url_prefix='/apli3')


from app.main import routes
