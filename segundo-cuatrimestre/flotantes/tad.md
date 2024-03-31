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

