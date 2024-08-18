from conexionbd import *

try:
    micursor=conexion.cursor()

    sql="update habitaciones set camas=´2´  where id=2¨"
    micursor.execute(sql)
    conexion.commit()
except:
    print("hubo un erro con la actualizacion")
else:
    print("la actualizacion fe exitosa")

    