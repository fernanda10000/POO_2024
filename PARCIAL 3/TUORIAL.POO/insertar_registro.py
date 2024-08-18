from conexionbd import *


try:
    micursor=conexion.cursor()

    sql="insert into habitacion(id_habitacion, num_camas,num_baños)"
    micursor.execute(sql)
    conexion.commit()
except:
    print("ocurrio un problema en el servidor")
else:
    print("registro insertado")
    