from . import bp_apli3
from flask_login import login_required

@bp_apli3.route('/')
@login_required
def index():
    return "Página Inicial apli3"
