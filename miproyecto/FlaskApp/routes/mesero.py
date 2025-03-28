from flask import Blueprint
from flask_login import login_required
from utilidad import requiere_rol

mesero_bp = Blueprint('mesero',__name__)
@mesero_bp.route('/mesero')

@requiere_rol(['administrador','mesero'])
@login_required
def mesero():
    from flask import render_template
    return render_template('mesero.html')