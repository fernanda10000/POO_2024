import os
import math

def SolicitarNumeros():
    global n1, n2
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

def OperacionesArit(n1, n2):
    global i
    #====Suma=====
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        suma = n1 + n2
        return(f"{n1} + {n2} = {suma}")

    #=====Resta=====
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        resta = n1 - n2
        return(f"{n1} - {n2} = {resta}")

    #=====Multiplicación=====
    elif opcion == "3" or opcion == "x" or opcion == "MULTIPLICACION":
        multiplicacion = n1 * n2
        return(f"{n1} x {n2} = {multiplicacion}")

    #=====División=====
    elif opcion == "4" or opcion == "/" or opcion == "DIVICION":
        if n2 != 0:
            division = n1 / n2
            return(f"{n1} / {n2} = {division}")
        else:
            return("No se puede dividir entre cero")

    #=====Potencia=====
    elif opcion == "5" or opcion == "**" or opcion == "POTENCIA":
        potencia = n1 ** n2
        return(f"{n1} ^ {n2} = {potencia}")

    #=====Raíz=====
    elif opcion == "6" or opcion == "√" or opcion == "RAIZ":
        if n1 >= 0:
            raiz = math.sqrt(n1)
            return(f"√{n1} = {raiz}")
        else:
            return("No se puede calcular la raíz cuadrada de un número negativo")

i = True
while i:
    os.system("clear")
    print(f"========== \n Calculadora Básica \n=============")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Potencia")
    print("6.- Raíz")
    print("7.- Salir")
    opcion = input("Elige una opción ").upper()

    if opcion == "7":
        print("Saliste")
        i = False
    elif opcion in ["1", "2", "3", "4", "5"]:
        SolicitarNumeros()
        print(OperacionesArit(n1, n2))
    elif opcion == "6":
        n1 = int(input("Número: "))
        n2 = None  # No se usa en la raíz, pero se mantiene para la estructura
        print(OperacionesArit(n1, n2))
    else:
        print("Opción no válida")
        