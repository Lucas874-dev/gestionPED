from flask import Blueprint
from flask_login import login_required
from utilidad import requiere_rol

cocinero_bp = Blueprint('cocinero',__name__)
@cocinero_bp.route('/cocinero')
@login_required
@requiere_rol(['cocinero','administrador'])
def cocinero():
    from flask import render_template
    return render_template('cocinero.html')