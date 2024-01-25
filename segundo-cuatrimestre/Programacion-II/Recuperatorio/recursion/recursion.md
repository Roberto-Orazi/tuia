# Recursion

## Imprimir vs Devolver
La principal diferencia es la reutilizacion en el caso del return.
Si usamos print tampoco podemos hacer operaciones entre resultados.

## Scopes de variables
Si declaramos variables dentro de una funcion o un bloque de codigo se le llaman variables locales
Fuera de una funcion, son variables globales.

## Definicion de Recursion
En pocas palabras es una tecnica de programacion en la cual un algoritmo, funciones, subrutinas se llama a si mismo hasta que llega a la condicion de finalizacion(caso base)

## Funcion recursiva
Una funcion recursiva es cualqueir funcion que se llame a si misma.

Tienen que tener:
1. Caso base:
    - Es cuando la funcion retorna sin volver a llamarse.
    - Sin caso base queda en bucle infinito
2. Caso recursivo:
    - Es la parte de la funcion que se llama a si misma con alguna variacion en sus argumentos.

## Algoritmos recursivos y iterativos
- Los algoritmos recursivos son losq ue hacen las llamadas recursivas para llegar al resultado.
- Los iterativos son los que llegan mediante una iteracion mediante un ciclo definido o indefinido.

## Errores comunes
1. No escribir el caso base
2. No asegurarse que el caso recursivo termine en un caso base

## Por si no te acordas de nada
1. La recursion es el proceso de cuando la funcion se invoca asi misma.
2. Siempre acordate del caso base. Y del caso recursivo.
3. La funcion no es ni mejor ni peor por ser recursiva. Siempre depende.

