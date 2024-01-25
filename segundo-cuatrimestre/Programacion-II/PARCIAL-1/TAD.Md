# Tipo Abstracto de Datos
Los tipos de datos definidos en POO son tipos de datos concretos, por ej: Point, Rectangulo.

Otra forma de definir tipos de datos es mediante sus operaciones:
- Enumerandolas e indicando su comportamiento.
Osea decir cual es su resultado esperado.

Esta manera de definir datos se le llama tipos abastractos de datos o TADs

## Que es tad?

- Una coleccion de datos.
- Los datos estan acompañados por un conjunto de operaciones para manipularlos.

## Porque son utiles?
Los programas que los usan hacen referencia a las operaciones que tienen y no a la representacion, por lo tanto si se cambia la representacion, el programa sigue funcionando.

## Ciclo de vida de un TAD

La programacion del Tad:
  - Se elige una representacion
  - Se programan los metodos sobre esa representacion

La construccion de los programas que lo usan:
  - En esta fase no es relevante como esta implementado el tad sino los metodos que posee.

- En POO, una interfaz o protocolo es un medio comun para que los objetos no relacionados se comuniquen entre si.

- Estas son definiciones de metodos y valores, en los cuales los objetos estan de acuerdo para cooperar.

- A quien utilice el TAD solo le interesa la interfaz que ofrece.

## TAD Lista

Representa un conjunto de valores ordenados y numerables con los siguientes metodos:
   - __str__ obtener representacion de lista como string
   - __len__ calcular longitud
   - append(x) agrega elemento final de la lista
   - insert(i,x) agrega elemento x en pos i
   - remove(x) elimina la primera aparicion de x, si no hay tira error
   - pop(i) elimina elemento en pos i y devuelve su valor
   - index(x) devuelve posicion de la primera aparicion de x, si no hay tira error

### Listas Nativas
Las listas en python son una implementacion del TAD Lista.
Esto significa que el tipo list en python se pueden implementar los metodos mencionados.

#### Arreglos y Performance
- La Representacion interna de las listas nativas de python utiiza una estructura de datos llamada arreglo.
- Un arreglo es una forma mas simple de almacenar una secuencia de datos en la memoria, los elementos estan contiguos.
- Facilidad para acceder a un elemento mediante la posicion i, lo podemos hacer con lista[i], es de tiempo constante por lo tanto no depende del largo del arreglo.
- Agregar o quitar elementos en una posicion dada del arreglo si es de tiempo lineal ya que va a tardar mas o menos dependendo del largo y la posicion que querramos modificar.


### Lista Enlazada
Una lista enlaza esta formada por nodos, y cada nodo tiene un elemento y una referencia a otro nodo, como vagones de tren.

Ventaja
   - Eliminar el primer elemento es una operacion de tiempo constante
Desventaja:
   - El acceso a la posicion i es un tiempo proporcional a i

#### Clase lista Enlazada
Se define la clase ListaEnlazada para que no haya que operar mediante las referencias internas de los nodos, sino que se haga atraves de operaciones de lista.

Consideraciones:
- La lista tiene que tener como atributo la referencia del primer nodo
- Si implementamos el metodo __len__ tendriamos que recorrer todos los nodos y contar la cantidad de elementos. Para mejorar la eficiencia se agrega un atributo numerico que vaya sumando los nodos a medida que los vamos agregando.
- Para hacer nodos privados al nombre le ponemos un _ adelante y quedaria _Nodo

#### Invariantes de objeto
Las invariantes son condiciones que deben ser siempre ciertas.
Entonces Las invariantes de objeto, son condiciones que deben ser ciertas a lo largo de toda la existencia de un objeto.

Por ejemplo:
ListaEnlazada presenta 2 invariantes:
1. atributo len(Debe contenter siempre la misma cantidad de nodos de la lista)
2. atributo prim(referencia al primer nodo)

## Arreglo Vs Lista Enlazada
### Arreglo
- Barato para buscar elementos por posicion
- Barato agregar o elminar al final
- Caro agregar o eliminar al principio o medio

### Lista Enlazada
- Caro para buscar elementos por posicion
- Barato agregar al principio
- Barato agregar o eliminar al principio o en medio ya que no hay que mover nada en memoria solo actualizar referencias.
