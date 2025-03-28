from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

'''La utilizacion de la libreria Flas-Wtf, nos aseguramos 
de su VALIDACION, ya que los datos cumplan ciertos requisitos
antes de procesarlos. Su SEGURIDAD ya que incorpora proteccion
CSRF. Y su facil implementacion, ya que nos permite renderizar
el formulario en la plantilla de manera sencilla
'''
class RegistroForm(FlaskForm):
    
    nombre = StringField('Nombre', validators=[DataRequired(message="Rellene este campo."), Length(min=5, max=15, message="Debe tener al menos 5 caracteres")])
    apellido = StringField('Apellido', validators=[DataRequired(message="Rellene este campo."), Length(min=5, max=15,message="Debe tener al menos 5 caracteres")])
    telefono = StringField('Telefono', validators=[DataRequired(message="Rellene este campo."), Length(min=10,message="Debe tener al menos 10 caracteres")])
    email = StringField('Email', validators=[DataRequired(message="Rellene este campo."), Email(message="Ingrese un Email.")])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message="Rellene este campo."), Length(min=6,max=20,message="Debe tener al menos 6 caracteres")])
    confirmar_contraseña = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Rellene este campo."), EqualTo('contraseña',message="No coinciden las contraseñas")])
    submit = SubmitField('Registrarse')


class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(message="Ingrese su Email")])
    contraseña = PasswordField("Contraseña",validators=[DataRequired(message="Ingrese su Contraseña")])
    submit = SubmitField('Inicie Sesion')

