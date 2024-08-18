
import mysql.connector

#Conectar con la BD MySQL
conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_notas'
)

#verificar la conexion a la BD
# if conexion.is_connected():
#     print(f"Se creo la conexion con la BD exitosamente")
# else:
#     print(f"No fue posible conectar con la BD ... verifique ...")    

#cremar un objeto de tipo cursos que se pueda feitilzaqr nuevamente 
cursor=conexion.cursos()