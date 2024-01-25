#EJERCICIO 5
import random
def es_par(num):
    '''
    Esta funcion tiene como parametro un valor entero y nos devuelve un string
    '''
    if(num%2 == 0):
        return "es par"
    else:
        return "no es par"
numero = random.randint(0,100)
x = es_par(numero)

print ("El numero", x, "Y el numero es", numero)

import random
def es_par(num) -> bool:
    '''
    Esta funcion tiene como parametro un valor entero y nos devuelve un string
    '''
    if(num%2 == 0):
        return True
    else:
        return False
numero = random.randint(0,100)
x = es_par(numero)

print ("Es par?", x, "Y el numero es", numero)