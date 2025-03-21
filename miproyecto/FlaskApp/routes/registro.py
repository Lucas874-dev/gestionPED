from flask import Blueprint, render_template, redirect, url_for, flash, request
from config import app, mysql
from flask_bcrypt import Bcrypt
from formularios.forms import RegistroForm

bcrypt = Bcrypt(app)

registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/registro', methods=['GET', 'POST'])

def registro():

    '''Utilizamos la libreria Flask-WTF para
    la validacion y renderizacion de los formularios'''

    form = RegistroForm()
    
    #print("request.method:", request.method)   Muestra si es POST o GET
    #print("request.form:", request.form)   Verifica qué datos está enviando el formulario
    #print("CSRF Token:", request.form.get("csrf_token"))   Revisa si el token se está enviando
    
    if form.validate_on_submit():
        '''En esta seccion capturamos las datos enviados
        por medio del formulario y lo almancenamos en 
        variables para sus posterior uso'''
     

        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        contraseña = form.contraseña.data
        

        print(f"nombre:{nombre},apellido:{apellido},email:{email},contraseña:{contraseña}")


        '''En esta variable por medio de la libreria
        brypt incriptamos la  antes de almacenarla
         para que sea mas segura'''
        contraseña_incriptada = bcrypt.generate_password_hash(contraseña).decode('utf-8')

        """Usamos sentencias sql para insertar los
        datos del formulario en la tabla de la base de datos,
        se crea una variable y se guarda la conexion"""

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (nombre, apellido, email, contraseña) VALUES (%s, %s, %s, %s)", 
                    (nombre, apellido, email, contraseña_incriptada))
        mysql.connection.commit()
        cur.close() 
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        
        return redirect(url_for('registro.registro'))

    return render_template('registro.html', form=form)
