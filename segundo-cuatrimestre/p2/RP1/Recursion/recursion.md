### Recursion
```
Es una tecnica para programar que usa algoritmos, procedimientos, subrutinas, funciones que se llaman asi mismo hasta llegar a la condicion de finalizacion
```

###  Funcion Recursiva
```
La recursion es una funcion que se llama a si mismo, las funciones recursivas tiene 2 partes:
1. Caso base que es cuando termina la funcion y retorna los valores
2. El caso recursivo que es cuando se llama a si misma.
```

### Scopes de variables
```
Las variables tienen un alcance, si nosotros las declaramos adentro de una funcion y no las retornamos, la vida util de esa variable existe solo cuando se lama a la funcion.
```

### Imprimir vs Retornar
```
- Si imprimimos un resultado con el print, no lo podemos reutilizar ni usar para otras operaciones
- Si devolvemos un resultado con el return lo hacemos reutilizable, ya que podemos usar ese valor para sumar 2 numeros por ejemplo
```
### Pasos para hacer una funcion recursiva
```
1. Encotrar un caso base, tiene que ser algo sencillo de calcular y a veces hasta ni eso. (HAY QUE ASEGURARSE QUE TENGAMOS SIEMPRE UN CASO BASE)

2. Hay que idear como con la llamada recursiva a la funcion podemos reducir la lista hasta que llegue a 0 elementos. (HAY QUE ASEGURARSE QUE SIEMPRE LLEGUE A 0 ELEMENTOS O A NUESTRA CONDICION PARA QUE VAYA AL CASO BASE)
```

# PREGUNTAS
Que es la recursion?

La recursion es una funcion que se llama a si misma, estas tienen 2 partes, el caso base y el caso recursivo.


Algoritmos recursivos vs iterativos
Los algoritmos recursivos son los que llegan al resultado realizando llamadas recursivas.

Los algoritmos iterativos llegan al resultado iterando un cilcio definido o indefinido de veces.

ejemplo de Recursion eficiente
La funcion potencia es eficiente hacerla recursivamente ya que en la funcion recursiva se multiplica menos veces que en la iterativa.

ejemplo de Recursion ineficiente
Fibonacci es poco eficiente ya que para calcular fib(n-1) hay que calcular tambien fib(n-2) para luego volver a calcularlo para obtener f(n), mientras que iterando solo haremos n-1 iteraciones.


- como esta formado un algoritmo recursivo y cuales son los errores comunes?

1. El caso base es el que termina la funcion y retorna los valores(el que detiene la recursion)
Una funcion sin caso base nos lleva a un bucle infinito.

2. El caso recursivo es el que se vuelve a llamar a la funcion hasta que llega al caso base. Hay que asegurarse que siempre termine en un caso base.

Errores comunes:
- No escribir un caso base para la recursion
- No asegurarse que el caso recursivo converja en el caso base

Caso base: es la condicion en la cual la funcion retorna sin volver a llamarse.

Caso recursivo: Es la parte en la que la funcion se llama a si mismo, con una variacion de los argumentos.
