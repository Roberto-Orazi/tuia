from typing import Any


def verificar_suma (L:int, n: int)->bool:
    if len(L) == 0:
        return n == 0
    for i in range(n//L[0] + 1):
        if(verificar_suma(L[1:],n-i*L[0])):
            return True
    return False

print(verificar_suma([5,3,9],7)) # False
print(verificar_suma([5,1,9],31)) # True



def cantidad_nodos(tree, suma:int=0)->int:
    if tree is None:
        return suma

    if tree.left is not None and tree.right is not None:
        suma+=1

    suma = cantidad_nodos(tree.left, suma)
    suma = cantidad_nodos(tree.right, suma)

    return suma

class Grafo:
    def __init__(self)->None:
        self.vertices=[]
        self.vecinos={}

    def add_node(self, vertice: Any)-> None:
        self.vertices.append(vertice)
        self.vecinos[vertice]=[]

    def add_edge(self, vertice1: Any, vertice2: Any)->None:
        self.vecinos[vertice1].append(vertice2)
        self.vecinos[vertice2].append(vertice1)


def grafo_k_regular(G: Grafo, k: int)-> bool:
    if len(G.vertices) != k:
        return False

    for vertice in G.vertices:
        if len(G.vecinos[vertice]) != k:
            return False

    return True


def es_caso_base(a:int,b:int)->int:
    return b-a == 0

def resolver_caso_base(lista):
    return lista[0]

def dividir(lista:list[int],a:int,b:int)->tuple[list[int], list[int]]:
    pass

def combinar(m1:list[int],m2:list[int]):
    pass

def resolver(lista: list[int], a:int,b:int)->int:
    pass
