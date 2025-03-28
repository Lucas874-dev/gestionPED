from functools import wraps
from flask import redirect,url_for,flash
from flask_login import current_user
from models import control_rol


def requiere_rol(roles_permitidos):
    def caja(f):
        @wraps(f)
        def etiqueta(*args,**kwargs):
            if current_user.is_authenticated:
                control= control_rol(current_user.id)
                roles_usuario= control.obtener_roles()

                if any (rol in roles_permitidos for rol in roles_usuario):
                    return f(*args,**kwargs)
               
            flash('Acesso no permitido: No tienes permisos suficientes.','warning')
            return redirect(url_for('login.login'))
        return etiqueta
    return caja