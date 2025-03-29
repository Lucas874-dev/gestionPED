from flask import Blueprint
from flask_login import login_required
from utilidad import requiere_rol

cajero_bp = Blueprint('cajero',__name__)

@cajero_bp.route('/cajero')
@requiere_rol(['administrador','cajero'])
@login_required
def cajero():
    from flask import render_template
    return render_template('cajero.html')