# Programacion II

- Primer parcial Jueves 12/10
- Segundo parcial Jueves 23/11
- Primer TP Lunes 16/10
- Segundo TP Jueves 07/12
- RECUPERATORIOS LAS PRIMERAS SEMANAS DE DICIEMBRE

### LUNES CLASES DE PRACTICA
### JUEVES CLASES DE TEORIA

### Repaso de funciones
```
Una funcion es un fragmento de codigo que permite efectuar una operacion determinada, por ejemplo, abs, min, max y len que son built in o incluidas en python.
parametros(0 o más)
---->                 ---->
---->       ACCIONES  ---->     RESULTADO
---->                 ---->
```
Se pueden definir funciones:
```
def nombre_funcion(argumentos):
    codigo
    return retorno
```
## IMPORTANTE: UNA FUNCION ES MAS REUTILIZABLE SI UTILIZAMOS RETURN EN VEZ DE PRINT

## Recursion
#### 2 Secciones claramente divididas
```
1. Condicion de la funcion en que retorna sin volver a llamarse. Es para que no se llame de manera indefinida. Se le llama caso base de recursion.

2. La funcion se llama asi misma con variacion en sus argumentos. Se le llama caso recursivo de la recursion.
```

#### EJEMPLO DE UNA FUNCION RECURSIVA MATEMATICA
0! = 1 x! = x(x-1)!, si x > 0
```
def factorial(n: int) -> int:
    """
    Precondicion: n entero >= 0
    devuelve: n!
    """
    if n == 0
        return 1
    return n * factorial(n - 1)
```
### La ejecucion se veria asi:
```
>>> factorial(0)
1
>>> factorial(3)
6
```
#### MISMO EJEMPLO PERO CON ITERACION
```
def factorial(n: int) -> int:
    """
    Precondicion: n entero >= 0
    devuelve: n!
    """
    fact = 1
    for num in range(n,1,-1):
        fact *= num
    return fact
```

```
Antes de programar una funcion recursiva hay que tener en cuenta:
- El caso base: tomamos el valor 0
- El caso recursivo: tenemos 2 partes n para par y n para impar
b**0=1
b**n= b**n/2 * b**n/2 si n es par
b**n= b**((n-1)/2) * b**((n-1)/2) * b si n es impar
```
#### En python:
```
def potencia(b:int, n:int)->int:
    """
    Precondicion: n entero >= 0
    devuelve: b**n
    """
    if n == 0:
        return 1
    if n%2 == 0:
        p = potencia(b,n//2)
        return p * p
    else:
        p = potencia(b, (n-1)//2)
        return p * p * b
```
### TEST DE LA FUNCION POTENCIA
```
n=10 -> 1 mmult(p*p)
>>> n es par
n=5 -> 2 mmult(p*p*b)
>>> n es impar
n=2 -> 1 mmult(p*p)
>>> n es par
n=1 -> 2 mmult(p*p*b)
>>> n es impar
n=0
Retorna 1
```

#### FIBONACCI

```
def fib(n:int)->int:
    """
    Precondicion: n entero >= 0
    devuelve: El numero de fibonacci numero n
    """
    if n==0 or n==1:
        return n
    return fib(n-1), fib(n-2)
```

```
def fib(n:int)->int:
    """
    Precondicion: n entero >= 0
    devuelve: El numero de fibonacci numero n
    """
    if n==0 or n==1:
        return n
    ant2=0
    ant1=1
    for i in range(2, n+1):
        fibn = ant1 + ant2
        ant2=ant1
        ant1=fibn
    return fibn
```

## UN ALGORITMO RECURSIVO NO ES MEJOR QUE UNO INTERATIVO, NI VICEVERSA. HAY QUE VER EN QUE SITUACION ES MAS CONVENIENTE.

## COMO DISEÑAR UNA FUNCION RECURSIVA:
```
'''
ESCRIBIR UNA FUNCION RECURSIVA QUE SUME LOS ELEMENTOS DE UNA LISTA
DE NUMEROS ENTEROS EN PYTHON
'''
def sumar(lista: list[int])->int:
    if len(lista)==0:
        return 0
    return lista[0] + sumar(lista[1:])
```
#### ERRORES COMUNES EN FUNCIONES RECURSIVAS
- No escribir un caso base para la recursion
- No asegurarse de que el caso recursivo converja a un caso base.

## CONCLUSIONES
- La recursion es el proceso por el cual una funcion se invoca asi misma. Permite crear un nuevo tipo de ciclos
- Siempre que se escribe una funcion recursiva es importante el caso base y el caso recursivo, un caso recursivo sin el caso base es equivalente a un bucle infinito
- Una funcion no es mejor ni peor por ser recursiva.