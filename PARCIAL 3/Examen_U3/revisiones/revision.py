from conexionBd import *
class Revisiones:
    def __init__(self,n_revision,cambiofiltro,cambioaceite,cambiofrenos,otro,matricula):
        self.n_revision=n_revision
        self.cambiofiltro=cambiofiltro
        self.cambioaceite=cambioaceite
        self.cambiofrenos=cambiofrenos
        self.otro=otro
        self.matricula=matricula

    def Crear(self):
        try:
            sql="INSERT INTO revisiones (no_revision,cambiofiltro,cambioaceite,cambiofrenos,otros,matricula) VALUES (%s,%s,%s,%s,%s,%s)"
            valor=(self.n_revision,self.cambiofiltro,self.cambioaceite,self.cambiofrenos,self.otro,self.matricula)
            cursor.execute(sql,valor)
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def mostrar_registros():
        try:
          cursor.execute("SELECT * FROM revisiones")
          resultados = cursor.fetchall()
          print(".::DATOS DE LA REVISION::.")
          for fila in resultados:
             print(f" Folio: {fila[0]} \n Cambio de filtro: {fila[1]}\n Cambio de aceite: {fila[2]}\n Cambio de frenos: {fila[3]}\n Otro: {fila[4]}\n Matricula: {fila[5]}")
        except:
            print("**No existen registros... vuelva a intentar")
    @staticmethod
    def Actualizar(n_revision,cambiofiltro,cambioaceite,cambiofrenos,otro):
        try:
            sql="UPDATE revisiones SET  cambiofiltro= %s,cambioaceite=%s,cambiofrenos=%s,otros=%s WHERE no_revision = %s"
            cursor.execute(sql,(cambiofiltro,cambioaceite,cambiofrenos,otro,n_revision))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def Eliminar(n_folio):
        try:
            sql="DELETE FROM revisiones WHERE no_revision = %s"
            cursor.execute(sql,n_folio)
            conexion.commit()
            return True
        except:
            return False
