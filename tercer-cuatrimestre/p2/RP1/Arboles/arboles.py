class Arbol:
    def __init__(self,cargo,left,right) -> None:
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self) -> str:
        return str(self.cargo)


def agregar_nodo(nodo_nuevo, arbol):
    if arbol == None:
        return Arbol(nodo_nuevo, None, None)
    else:
        if nodo_nuevo < arbol.cargo:
            arbol.left=Arbol(arbol.cargo, agregar_nodo(nodo_nuevo, arbol.left), arbol.right)
        elif nodo_nuevo > arbol.cargo:
            arbol.right=Arbol(arbol.cargo, arbol.left, agregar_nodo(nodo_nuevo, arbol.right))
        else:
            return arbol

def crear_arbol(lista_nodos):
    arbol = None
    while(lista_nodos!=[]):
        cargo=lista_nodos.pop()
        arbol=agregar_nodo(cargo, arbol)
    return arbol

def crear_arbol_recursivo(lista_nodos, arbol=None):
    if lista_nodos == []:
        return arbol
    arbol=agregar_nodo(cargo,arbol)
    cargo=crear_arbol(lista_nodos[1:])
    
def buscar(dato, arbol):
    if arbol == None:
        return False
    else:
        if dato < arbol.cargo:
            return buscar(dato, arbol.left)
        elif dato > arbol.cargo:
            return buscar(dato, arbol.right)
        else:
            return True

def pre_order(arbol):
    if arbol == None:
        return
    print(arbol.cargo)
    pre_order(arbol.left)
    pre_order(arbol.right)

def in_order(arbol):
    if arbol == None:
        return
    in_order(arbol.left)
    print(arbol.cargo)
    in_order(arbol.right)

def post_order(arbol):
    if arbol == None:
        return
    post_order(arbol.left)
    post_order(arbol.right)
    print(arbol.cargo)
