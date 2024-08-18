from conexionBD import *


class uSUARIOS:
    def __init__(self, nombre, apellidos,email, password):
        self.nombre= nombre
        self.apellidos = apellidos
        self.email = email
        self.contraseña = self.hash_password(password)

def hash_password(self, password):
    return hashlib,sha256(contrasena.encode()).hexdigest()


def registrar (self):
    fecha=datetime.datetime.now()
    cursor.execute (
        "insert into usuarios values (null, %s, %s,%s,%s)"
    )