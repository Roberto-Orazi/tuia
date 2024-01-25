# Recursión

## Que es la recursión?
La recursion en pocas palabras es cuando una funcion se llama a si misma.

#### Print Vs Return
Print
```
def imprimir_segundos( horas:int,minutos:int,segundos:int )->None:
    """
        Transforma en segundos una medida
        de tiempo expresada horas,minutosysegundos
    """
    print( 3600*horas +60*minutos +segundos )
```
Return
```
def devolver_segundos( horas:int,minutos:int,segundos:int )->int:
    """
        Transforma en segundos una medida de tiempo
        expresada horas,minutosysegundos
    """
    return( 3600*horas +60*minutos +segundos )
```
La diferencia entre las 2 es que con imprimir segundos
no podemos hacer operaciones con los valores, por ejemplo:
>>>s1=devolver_segundos(1,10,10)
>>>s2=devolver_segundos(2,32,20)
>>>s1+s2
13350
con el imprimir segundos no podemos.

```
Una funcion es mas reutilizable is devuelve un resultado, utilizando un return.
En vez de imprimirlo usando el print.
Es mas reutilizable si recibe parametros que leyendo datos mediante inputs.
```
### Tenemos 2 tipos de recursion:
1. Caso Base:
Existe una condicion que la funcion retorna sin volver a llamarse sino queda en bucle infinito.
2. Caso Recursivo:
Se llama la funcion a si misma con alguna variacion en sus argumentos.

## Algoritmos Recursivos e Iterativos
- Algoritmos Recursivos
Son aquellos que realizan llamadas recursivas para llegar al resultado.
- Algoritmos Iterativos
Son quellos que llegan al resultado atraves de una iteracion.

Todo algoritmo recursivo puede expresarse como iterativo y viceversa.
Segun el problema a resolver vemos cual de los 2 usamos.

## Iteracion Vs Recursion

RECORDAR QUE RECURSIVO NO ES MEJOR QUE ITERATIVO NI VICEVERSA.
DEPENDE EL PROBLEMA.

### Diseño de funciones recursivas.
1. Encontrar el caso base, debe ser sencillo de calcular
   y muchas veces no hace falta calcular nada. Si la lista
   es vacia es obvio que la suma de elementos es 0.
2. Tenemos que pensar como reducir una lista no vacia para
   que llegue a tener 0 elementos.

### Errores mas comunes
1. No escribir un caso base para la recursión
2. No asegurarse de que el caso recursivo no llegue a un caso base

Cualquier cosa el interprete nos va a tirar error de maximum recursion depth exceeded

## Conclusion
- La recursión es el proceso por el cual la funcion se invoca a si misma. y permite crear nuevo tipos de ciclos.
- Para escribir una funcion recursiva siempre hay que considerar el caso base(Detiene la recursion) y
  el caso recursivo que es el que realiza la llamada recursiva. Si no tiene caso base es bucle infitnito
- Una funcion no es mejor ni peor por ser recursiva.