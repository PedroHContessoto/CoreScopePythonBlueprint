from . import bp_apli2
from flask_login import login_required

@bp_apli2.route('/')
@login_required
def index():
    return "Página Inicial apli2"
