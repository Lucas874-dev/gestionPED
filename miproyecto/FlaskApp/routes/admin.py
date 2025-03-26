from flask import Blueprint
from flask_login import login_required



'''login_requerid nos garantiza que solo los usuarios
auutenticados pueden acceder a esta ruta'''

admin_bp = Blueprint('admin', __name__)
@admin_bp.route('/admin')
@login_required 

def admin():
    
    from flask import render_template
    return render_template ('admin.html')