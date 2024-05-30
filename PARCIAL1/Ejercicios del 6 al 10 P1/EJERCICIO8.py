def calcular_porcentaje(porcentaje, numero):
    return (porcentaje / 100) * numero

# Solicitar el porcentaje y el número al usuario
porcentaje = float(input("Introduce el porcentaje: "))
numero = float(input("Introduce el número: "))

# Calcular el porcentaje del número
resultado = calcular_porcentaje(porcentaje, numero)

# Mostrar el resultado
print(f"{porcentaje}% de {numero} es {resultado}")