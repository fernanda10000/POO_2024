import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost"
        user="root"
        password=""
    )
except:
    print("RESULTO UN ERROS EN EL SERVIDOR")
else:
    if conexion.is_connected():
        print("Se creo la conexion con exito")

    micursor=conexion.cursor()

    sql="create databases bd_hotel"
    micursor.execute(sql)

    if micursor:
        print ("se creo base de datos")
    
    micursor.execute("show databases")

  














