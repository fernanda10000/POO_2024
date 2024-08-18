from conexionBd import *
class Autos:
    def __init__(self, matricula,marca,modelo,color,nif):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.nif=nif
    
    def Crear(self):
        try:
            sql="INSERT INTO autos (matricula,marca,modelo,color,nif) VALUES (%s,%s,%s,%s,%s)"
            valor=(self.matricula,self.marca,self.modelo,self.color,self.nif)
            cursor.execute(sql,valor)
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def Actualizar(matricula,marca,modelo,color):
        try: 
            sql="UPDATE autos SET  marca= %s,modelo=%s,color=%s WHERE matricula = %s"
            cursor.execute(sql,(marca,modelo,color,matricula))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def Eliminar(matricula):
        try:
            sql="DELETE FROM autos WHERE matricula = %s"
            cursor.execute(sql,matricula)
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def mostrar_todo():
        try:
            cursor.execute("SELECT * FROM autos")
            resultados = cursor.fetchall()
            print(".::DATOS DEL AUTO::.")
            for fila in resultados:
                        print(f" Matricula: {fila[0]} \n Marca: {fila[1]}\n Modelo: {fila[2]}\n Color: {fila[3]}\n N. Cliente: {fila[4]}")
        except:
            print("**No existe este auto... vuelva a intentar")