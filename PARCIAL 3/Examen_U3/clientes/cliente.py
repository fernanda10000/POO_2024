from conexionBd import *
class Clientes:
    def __init__(self, nif,nombre,direccion,ciudad,telefono):
        self.conexion=conexion
        self.nif=nif
        self.nombre=nombre
        self.direccion=direccion
        self.ciudad=ciudad
        self.telefono=telefono

    def Crear(self):
        try:
            sql="INSERT INTO clientes (nif,nombre,direccion,ciudad,telefono) VALUES (%s,%s,%s,%s,%s)"
            valor=(self.nif,self.nombre,self.direccion,self.ciudad,self.telefono)
            cursor.execute(sql,valor)
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def Mostrar_clientes():
        try:
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            print(".::DATOS DE CLIENTES::.")
            for fila in resultados:
                        print(f" Nombre: {fila[1]} \n Direccion: {fila[2]}\n Ciudad: {fila[3]}\n Telefono: {fila[4]}")
        except:
            print("**No existe este el cliente... vuelva a intentar")
    @staticmethod
    def Actualizar(nif,direccion,ciudad,telefono):
        try:
            sql="UPDATE clientes SET  direccion= %s, ciudad=%s, telefono=%s WHERE nif = %s"
            cursor.execute(sql,(direccion,ciudad,telefono,nif))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def Eliminar(nif):
        try:
            #nif=(input("Ingrese su NIF: "),)
            sql="DELETE FROM clientes WHERE nif = %s"
            cursor.execute(sql,nif)
            conexion.commit()
            return True
        except:
            return False
    