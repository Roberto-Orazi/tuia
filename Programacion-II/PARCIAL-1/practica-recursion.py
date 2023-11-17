# Ejercicio 1 a
def repite_hola(n):
    if n == 0:
        return 1
    else:
        print("Hola")

    return(repite_hola(n-1))

repite_hola(2)

# Ejercicio 1 b
def multiple_hola(n: int) -> str:
    concat = ''
    if n == 0:
        return ''
    else:
        concat = concat + "Hola "

    return concat + multiple_hola(n - 1)

print(multiple_hola(4))

# Ejercicio 2
'''
Retorna siempre el a
'''

# Ejercicio 3 a
def repite_saludo(n:int, saludo:str)->str:
    if n==0:
        return ''
    else:
        print(saludo)
    return saludo + repite_saludo(n-1, saludo)

repite_saludo(3, "saludis ")

# Ejercicio 3 b
def repite_saludos(n:int, saludo:str)->str:
    if n==0:
        return ''
    return saludo + repite_saludos(n-1, saludo)

print(repite_saludos(3, "saludos "))

# Ejercicio 4
def naturales(n:int)->int:
    if n==0:
        return 0
    else:
        print(n)
    return(naturales(n-1))
naturales(5)

# Ejercicio 5
def interativa(t: int, k: int)->int:
    while t<100:
            t=t+k
            k=k+1
    return(k)
print(interativa(20,1))

def recursiva(t: int, k: int) -> int:
  if t >= 100:
    return k
  else:
    return recursiva(t + k, k + 1)

print(recursiva(20,1))

# Ejercicio 6
def suma_recursiva(n:int)->int:
    suma=0
    if n==0:
        return 0
    else:
        return n + suma_recursiva(n-1)

print(suma_recursiva(2))

# Ejercicio 7
def cantidad_digitos(n: int)-> int:
    if (n//10) == 0:
        return 1
    else:
        return(1 + cantidad_digitos(n//10))

print(cantidad_digitos(22))

# Ejercicio 8
def recursiva_8(lista: list[int]) -> int:
    c=2
    if len(lista) == 0:
        return 1
    else:
        c=c*lista.pop() * recursiva_8(lista)

    return c

print(recursiva_8([2, 3, 5]))

#Ejercicio 9 def mayor
