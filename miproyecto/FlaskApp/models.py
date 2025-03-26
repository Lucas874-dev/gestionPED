from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nombre,telefono, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.email= email
        self.telefono= telefono
        self.contraseña= contraseña


class control_rol():
    def __init__(self,user_id):
      from config import mysql, app 
      from flask import flash, redirect, url_for
      cur= mysql.connection.cursor()
      
      cur.execute('''SELECT ur.id_usuario,ur.id_rol,r.nombre as nombre_rol,u.nombre as nombre_usuario FROM usuario_rol as ur 
      INNER JOIN usuarios as u ON u.id_usuario= ur.id_usuario
      INNER JOIN roles as r ON ur.id_rol= r.id_rol
      WHERE ur.id_usuario =%s''',(user_id,))

      self.roles = cur.fetchone()
      cur.close()

    def obtener_rol(self):
     if self.roles:
        return self.roles['nombre_rol']
     return None 


