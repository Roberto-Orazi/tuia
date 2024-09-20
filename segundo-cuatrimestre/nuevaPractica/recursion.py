# Ejercicio 0
def factorial(n: int) -> int:
    if n == 0:
        return 1

    return factorial(n - 1) * n


factorial(4)


# Ejercicio 1.1
def repite_hola(n: int) -> str:
    if n == 0:
        return ""

    print("hola")
    return repite_hola(n - 1)


repite_hola(4)


# Ejercicio 1.2
def concatena_hola(n: int) -> str:
    if n == 0:
        return ""

    return "hola " + concatena_hola(n - 1)


concatena_hola(5)


# Ejercicio 2.1
def repite_saludo(n: int, cadena: str) -> str:
    if n == 0:
        return ""

    print(cadena)
    return repite_saludo(n - 1, cadena)


repite_saludo(5, "chau")


# Ejercicio 2.1
def concatena_saludo(n: int, cadena: str) -> str:
    if n == 0:
        return ""

    return cadena + concatena_saludo(n - 1, cadena)


concatena_saludo(5, "chau ")

# Ejercicio 3
"""
El resultado de misterio 5 va a ser siempre a, ya que estamos sumando 1 cada vez que le restamos 1, por ende vamos a
sumar 1 por cada llamada
"""


def misterio(a: int) -> int:
    if a == 0:
        return a

    return 1 + misterio(a - 1)


misterio(5)


# Ejercicio 4
def f(n: int, d: int) -> None:
    if n > 1:
        if n % d == 0:
            print(d)
            f(n // d, d)
        else:
            f(n, d + 1)


f(30, 2)
# Ejercicio 4.1-4.2
"""
f(30,2) imprime 2,3,5

La funcion muestra los divisores primos de la funcion
"""


# Ejercicio 4.3
def f_iterativa(n: int, d: int) -> int:
    while n > 1:
        if n % d == 0:
            print(d)
            n = n // d
        else:
            d += 1


f_iterativa(30, 2)


# Ejercicio 5
def mystery(a: int, b: int) -> int:
    if b == 0:
        return a
    return mystery(2 * a, b - 1)


result = mystery(7, 3)
print(result)

"""
Esto va a devolver x*(2^y)

Devuelve 56 la funcion mystery(7,3)

Se llama 3 veces la funcion

Primera llamada: mystery(7, 3), que llama a mystery(14, 2)

Segunda llamada: mystery(14, 2), que llama a mystery(28, 1)

Tercera llamada: mystery(28, 1), que llama a mystery(56, 0)

Cuarta llamada: mystery(56, 0), que retorna 56
"""


# Ejercicio 6
def imprimir_natural(n: int) -> int:
    if n == 0:
        return 0
    imprimir_natural(n - 1)
    print(n)


imprimir_natural(5)


# Ejercicio 7
def recursiva(t: int, k: int) -> int:
    if t >= 100:
        return k
    else:
        return recursiva(t + k, k + 1)


recursiva(10, 20)


def iterativa(t: int, k: int) -> int:
    while t < 100:
        t += k
        k += 1
    return k


iterativa(10, 20)


# Ejercicio 8
def n_esimo(n: int) -> int:
    if n == 0:
        return 0
    return n + n_esimo(n - 1)


n_esimo(5)


# Ejercicio 9
def cantidad_digitos(n: int) -> int:
    if n // 10 == 0:
        return 1
    return 1 + cantidad_digitos(n // 10)


cantidad_digitos(1)


# Ejercicio 10
def es_potencia(n: int, b: int) -> int:
    if n < 1:
        return False
    if n // b == 1:
        return True
    if n % b != 0:
        return False
    return es_potencia(n // b, b)


print(es_potencia(8, 2))
print(es_potencia(64, 4))
print(es_potencia(70, 10))


# Ejercicio 11
def mayor_elemento(lista: list[int], max: int = 0) -> int:
    if not lista:
        return max
    if lista[0] > max:
        max = lista[0]
    return mayor_elemento(lista[1:], max)


mayor_elemento([1, 2, 3, 3, 5, 6, 1, 2, 3, 2, 2])


# Ejercicio 12
def iterativa12(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c


iterativa12([1, 2, 3, 4])


def recursiva12(l: list[int], c: int = 0, valor: int = 1) -> int:
    if not l:
        return valor
    c += 1
    valor *= c
    return recursiva12(l[1:], c, valor)


recursiva12([1, 2, 3, 4])

# Ejercicio 13
