#Todas las variables de python son polimorfas
#Las variables puede tomar distintos tipos de datos
#Es lenguaje de tipado dinamico
#Hay muchos tipos de polimorfismo


class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato=Gato()
perro=Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(gato)
hacer_sonido(perro)

#POLIMORFISMO DE HERENCIA O SUBCLASE
class Animal():
     def sonido(self):
        pass
class Oveja(Animal):
    def sonido(self):
        return "Bee"

class Abeja(Animal):
    def sonido(self):
        return "sssss"

def hacer_sonido(animal):
    print(animal.sonido())

oveja=Oveja()
abeja=Abeja()

print(oveja.sonido())
print(abeja.sonido())

hacer_sonido(oveja)
hacer_sonido(abeja)

#POLIMORFISMO DE CONVERSION
num1=3
num2=4.4

resultado=num1+num2

print(resultado)
print(type(resultado))

def recorrer(elemento):
    for item in elemento:
        print(item)

lista=[1,2,3,4]
lista2=['maquina','como','andas']
lista3='wachin'

recorrer(lista) #imprime 1 por 1 elementos
recorrer(lista2) #imprime 1 por 1 elementos
recorrer(lista3) #imprime 1 por 1 caracter

#TENEMOS TIPO REAL Y TIPO DINAMICO YA QUE EL TIPO DE DATO CAMBIA CON LA HERENCIA
