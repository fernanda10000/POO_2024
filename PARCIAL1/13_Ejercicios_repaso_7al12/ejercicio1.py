#1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
# a.- Recorrer la lista y mostrarla
# b.- hacer una funcion que recorra la lista de numeros y devuelva un string
# c.- ordenarla y mostrarla
# d.- mostrar su longitud
# e.- buscar algun elemento que el usuario pida por teclado


# Lista de 8 números enteros
numeros = [23, 5, 67, 12, 98, 45, 34, 56]

# a. Recorrer la lista y mostrarla
def mostrar_lista(lista):
    for numero in lista:
        print(numero)

print("a. Recorrer la lista y mostrarla:")
mostrar_lista(numeros)

# b. Hacer una función que recorra la lista de números y devuelva un string
def lista_a_string(lista):
    return ', '.join(map(str, lista))

print("\nb. Lista convertida a string:")
print(lista_a_string(numeros))

# c. Ordenarla y mostrarla
numeros_ordenados = sorted(numeros)
print("\nc. Lista ordenada:")
print(numeros_ordenados)

# d. Mostrar su longitud
print("\nd. Longitud de la lista:")
print(len(numeros))

# e. Buscar algún elemento que el usuario pida por teclado
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento} se encuentra en la lista."
    else:
        return f"El elemento {elemento} no se encuentra en la lista."

# Solicitar al usuario un número para buscar
elemento_a_buscar = int(input("\nIngresa el número que deseas buscar: "))
print(buscar_elemento(numeros, elemento_a_buscar))
