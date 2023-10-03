# ABSTRACCION


```
TAD: Tipo abstracto de dato
Ciclo de vida de un tad:
1. La programacion del TAD: Se elige una representacion y un programa

2. La construccion de los programas que lo usan osea los metodos que posee
```
### Una interfaz o protocolo, es un medio comun para que los objetos no relacionados se comuniquen entre si

El TAD Lista es un conjunto de valores ordenados y numerables con las siguientes operaciones: Las listas de python son
una implementacion del TAD Lista.

```
__str__
__len__
append(x)
insert(i,x)
remove(x)
pop(x)
index(x)
```

## ARREGLOS Y PERFORMANCE
Las representacion interna de las listas nativas de python ustiliza una estructura de datos llamada arreglo. Un arreglo
es la forma mas facil de almacenar una secuenta de datos en la memoria.

```
class Nodo:
    def __init__(self, dato: Any=None, prox: 'Nodo' | None=None)
        self.dato=dato
        self.prox=prox
    def __str__(self):
        return(self.dato)
```

>>> n3=Nodo('Bananas')

>>>n2=Nodo('Peras', n3)

>>>n1=Nodo('Manzanas', n2)

>>>str(n1)

'Manzanas'

>>>str(n2)

'Peras'

>>>str(n3)

'Bananas'
```
def ver_lista(nodo: Nodo | None) -> None:
    """Recorre todos los nodosatrav´esdesus enlaces, mostrando sus contenidos."""
    while nodo is not None:
    print(nodo)
    nodo=nodo.prox
```

# CONVENCION SI USAMOS UN _MiClase ES SOLO PARA QUE SE UTILICE POR AFUERA

```
class ListaEnlazada:
    '''
    Modela una lista enlazada
    '''
    def __init(self)->None:
        self.Prim=None
        self.len=0
```
# Metodo INSERT
```
def insert(self,i:int,x:Any)->None:
    '''
    Inserta el elementoxenla posici´oni. Sila posici´onesinv´alida,imprime un error y retorna inmediatamente
    '''
    if i<0 or i>self.len:
        print('Posicion invalida')
        return
    nuevo=_Nodo(x)
    if i==0:
        #Insertamos al principio
        nuevo.prox=self.prim
        self.prim=nuevo
    else:
        #Busca el nodo anterior en la posicion deseada
        n_ant=self.prim
        for pos in range(1,i):
            n_ant=n_ant.prox
            nuevo.prox=n_ant.prox
            n_ant.prox=nuevo
            #Intercala el nuevo nodo
            nuevo.prox=n_ant.prox
            n_ant.prox=nuevo
    self.len+=1
```
# Metodo POP
```
def pop(self, i:int | None=None)->Any:
    '''
    Elimina nodo de la posicion i, y devuelve el dato contenido. Si i fuera de rango, muestra un mensaje de error y termina. Sino se recibe la posicion,devuelve el ultimo elemento
    '''
    if i is None:
        i=self.len-1
    if i<0 or i>=self.len:
        print('Posicion invalida')
        return
    if i==0:
        dato=self.prim.dato
        self.prim=self.prim.prox
    else:
        n_ant=self.prim
        n_act=n_ant.prox
        for pos in range(1,i):
            n_ant=self.prim
            n_act=n_ant.prox
        dato=n_act.dato
        n_ant.prox=n_act.prox
    self.len-=1
    return dato
```
# Metodo REMOVE
```
def remove(self,x:Any)->None:
    '''
    Borrala primera aparici´ondel valorxen lalista.Sixnoest´aenlalista,imprime un mensaje deerroryretorna inmediatamente
    '''
    if self.len==0:
        print('La lista esta vacia')
        return
    if self.prim.dato==x:
        #Saltea la cabecera de la lista
        self.prim=self.prim.prox
    else:
        #Busca el nodo anterior al que contiene x osea (n_ant)
        n_ant=self.prim
        n_act=n_ant.prox
        while n_act is not None and n_act.dato !=x:
            n_ant=n_act
            n_act=n_ant.prox
        if n_act==None:
            print('El valor no esta en la lista')
            return
        n_ant.prox=n_ant.prox
        self.len-=1
```
# INVARIANTES DEL OBJETO

- Son condiciones que deben ser siempre ciertas.

- Son condiciones que deben ser ciertas a lo largo de toda la existencia de un objeto

La clase ListaEnlazada presentada en la seccion anterior cuenta con 2 invariantes que siempre debemos mantener:

  1. El atributo len que debe contener la cantidad de nodos de la lista
  2. El atributo prim referencia siempre al primer nodo de la lista