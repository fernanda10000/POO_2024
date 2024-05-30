def numeros_impares(inicio, fin):
    if inicio > fin:
        inicio, fin = fin, inicio  # Asegurarse de que inicio sea menor que fin
    for numero in range(inicio, fin + 1):
        if numero % 2 != 0:
            print(numero)

# Solicitar los números al usuario
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

# Llamar a la función para mostrar los números impares
numeros_impares(inicio, fin)
