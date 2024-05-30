"""Programa para calcular el IMC de una persona:
        IMC          CLASIFICACION
 =====================================
   < 18.5     ->Peso Inferior al normal 
18.5 - 24.9 -> normal
25.0 - 29.9 -> peso superior al normal
30.0 - 34.9 -> obesidad 


IMC = peso / (estatura * estatura)
"""

def calcularIMC(p, a):

    return p / (a * a)

def NivelDePeso(IMC):
    if IMC < 18.5:
        return "bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "normal"
    elif 25 <=IMC <= 29.9:
        return "sobre peso"
    elif 30 <= IMC <= 34.9:
        return "obesidad I"
    elif 35 <= IMC <= 50:
        


peso = float(input("ingrese el peso (kg):  "))
altura = float(input("ingrese la estatura (m): "))
print("su nivel de peso es:", NivelDePeso(calcularIMC(peso, altura)))

 # Preguntar al usuario si desea realizar otro cálculo
otra_vez = input("¿Desea calcular otro IMC? (s/n): ")
if otra_vez != 's': 
    break

print("Se realizaron un total de", contador_calculos, "cálculos de IMC."): 