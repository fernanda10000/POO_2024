from coches import *
#Crear un objetos o instanciar la clase

#print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
#coche1.getInfo()

#print("Objeto 2")
#coche2=Coches("Azul","Nissan","2020",180.150,6)
#coche2.getInfo()

print(coche1.publico_atributo)
#print(coche1.__privado_atributo)
print(coche1.getPrivadoAtributo())
coche1.getMetodoPublica()