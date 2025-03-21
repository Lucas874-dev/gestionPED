from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager

"""Con un archivo de configuracion independiente
promovemos el facil mantenimineto del mismo y
una estrucutura mas ordenada de los elementos 
de la aplicacion"""

app = Flask(__name__)

'''Configuracion de la conexion a la base de datos.
Colocamos todas las credenciales necesarias para validar
y autorizar la conexion al servidor de la base de datos 
'''
    
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'guadalupe'
app.config['MYSQL_DB'] = 'restaurante'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #Permite que las consultas devuelvan diccionarios

'''Configuracion de la seguridad de la aplicacion.
ESTA CONTRASEÑA DEBE SER MODIFICADA EN ENTORNOS DE 
PRODUCCION. Esta clave nos sirve para firmar Cookies
y proteger las sesiones utilizadas'''

app.config['SECRET_KEY'] = 'clavesecreta' 

'''Inicializacion de la conexion Mysql'''

mysql = MySQL(app)

'''Configuracion de Flask-Login.
Esta es una libreria que nos ayuda a gestionar las sesiones, 
esta informacion nos ayuda a proteger vistas de usuarios no
autorizados en la APP'''

login_manager = LoginManager(app)
login_manager.login_view= 'login.login' #Redirige al usuario si no esta autenticado

@login_manager.unauthorized_handler # Si no esta autorizado se envia un mensaje personalizado ubicado en la funcion noautoriado.
def noautorizado():
    from flask import flash,redirect,url_for
    flash("Debes iniciar sesion para acceder a esta pagina","warning")
    return redirect(url_for('login.login'))