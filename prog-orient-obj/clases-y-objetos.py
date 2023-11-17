'''
En las clases se usa PascalCase
'''
class NombreClase():
    propiedad1 = 'Valor 1'
    propiedad2 = 'Valor 2'
    propiedad3 = 'Valor 3'

class Celular():
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

#Aca estamos creando una instancia de la clase osea estamos creando un objeto
celular1 = Celular()
#Osea los objetos son la instancia de una clase
#Las propiedades de las clases son fijas, ya que cambiarlo es poco practico
celular1.marca = 'Apple'
print(celular1.marca)
print(celular1) #Nos muestra que es un objeto de main que es el modulo que estamos manejando
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)

