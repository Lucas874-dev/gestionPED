from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nombre, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.email= email
        self.contraseña= contraseña
