def r(n,d):
    if n>1:
        if n%d==0:
            print(d)
            r(n//d, d)
        else:
            r(n, d+1)

r(30,2)

def i(n,d):
    while n>1:
        if n%d==0:
            print(d)
            n=n//d
        else:
            d+=1

i(30,2)

# Esto va a imprimir todos los divisores(d) primos de n


def postorden(tree):
    if tree is None:
        return tree
    postorden(tree.left)
    postorden(tree.right)
    print(tree.cargo)

class Grafo:
    def __init__(self):
        self.vertices=[]
        self.vecinos={}

    def add_node(self, vertice):
        self.vertices.append(vertice)
        self.vecinos[vertice]=[]

    def add_edge(self, vertice1, vertice2):
        self.vecinos[vertice1].append(vertice2)
        self.vecinos[vertice2].append(vertice1)

    def vecinos_grado_3(self, vertice):
        for vecinos in self.vertices[vertice]:
            print(vecinos)

'''
Lista A de numeros enteros de longitud n>0 y dos enteros aa, b tales que 0 <= a < b <= n y devuleva el numero mas grande
en el intervalo L[a:b] es decir el numero mas grande que esta en la lista entre los indices a y b incluyendo el primero
pero no el ultimo
'''
def esCasoBase(a,b):
    return b-a == 1

def resolverCasoBase(lista:list,a):
    return len(lista)

def dividir(lista:list, a,b):
    mitad=(a+b)//2
    return (lista[a:mitad], a), (lista[mitad:b],b), mitad

def combinar(v1, v2):
    return max(v1,v2)

def resolver(lista:list, a,b):
    if esCasoBase(a,b):
        return resolverCasoBase(lista,a)
    (m1,a1),(m2,b1),mitad=dividir(lista, a,b)
    r1=resolver(m1,a1,mitad)
    r2=resolver(m2,mitad,b1)
    return combinar(r1,r2)

lista=[0,1,2,3,4,5,6,7,8,9]
a=3
b=7
maxvalue=resolver(lista,a,b)
print('valor', maxvalue)
m1=[3,4]
m2=[5,6]


def esCasoBase(lista: list, a: int, b: int) -> bool:
    return b - a == 1  # Es caso base si solo hay un elemento en el intervalo

def resolverCasoBase(lista: list, a: int) -> int:
    return lista[a]  # Devuelve el único elemento en el caso base

def dividir(a: int, b: int):
    mitad = (a + b) // 2
    return (a, mitad), (mitad, b)  # Devuelve los límites de las dos mitades

def combinar(v1: int, v2: int) -> int:
    return max(v1, v2)  # Devuelve el máximo de dos valores

def resolver(lista: list, a: int, b: int) -> int:
    if esCasoBase(lista, a, b):
        return resolverCasoBase(lista, a)

    (a1, m1), (m2, b2) = dividir(a, b)
    max1 = resolver(lista, a1, m1)
    max2 = resolver(lista, m2, b2)

    return combinar(max1, max2)

# Ejemplo de uso
L = [3, 5, 1, 8, 4, 7]
a = 1
b = 4
resultado = resolver(L, a, b)
print("El número más grande en el intervalo L[{}:{}] es: {}".format(a, b, resultado))