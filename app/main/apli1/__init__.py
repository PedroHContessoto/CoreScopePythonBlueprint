from flask import Blueprint

bp_apli1 = Blueprint('apli1', __name__)

from . import routes