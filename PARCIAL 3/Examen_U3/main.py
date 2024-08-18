from clientes import cliente
from autos import auto
from revisiones import revision
from usuarios import usuario
from funciones import *
import getpass
import os


def Menucliente():
    while True:
        os.system("cls")
        print("""
            .::  CLIENTES  ::. 
                1.- Insertar
                2.- Consultar
                3.- Actualizar
                4.- Eliminar 
                5.- Salir  
                """)
        opcion=input("Ingrese la opcion: ").upper()
        if opcion=="1" or opcion=="INSERTAR":
            os.system("cls")
            nif=input("Ingrese el NIF ")
            nombre=input("Ingrese el nombre: ")
            direccion=input("Ingrese la direccion: ")
            ciudad=input("Ingrese la ciudad: ")
            telefono=input("Ingrese el telefono ")
            objeto_cliente=cliente.Clientes(nif,nombre,direccion,ciudad,telefono)
            resultado=objeto_cliente.Crear()
            if resultado:
                print(f"\n\t\t.::El cliente {nombre} se registro correctamente::.")
            else:
                print(f"\n\t\t**No fue posible registrar al cliente... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="2" or opcion=="CONSULTAR":
            os.system("cls")
            cliente.Clientes.Mostrar_clientes()
            EspereTecla()
 
        elif opcion=="3" or opcion=="ACTUALIZAR":
            os.system("cls")
            nif=input("Ingrese el nif: ")
            direccion=input("Ingrese la nueva direccion: ")
            ciudad=input("Ingrese la nueva ciudad: ")
            telefono=input("Ingrese el nuevo telefono: ")
            resultados=cliente.Clientes.Actualizar(nif,direccion,ciudad,telefono)
            if resultados:
                print(f"\n\t\t.::Cliente actualizado correctamente::.")
            else:
                print(f"\n\t\t**No fue posible actualizar la informacion... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="4" or opcion=="ELIMINAR":
            os.system("cls")
            nif=(input("Ingrese el nif: "),)
            resultados=cliente.Clientes.Eliminar(nif)
            if resultados:
                print(f"\n\t\t.::Cliente eliminado correctamente::.")
            else:
                print(f"\n\t\t**No fue posible eliminar al cliente... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="5":
            os.system("cls")
            print("Gracias por usar el sistema!")
            break
def MenuAutos():
    while True:
        os.system("cls")
        print("""
            .::  AUTOS  ::.
                1.- Insertar
                2.- Consultar
                3.- Actualizar
                4.- Eliminar 
                5.- Salir  
                """)
        opcion=input("Ingrese la opcion: ").upper()
        if opcion=="1" or opcion=="INSERTAR":
            os.system("cls")
            matricula=input("Ingrese la matricula: ")
            marca=input("Ingrese la marca: ")
            modelo=input("Ingrese el modelo: ")
            color=input("Ingrese el color: ")
            nif=input("Ingrese el NIF ")
            ob_auto=auto.Autos(matricula,marca,modelo,color,nif)
            resultado=ob_auto.Crear()
            if resultado:
                print(f"\n\t\t.::El auto {matricula} se registro correctamente::.")
            else:
                print(f"\n\t\t**No fue posible registrar el auto... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="2" or opcion=="CONSULTAR":
            os.system("cls")
            auto.Autos.mostrar_todo()
            EspereTecla()
        elif opcion=="3" or opcion=="ACTUALIZAR":
            os.system("cls")
            matricula=input("Ingrese la matricula: ")
            marca=input("Ingrese la nueva marca: ")
            modelo=input("Ingrese el nuevo modelo: ")
            color=input("Ingrese el nuevo color: ")
            resultados=auto.Autos.Actualizar(matricula,marca,modelo,color)
            if resultados:
                print(f"\n\t\t.::Auto actualizado correctamente::.")
            else:
                print(f"\n\t\t**No fue posible actualizar la informacion... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="4" or opcion=="ELIMINAR":
            os.system("cls")
            matricula=(input("Ingrese la matricula: "),)
            resultados=auto.Autos.Eliminar(matricula)
            if resultados:
                print(f"\n\t\t.::Auto eliminado correctamente::.")
            else:
                print(f"\n\t\t**No fue posible eliminar el auto... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="5":
            os.system("cls")
            print("Gracias por usar el sistema!")
            break
def MenuRevisiones():
    while True:
        os.system("cls")
        print("""
            .::  REVISIONES  ::.
                1.- Insertar
                2.- Consultar
                3.- Actualizar
                4.- Eliminar 
                5.- Salir  
                """)
        opcion=input("Ingrese la opcion: ").upper()
        if opcion=="1" or opcion=="INSERTAR":
            os.system("cls")
            n_revision=input("Ingrese el numero de revision: ")
            cambiofiltro=input("Ingrese el cambio de filtro: ")
            cambioaceite=input("Ingrese el cambio de aceite: ")
            cambiofrenos=input("Ingrese el cambio de frenos: ")
            otro=input("Ingrese otro servicio: ")
            matricula=input("Ingrese la matricula del vehiculo: ")
            ob_revision=revision.Revisiones(n_revision,cambiofiltro,cambioaceite,cambiofrenos,otro,matricula)
            resultado=ob_revision.Crear()
            if resultado:
                print(f"\n\t\t.::La revision {n_revision} se registro correctamente::.")
            else:
                print(f"\n\t\t**No fue posible registrar la revision... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="2" or opcion=="CONSULTAR":
            os.system("cls")
            revision.Revisiones.mostrar_registros()
            EspereTecla()
        elif opcion=="3" or opcion=="ACTUALIZAR":
            os.system("cls")
            n_revision=input("Ingrese el numero de revision: ")
            cambiofiltro=input("Ingrese el cambio de filtro: ")
            cambioaceite=input("Ingrese el cambio de aceite: ")
            cambiofrenos=input("Ingrese el cambio de frenos: ")
            otro=input("Ingrese otro servicio: ")
            resultados=revision.Revisiones.Actualizar(n_revision,cambiofiltro,cambioaceite,cambiofrenos,otro)
            if resultados:
                print(f"\n\t\t.::Revision actualizada correctamente::.")
            else:
                print(f"\n\t\t**No fue posible actualizar la informacion... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="4" or opcion=="ELIMINAR":
            os.system("cls")
            n_folio=(input("Ingrese el numero de revison: "),)
            resultados=revision.Revisiones.Eliminar(n_folio)
            if resultados:
                print(f"\n\t\t.::Revision eliminada correctamente::.")
            else:
                print(f"\n\t\t**No fue posible eliminar la revision... vuelva a intentarlo**")
            EspereTecla()
        elif opcion=="5":
            os.system("cls")
            print("Gracias por usar el sistema!")
            break
def MenuSecundario():
    while True:
        os.system("cls")
        print("""
        .::  Menu  ::. 
            1.- Clientes
            2.- Autos
            3.- Revisiones
            4.- Salir
            """)
        opcion = input("\t Elige una opción: ").upper()
        if opcion=="1" or opcion=="CLIENTES":
            Menucliente()
        elif opcion=="2" or opcion=="AUTOS":
            MenuAutos()
        elif opcion=="3" or opcion=="REVISIONES":
            MenuRevisiones()
        elif opcion=="4" or opcion=="SALIR":
            print("Hasta luego!")
            break


def menu_principal():
    while True:
        os.system("cls")
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "REGISTRO":
            os.system("cls")
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellido=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            empleado=input("\t Ingrese su numero su nif: ")
            obj_usuario=usuario.Usuario(nombre, apellido, email, password,empleado)
            resultado=obj_usuario.registrar()
            if resultado:
                print(f"\n\t{nombre} {apellido}, se registro correctamente con el email {email}")
            else:
                print(f"\n\t **Por favor inténtelo de nuevo más tarde")
            EspereTecla()
        elif opcion == '2' or opcion == "LOGIN":
            os.system("cls")
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            registro = usuario.Usuario.iniciarSesion(email, password)
            if len(registro)>0:
                MenuSecundario()
            else:
                print(f"\n\t Email y/o contraseña incorrectas...vuelva a intentarlo")
                EspereTecla()

        elif opcion == '3' or opcion == "SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            EspereTecla()
menu_principal()

