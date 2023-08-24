'''
ESCRIBIR UNA FUNCION RECURSIVA QUE SUME LOS ELEMENTOS DE UNA LISTA DE NUMEROS ENTEROS EN PYTHON
'''
def sumar(lista: list[int])->int:
    if len(lista)==0:
        return 0
    return lista[0] + sumar(lista[1:])

lista=[3,4,5,10,7]
print(sumar(lista))

'''
Ejercicio 1

1. Escribir una función recursiva `repite_hola` que reciba como parámetro
un número entero $n$ y escriba por pantalla el mensaje "Hola" $n$ veces. Invocarla con distintos valores de $n$.

2. Escribir otra función `repite_hola` que reciba como parámetro un
número entero $n$ y devuelva la cadena formada por $n$ concatenaciones de "Hola". Invocarla con distintos valores de $n$
'''

def multiples_hola(num: int)->str:
    '''
    Esta funcion recibe un numero entero como parametro y devuelve el mensaje hola N veces
    '''
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            print('Hola')

multiples_hola(2)

def concatenar_hola(num: int)->str:
    '''
    Esta funcion recibe un numero entero como parametro y devuelve el mensaje hola N veces concatenado
    '''
    cadena=''
    for i in range(0, num):
        if num == 0:
            return 1
        else:
            cadena = cadena + 'hola '
    return cadena

saludo=concatenar_hola(3)
print(saludo)

'''
Ejercicio 2 1. Piense cuál sería el resultado de la expresión `misterio(5)` y luego compruebe su hipótesis ejecutándola.

2. Explique con sus palabras qué hace `misterio(a)` para
cualquier `a`, sea positivo, negativo o 0.
'''
#va a imprimir 5
def misterio(a: int) -> int:
  if a == 0:
    return a

  return 1 + misterio(a - 1)

mistery=misterio(5)
print(mistery)

'''
Ejercicio 3
'''