print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
opcion=input("\t Elige una opción: ").upper()

solicitarNumeros()
print(operacionAritmetica(n1,n2,opcion))

print("             ..:::CALCULADORA BASICA:::..               ")
print("///Bienvenido, realiza tus operaciones facil y rapido///") 
print("         elige la funcion que quieras realizar:         ")

print("1°:suma")
print("2°:resta")
print("3°:multiplicacion")
print("4°:division")
print("5°:salir")

opcion=(input("¿que operacion desea realizar?: "))

if opcion=="+" or opcion=="suma" or opcion== "1":
     n1=int(input("numero #1: "))
     n2=int(input("numero #2: "))
     print(f"{n1}+{n2}={n1+n2}")
elif opcion=="-" or opcion=="resta" or opcion== "2":
     n1=int(input("numero #1: "))
     n2=int(input("numero #2: "))
     print(f"{n1}-{n2}={n1-n2}")
elif opcion=="*" or opcion=="multiplicacion" or opcion== "3":
     n1=int(input("numero #1: "))
     n2=int(input("numero #2: "))
     print(f"{n1}*{n2}={n1*n2}")
elif opcion=="/" or opcion=="division" or opcion== "4":
     n1=int(input("numero #1: "))
     n2=int(input("numero #2: "))
     print(f"{n1}/{n2}={n1/n2}")
elif opcion=="5" or opcion=="salir":
    print("terminaste tu operacion")