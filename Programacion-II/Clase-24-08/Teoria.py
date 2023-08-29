"""
ESCRIBIR UNA FUNCION RECURSIVA QUE SUME LOS ELEMENTOS DE UNA LISTA DE NUMEROS ENTEROS EN PYTHON
"""


def sumar(lista: list[int]) -> int:
    if len(lista) == 0:
        return 0
    return lista[0] + sumar(lista[1:])


lista = [3, 4, 5, 10, 7]
print(sumar(lista))

"""
Ejercicio 1

1. Escribir una función recursiva `repite_hola` que reciba como parámetro
un número entero $n$ y escriba por pantalla el mensaje "Hola" $n$ veces. Invocarla con distintos valores de $n$.

2. Escribir otra función `repite_hola` que reciba como parámetro un
número entero $n$ y devuelva la cadena formada por $n$ concatenaciones de "Hola". Invocarla con distintos valores de $n$
"""


def multiples_hola(num: int) -> str:
    """
    Esta funcion recibe un numero entero como parametro y devuelve el mensaje hola N veces
    """
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            print("Hola")


multiples_hola(2)


def concatenar_hola(num: int) -> str:
    """
    Esta funcion recibe un numero entero como parametro y devuelve el mensaje hola N veces concatenado
    """
    cadena = ""
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            cadena = cadena + "hola "
    return cadena


saludo = concatenar_hola(3)
print(saludo)

"""
Ejercicio 2 1. Piense cuál sería el resultado de la expresión `misterio(5)` y luego compruebe su hipótesis ejecutándola.

2. Explique con sus palabras qué hace `misterio(a)` para
cualquier `a`, sea positivo, negativo o 0.
"""


# va a imprimir 5
def misterio(a: int) -> int:
    if a == 0:
        return a

    return 1 + misterio(a - 1)


mistery = misterio(5)
print(mistery)

"""
Ejercicio 3 RECURSION 1. Escribir una función `repite_saludo` que reciba como parámetro un número entero $n$ y una
cadena saludo y escriba por pantalla el valor de saludo $n$ veces. Invocarla con distintos valores de $n$ y de saludo.

2. Escribir otra función `repite_saludo` que reciba como parámetro un número entero $n$ y una cadena saludo devuelva el
   valor de $n$ concatenaciones de saludo. Invocarla con distintos valores de $n$ y de saludo.
"""


# 3.1
def repite_saludo(num: int, saludo: str) -> str:
    """
    Esta funcion recibe un numero entero y una cadena como parametro y devuelve el mensaje N veces
    """
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            print(saludo)


# 3.2
def repite_saludo(num: int, saludo: str) -> str:
    """
    Esta funcion recibe un numero entero y una cadena como parametro y devuelve el mensaje N veces concatenado
    """
    cadena = ""
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            cadena = cadena + saludo
    return cadena

saludo = repite_saludo(3, "hola ")
print(saludo)

#CLASE 28/08

"""
Ejercicio 4 Escriba una funcion recursiva que tome un numero natural n e imprima todos los numeros desde n hasta 1.
"""


def funcion_recursiva(num:int) -> int:
    """
    Esta funcion recien un numero natural y devuelve todos los numeros desde n hasta 1
    """
    if num == 0:
        return 0
    else:
        print(num)
        return funcion_recursiva(num - 1)

funcion_recursiva(5)

"""
Ejercicio 5 Convierta la siguiente función recursiva a una iterativa.

def recursiva(t: int, k: int) -> int:
  if t >= 100:
    return k
  else:
    return recursiva(t + k, k + 1)
"""


def iterativa(t: int, k: int) -> int:
    while t < 100:
        t = t + k
        k = k + 1
    return k


valor = iterativa(1, 2)
print(valor)

'''
Ejercicio 6 Escribir una funcion recursiva que calcule revurivamente el n-esimo numero triangular(el numero 1+2+3+...+n)
'''
def funcion_recursiva(num:int) -> int:
    """
    Esta funcion recibe un numero natural y devuelve el numero triangular
    """
    if num == 0:
        return 0
    else:
        return num + funcion_recursiva(num - 1)

print(funcion_recursiva(5))

'''
Ejercicio 7 escribir una funcion recursiva que reciba un numero positivo n y devuelva la cantidad de digitos que tiene
'''
def cantidad_digitos(num:int) -> int:
    """
    Esta funcion recibe un numero natural y devuelve la cantidad de digitos que tiene
    """
    if num == 0:
        return 0
    else:
        return 1 + cantidad_digitos(num // 10)

cantidad_diti = cantidad_digitos(1234)
print(cantidad_diti)

'''
Ejercicio 8 Convierta la sigueinte funcion iterativa a una recursiva: def iterativa(l: list[int]) -> int:
  c = 1 for i in l:
    c = c * i
  return c
'''
def funcion_it_recursiva(l: list[int]) -> int:
    """
    Esta funcion recibe una lista de numeros enteros y devuelve el producto de todos los elementos
    """
    if len(l) == 0:
        return 1
    else:
        return l[0] * funcion_it_recursiva(l[1:])

lista = [1, 2, 3, 4, 5]
producto = funcion_it_recursiva(lista)
print(producto)

'''
Ejercicio 9 Escribir una funcion recursiva que encuentre el mayor elemento de una lista.
'''

def maximo_recursivo(l: list[int]) -> int:
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], maximo_recursivo(l[1:]))#UNA ALTERNATIVA ES USAR max(l.pop(),maximo_resursivo(l))

lista = [1, 2, 3, 4, 5, 6]
maximo = maximo_recursivo(lista)
print(maximo)

'''

'''