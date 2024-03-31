from flask import render_template
from flask_login import login_required
from app.main import bp_main

@bp_main.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html')
