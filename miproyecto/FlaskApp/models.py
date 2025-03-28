from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nombre,apellido,email, telefono, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido= apellido
        self.email= email
        self.telefono= telefono
        self.contraseña= contraseña


class control_rol():
    def __init__(self,user_id):
      from config import mysql 
      import MySQLdb
      
      cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      
      cur.execute('''SELECT r.nombre as nombre_rol
      from usuario_rol as ur
      INNER JOIN roles as r ON ur.id_rol= r.id_rol
      WHERE ur.id_usuario = %s
      ''',(user_id,))

      self.roles = cur.fetchall() or []
      cur.close()

    def obtener_roles(self):
     if self.roles:
       return[rol['nombre_rol'] for rol in self.roles]
     return[]

