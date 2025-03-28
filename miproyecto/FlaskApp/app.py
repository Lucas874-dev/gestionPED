from config import app, login_manager, mysql
'''Importamos los Blueprints de las 
Rutas'''
from routes.registro import registro_bp  
from routes.login import login_bp
from routes.admin import admin_bp
from routes.logout import logout_bp
from routes.mesero import mesero_bp
from routes.cocinero import cocinero_bp
from routes.cajero import cajero_bp
'''Estructura de los datos del usuario. Esta 
Estructura utiliza Flask-Login para extraer los datos
del usuario, segun el ID'''
from models import Usuario
from flask_login import LoginManager

'''Registro de Blueprints: De esta
manera organizamos las rutas en modulos
separados y asi mantenemos el codigo mas limpio'''
app.register_blueprint(registro_bp)
app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(mesero_bp)
app.register_blueprint(cocinero_bp)
app.register_blueprint(cajero_bp)

'''Esta fucnion nos permite cargar el
usuario en Flask-Login.'''

@login_manager.user_loader
def cargar_usuario(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id_usuario = %s",(user_id,))
    user = cur.fetchone()
    cur.close()

    if user:
        return Usuario(user['id_usuario'], user['nombre'],user['apellido'],user['telefono'],
         user['email'],user['contraseña'])
    return None


if __name__ == '__main__':
    app.run(debug=True)
