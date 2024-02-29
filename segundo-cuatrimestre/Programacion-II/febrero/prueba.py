""" def recursiva(numero:int) -> str:
    if (numero==0):
        return "0"
    digito=numero%10
    print(digito)
    resto = recursiva(numero//10)
    print('resto',resto)
    return str(resto)+str(digito)

prueba=recursiva(10)

print(prueba)



def calcular(a,b):
    if a==0:
        return b+1
    if b==0:
        return calcular(a-1,1)
    intermedio=calcular(a,b-1)
    return calcular(a-1,intermedio)

print(calcular(1,0))


class Entidad:
    def __init__(self,vida_inicial:int):
        self.vida=vida_inicial

class Enemigo(Entidad):
    def __init__(self,vida_inicial:int):
        super().__init__(vida_inicial)

class Jugador(Entidad):
    def __init__(self,vida_inicial:int):
        super().__init__(vida_inicial)
        self.enemigos_golpeados=[]

    def golpeado(self,cuanto):
        self.vida-=cuanto

    def golpear(self,enemigo,cuanto):
        enemigo.vida -= cuanto
        self.enemigos_golpeados.append(enemigo)

enemigo1 = Enemigo(50)
jugador = Jugador(100)
jugador.golpear(enemigo1, 20)
print(enemigo1.vida)
print(jugador.enemigos_golpeados)


class Cosa:
    def __init__(self,valor):
        self.valor=valor

class Coleccion:
    def __init__(self):
        self.coleccion=[]

    def agregar_cosa(self,cosa:Cosa):
        self.coleccion.append(cosa)

cosa=Cosa('valor')
coleccion=Coleccion()
coleccion.agregar_cosa(cosa)


def suma_cuadrada(n:int)->int:
    if n==0:
        return 0
    return(n*n + suma_cuadrada(n-1))

print(suma_cuadrada(3))

 """
class Caja:
    def __init__(self,dicc):
        lista=[1,2,5,10,20,50,100,200,500,1000]
        self.denominaciones={}

        for denominacion in dicc:
            if denominacion not in lista:
                print(f'{denominacion} no existe')
            else:
                self.denominaciones[denominacion]=dicc[denominacion]

    def total(self,total=0):
        for denominacion in self.denominaciones:
            total=total+(denominacion*self.denominaciones[denominacion])
        return total

diccionario={1:20,100:2,200:5,300:2}

caja=Caja(diccionario)

totales=caja.total()
print(totales)

class BinaryTree:
    def __init__(self,cargo,left,right):
        self.cargo=cargo
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.cargo)

def insertBST(new_data,BST_tree):
    if BST_tree==None:
        return BinaryTree(new_data)
    if new_data<BST_tree.cargo:
        return BinaryTree(BST_tree.cargo,insertBST(new_data,BST_tree.left),BST_tree.right)
    elif new_data>BST_tree.cargo:
        return BinaryTree(BST_tree.cargo,BST_tree.left,insertBST(new_data,BST_tree.right))
    else:
        return BST_tree

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None

    def invertir(self):
        if self.cabeza is None:
            return
        previo=None
        actual=self.cabeza
        siguiente=None

        while actual:
            siguiente=actual.siguiente
            actual.siguiente=previo
            previo=actual
            actual=siguiente
        self.cabeza=previo


def es_solucion(problema,solucion):
    return problema % solucion == 0

def candidatos(problema):
    for i in range(1,2,problema):
        yield i

def resolver(problema):
    for candidato in candidatos(problema):
        if es_solucion(problema,candidato):
            return candidato
    return -1


def es_caso_base(problema: "Problema") -> bool:
  pass

def resolver_caso_base(problema: "Problema") -> "Solución":
  pass

def dividir(problema: "Problema") -> "(Problema, Problema)":
  pass

def combinar(s1: "Solución", s2: "Solución") -> "Solución":
  pass

def resolver(problema: "Problema") -> "Solución":
  pass

