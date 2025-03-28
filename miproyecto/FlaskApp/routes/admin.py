from flask import Blueprint
from flask_login import login_required
from utilidad import requiere_rol



'''login_requerid nos garantiza que solo los usuarios
auutenticados pueden acceder a esta ruta'''

admin_bp = Blueprint('admin', __name__)
@admin_bp.route('/admin')

@login_required 
@requiere_rol(['administrador'])
def admin():
    from flask import render_template
    return render_template ('admin.html')