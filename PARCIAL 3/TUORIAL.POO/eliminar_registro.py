from conexionbd import *


try:
    micursor=conexion.cursor()
    sql="delete from habitacion"

    micursor.execute(sql)
    conexion.commit()
except:
    print("ocurrio un error")
else:
    print("registro eliminado correctamente")
    