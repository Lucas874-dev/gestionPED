from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nombre, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.email= email
        self.contraseña= contraseña


class control_rol():
    def __init__(self):
      from config import mysql, app 
      cur= mysql.connection.cursor()
      cur.execute('''SELECT ur.id_usuario,ur.id_rol,r.nombre as nombre_rol,u.nombre as nombre_usuario FROM usuario_rol as ur 
      INNER JOIN usuarios as u ON u.id_usuario= ur.id_usuario
      INNER JOIN roles as r ON ur.id_rol= r.id_rol
      WHERE r.nombre IN ('mesero','cocinero','cajero','administrador')''')
      roles = cur.fetchone()
      cur.close()
      # print(roles['id_usuario'],roles['id_rol'],roles['nombre_rol'],roles['nombre_usuario'])
      