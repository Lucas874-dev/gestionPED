from flask import Blueprint
from flask_login import logout_user

logout_bp = Blueprint('logout', __name__)
@logout_bp.route('/logout')

def logout():
    from flask import redirect, url_for, flash
    
    logout_user()  # Cierra la sesión
    flash("Sesión cerrada correctamente", "info")
    return redirect(url_for('login.login'))
