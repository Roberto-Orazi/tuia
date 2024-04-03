## Tipos abstractos de datos

Dentro del ciclo de vida del tad hay 2 fases:
- La programacion del tad.
Hay que elegir una representacion y programar cada uno de los metodos sobre esa representacion


Se diseña una estructura de datos para acceder a los datos y manipularlos eficientemente.

En la estructura de datos se define la coleccion de valores que se almacenan, como estan agrupados y como se relacionan.


- La construccion de los programas que lo usan.
En esta fase no es relevante para el programador como este implementado el tad, solo los metodos que posee. En poo una interfaz(protocolo) es un medio comun para que los objetos no relacionados se comuniquen entre si.


## Tad lista
El tad lista representa un conjunto de valores ordenados y numerables, tienen las siguientes operaciones:
(Las x suelen ser valores/elementos y i posiciones o indices)
- __str__ Obtener representacion de una lista como string
- __len__ Longitud lista
- append(x) Agrega un elemento X al final de la lista
- insert(i,x) Agrega un elemento X en la posicion I
- remove(x) Elimina la primera aparicion del elemento X de la lista si no existe tira error
- pop(i) Elimina el elemento de la posicion i y devuelve su valor. Si usamos pop() elimina y devuelve el ultimo elemento de la lista.
- index(x) Devuelve la posicion del elemento X

## Lista enlazada
La lista enlazada esta formada por nodos, donde cada nodo guarda un elemento y una referencia a otro nodo, como si fueran vagones en un tren.

Primero tenemos que definir la clase nodo que tiene solo 2 atributos, dato, para almacenar el elemento y proximo que es la referencia al proximo nodo.

```
from typing import Any

class Nodo:
    def __init___(self, dato: Any = None, prox: 'Nodo' | None = None):
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return str(self.dato)
```

Para recorrer los nodos podemos usar:

def ver_lista(nodo: Nodo | None) -> None:
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox

La clase lista enlazada tiene los mismos metodos que la lista:
- __str__
- __len__
- append(x)
- insert(i,x)
- remove(x)
- pop(i)
- index(x)

## Construccion de lista enlazada

```
class ListaEnlazada:

    def __init__(self)->None:
    self.prim=None
    self.len=0

    def __len__(self):
        return self.len

    def __str__(self):
        current=self.prim
        lista_str = ''

        while current:
            lista_str+=str(current.dato) + '->'
            current=current.prox

        lista_str+= 'None'
        return str(lista_str)

    def insert(self,i,x):
        if i < 0 or i > self.len:
            print('Posicion invalida')
            return

        nuevo = _Nodo(x)

        if i == 0:
            nuevo.prox = self.prim.prox
            # DUDA SOBRE ESTO LE ASIGNO EL VALOR DE SELF.PRIM.PROX QUE SERIA EL PROXIMO AL SELF.PRIM
            self.prim=nuevo

        else:
            n_ant=self.prim
            for pos in range(1,i):
            # ACA VAMOS A ITERAR HASTA LA POSICION ANTERIOR A LA DESEADA ASI LE ASIGNAMOS LA POSICION AL PROX QUE SERIA NUESTRO NUEVO NODO
                n_ant = n_ant.prox

            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len+=1

    def pop(self, i):
        if i is None:
            i = self.len - 1

        if i < 0 or i > self.len:
            print('posicion invalida')
            return

        if i == 0:
            dato=self.prim.dato
            self.prim=self.prim.prox
        else:
            n_ant=self.prim
            n_act=n_ant.prox
            for pos in range(1,i):
                n_ant=n_act
                n_act=n_ant.prox
            dato=n_act.dato
            n_ant.prox=n_act.prox
        self.len-=1
        return dato

    def remove(self,x):
    
```

