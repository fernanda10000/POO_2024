import mysql.connector

conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hotel'
)

if conexion.is_connected():
    print("Se conecto con la BD")

#Crear una tabla dentro de una BD existente
sql="create table clientes (id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))"

micursor=conexion.cursor()

micursor.execute(sql)

if micursor:
  print("Se creo la tabla con exito")

