# Ejercicio 1
'''
- cambiar valor:Creamos una funcion a la cual le vamos a ir actualizando el valor
'''

# Ejercicio 2
class Celda:
    def __init__(self, valor):
        self.valor=valor

    def __str__(self):
        if self.valor:
            return str(self.valor)

    def valor_nuevo(self, valor_nuevo):
        self.valor = valor_nuevo
        return str(self.valor)
celdaPrueba1=Celda(4)
print(celdaPrueba1)
celdaPrueba1.valor_nuevo(3)
print(celdaPrueba1)
# Ejercicio 3
'''
Nosotros tenemos una tupla ya que nuestros valores son constantes
Nosotros en nuestra funcion pertenece vamos a corroborar que el valor que queremops buscar este.
'''
# Ejercicio 4
class Conjuntos:
    def __init__(self, conjunto):
        self.conjunto=conjunto
    def __str__(self):
        if self.conjunto:
            return str(self.conjunto)
    def elemento_incluido(self, elemento):
       for i in self.conjunto:
        if elemento == i:
            print('el elemento esta en la tupla')
        else:
            print('el elemento no esta')
tuplita=[1,2,3]
tupla1=Conjuntos(tuplita)
tupla1.elemento_incluido(2)

# Ejercicio 6

class Nodo:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self, primer_elemento):
        self.primer_elemento=primer_elemento

    def ver_lista(self):
        nodito=self.primer_elemento
        while nodito:
            print(nodito)
            nodito=nodito.prox

n3=Nodo('chau')
n2=Nodo('mati', n3)
n1=Nodo('hola', n2)
lista1=ListaEnlazada(n1)

lista1.ver_lista()

# Ejercicio 7
class Nodo7:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return str(self.dato)

    def insert(self):
        pass

    def index(self):
        pass

class ListaEnlazada2(Nodo7):
    def __init__(self, primer_elemento, len: int)->None:
        self.primer_elemento=primer_elemento
        self.len=0

    def ver_lista(self):
        nodito2=self.primer_elemento
        while nodito2:
            print(2)
            nodito2=nodito2.prox

n6=Nodo7('chau')
n5=Nodo7('mati', n6)
n4=Nodo7('hola', n5)
lista2=ListaEnlazada(n4)

lista2.ver_lista()
