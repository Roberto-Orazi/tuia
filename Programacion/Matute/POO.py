
"""
Curso de programacion orientada a objetos de python

"""
class Mylist():
    def __init__(self, any_list : list[int])-> None:
        self.any_list = any_list
    def square(self):
        lista = []
        for x in self.any_list:
            square = x * x
            lista.append(square)
        return lista
    def doble(self):
        listaDoble = []
        for x in self.square():
            doble = 2 * x
            listaDoble.append(doble)
        return listaDoble
    def sum(self):
        return(sum(self.doble()))

lista1 = Mylist([1,2,3,4,5,6])
print(lista1.sum())
"""
En este caso estamos representando una alternativa al paradigma imperativo
Estamos creando una instancia de la clase lista, lo que sus metodos podran hacer
es elevarla al cuadrado, multiplicarlas por 2 y sumarlas para devolver un entero.
"""


