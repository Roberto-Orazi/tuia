# Arboles

Los arboles son estructuras jerarquicas que se usan para modelar una variedad de problemas y situaciones.

## Definicion formal de arbol

Un arbol T es un conjunto de puntos a los que llamamos vertices y pueden estar unidos por lineas(ARISTAS) si V y W son vertices en T entonces existe un unico camino desde V a W.

Un arbol con raiz es un arbol en el que un vertice especifico se designa como raiz.

## Arbol Binario
Son los mas importantes de los arboles especiales de arboles con raiz.
Todo arbol binario tiene a lo sumo 2 hijos.
Cada hijo se designa como un hijo izquierdo o derecho.


## Definicion formal de arbol binario
Un arbol binario es un arbol con raiz en el que cada vertice puede tener ningun, uno o dos hijos. Si tiene uno tiene o un izquierdo o un derecho, y si tiene 2 tiene uno izquierdo y uno derecho
Un arbol binario completo es un arbol binario en el que cada vertice tiene dos o cero hijos

Un arbol binario es:
   - El arbol vacio o representado por none
   - Un nodo que contiene una referencia del objeto y dos referencias a arboles binarios

La implementacion es:
```
class BinaryTree:
    def __init__(self, cargo, left=None, Right=None):
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.cargo)
```

## Arbol binario de busqueda
