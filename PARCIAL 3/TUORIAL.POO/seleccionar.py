from conexionbd import *

try:

    micursor=conexion.cursor()
    sql="select habitacion,num_camas from habitacion"
    micursor.execute(sql)
    resultado=micursor.fetchall()


    if len(resultado)>0:
        print("registro de la tabla: {len{resultado}}")
   for x in resultado:
    print(x)

   except:
    print("ocurrio un problema en el servidor")
   else:
    print("registro insertado")
    