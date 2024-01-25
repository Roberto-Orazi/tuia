class Nodo:
    def __init__(self, dato=None, prox: 'Nodo' or None = None):
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return(f'{self.dato},{self.prox}')

    def verLista(self):
        while self is not None:
            print(self)
            self=self.prox

nodo3=Nodo('hola')
nodo2=Nodo('hola2',nodo3)
nodo1=Nodo('hola1',nodo2)

nodo1.verLista()

nodo1.prox=None

nodo1.verLista()

class ListaEnlazada:
    def __init__(self):
        self.primero=None

    def __str__(self):
        nodos = []
        nodo_actual = self.primero
        while nodo_actual:
            nodos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.prox
        return " -> ".join(nodos)

    def intercambiar(self, i, j):
        if i < 0 or j < 0 or i >= self.len or j >= self.len:
            print('Posiciones invalidas')
            return
        dato_i = self.pop(i)
        dato_j = self.pop(j if j < i else j - 1)
        self.insert(i, dato_j)
        self.insert(j, dato_i)

lista = ListaEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)

print("Lista original:", lista)

lista.intercambiar(0, 2)

print("Lista después de intercambiar:", lista)