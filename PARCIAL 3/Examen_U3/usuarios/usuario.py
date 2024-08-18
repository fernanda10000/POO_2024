from conexionBd import *
import hashlib
import datetime
class Usuario:
    def __init__(self, nombre, apellido, usuario, password,cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = self.hash_password(password)
        self.cliente=cliente

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s,%s)",
                (self.nombre, self.apellido, self.usuario, self.contrasena,fecha,self.cliente)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def iniciarSesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where usuario=%s and password=%s",
                (email, contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return []
        except:
            return []