## Arboles
Los arboles son estructuras jerarquicas que se usan para modelar variedad de problemas y situaciones.

### Definicion formal
En un arbol T, es un conjunto de puntos a los que llamamos vertices y pueden estar unidos con lineas llamadas aristas. Satisface que si v y w son vertices de T, existe un unico camino desde v a w.
Un arbol con raiz es un arbol en el que un vertice se designa como raiz.

## Arboles binarios
Los arboles binarios estan entre los tipos especiales mas importantes de arboles con raiz.
Todo vertice en un arbol binario tiene a lo sumo 2 hijos. Cada hijo se asigna como izquierdo y como derecho pero no ambos. Si un vertice tiene 2 hijos uno se asigna como izquierdo y uno derecho.

Un arbol binario completo es un arbol binario en el que cada vertice tiene dos o cero hijos.

```
class BinaryTree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.cargo)

left = BinaryTree(2)
right = BynaryTree(3)

tree = BinaryTree(1,left,right)
tree = BinaryTree(1,BinaryTree(2),BynaryTree(3))
```

### Construccion arbol binario de busqueda
#### Insertar valores
```
def insertBST(new_data, BST_tree):
    if BTS_tree == None:
        return BinaryTree(new_data,None,None)
    else:
        if new_data < BST_tree:
            return BinaryTree(BST_tree.cargo, insert(new_data, BST_tree.left), BST_tree.right)
        elif new_data > BST_tree:
            return BinaryTree(BST_tree.cargo, BST_tree.left, insert(new_data, BST_tree.right))
        else:
            return BST_tree
```
#### Crear arbol
```
def createBST(data_list):
    BST_tree = None

    while(data_list!=[]):
        cargo=data_lista.pop()
        BST_tree = insertBST(cargo,BST_tree)

    return BST_tree
```
#### Busqueda de datos
```
def searchBST(D,BST_tree):
    if BST_tree==None:
        return False
    elif(D<BST_tree.cargo):
        return searchBST(D,BST_tree.left)
    elif(D>BST_tree.cargo):
        return searchBST(D,BST_tree.right)
    else:
        return True
```

## Tipos de recorrido

### Pre Order
1. Raiz
2. Izquierda
3. Derecha
```
def preorder(tree):
    if tree == None:
        return
    print(tree.cargo)
    print (preorder(tree.left))
    print (preorder(tree.right))

```
### In Order
1. Izquierda
2. Raiz
3. Derecha
```
def inorder(tree):
    if tree == None:
        return
    print (preorder(tree.left))
    print(tree.cargo)
    print (preorder(tree.right))
```

### Post Order
1. Izquierda
2. Derecha
3. Raiz
```
def postorder(tree):
    if tree == None:
        return
    print (preorder(tree.left))
    print (preorder(tree.right))
    print(tree.cargo)
```
