# Estructura de datos

Es un conjunto de datos agrupados bajo un nombre:
## Listas
### Agrupacion de datos combinando distintos tipos de dato, son mutables ya que se puede agregar borrar y modificar los datos.
````
alumno = [7, 'Jose', 24, 2022]

alumno[1]
'Jose'

alumno[-1]
2022

alumno[0] = 9

alumno
[9, 'Jose', 24, 2022]
````
### APEND
lista.append()
### INSERT
lista.insert(Posicion, valor que quiero agregar)
Agrega un elemento a la lista, ingresandole la posicion y luego el valor
### REMOVE
lista.remove(Posicion del elemento que quiero eliminar por valor)
### POP
lista.pop(posicion del elemento que queremos elminar por indice, si esta vacio borra toda la lista)
### INDEX
lista.index(elemento que queremos saber el numero de index)
### SORT
lista.sort()
Ordena los elementos



## Tuplas
### Son listas pero no son modificables, son inmutables
````
tupla1 = (1, 'hola', 22, 34)
tupla2 = (1, 'Chau', (1,2))
````

````
tupla1.index((1,2)) #IGUAL QUE EN LISTAS
2

tupla.count(elemento que queremos saber cuantas veces aparece en la tupla)
````
