from flask import Blueprint, render_template, url_for, flash, redirect
from config import app, mysql
from flask_bcrypt import Bcrypt
from flask_login import login_user
from models import Usuario
from formularios.forms import LoginForm


bcrypt = Bcrypt(app)

login_bp = Blueprint ('login', __name__)

@login_bp.route('/login', methods=['GET','POST'])

def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        
        email = form.email.data
        contraseña = form.contraseña.data

        """En esta seccion no hace falta utilizar el metodo
         brypt.generate_password_hash ya que lo que debo
         realizar es una comprabacion de la contraseña 
         ingresada en el formulario de login para validar 
         si coincide con la de la BD"""
        
        cur = mysql.connection.cursor()

        cur.execute('SELECT id_usuario, nombre, email, contraseña FROM usuarios WHERE email= %s',(email,))
        usuario = cur.fetchone()
        cur.close()

        '''Con bcrypt.check_password_hash validamos si la
        contraseña incriptada en la base de datos es la 
        misma que la ingresa por el usuario.'''

        if usuario and bcrypt.check_password_hash(usuario['contraseña'],contraseña):

            user = Usuario (usuario['id_usuario'],usuario['nombre'], usuario['email'],
            usuario['contraseña'])
            
            '''Inicia Sesion. Estable la sesion del usuario'''
            login_user(user) 

            flash(f"Bienvenido, {usuario['nombre']}!", "success")
           
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash("Correo o contraseña incorrectos.", "danger")

    return render_template ('login.html', form=form)


