from flask import Blueprint
from flask_login import login_required



'''login_requerid nos garantiza que solo los usuarios
auutenticados pueden acceder a esta ruta'''

dashboard_bp = Blueprint('dashboard', __name__)
@dashboard_bp.route('/dashboard')
@login_required 

def dashboard():
    
    from flask import render_template
    return render_template ('dashboard.html')