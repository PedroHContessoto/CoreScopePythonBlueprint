from . import bp_apli1
from flask_login import login_required

@bp_apli1.route('/')
@login_required
def index():
    return "Página Inicial apli1"
