### Error types ###

# SyntaxError
'''
Son errores de sintaxis
Ej:
print "Hola aca faltan parentesis"
'''
print("Hola aca no falta nada")

# NameError
'''
Son errores por mal escritura de nombre de variables o falta de declaracion
Ej:
print(variable)
name 'variable' is not defined
    print(variable)
NameError: name 'variable' is not defined
'''
variable='anda'
print(variable) # Ahora no me tira mas error porque ya esta declarada/definida la variable

# IndexError
'''
En una lista podemos tener 5 items y hacemos una llamada al 6to item
por lo tanto tira error en el index ya que el numero de index no existe
Ej:
my_list=[1,2,3,4,5] tiene solo cinco elementos pero como arranco en cero el maximo es 4
list index out of range
    print(my_list[5])
IndexError: list index out of range
'''
my_list=[1,2,3,4,5]
print(my_list[4])

# ModuleNotFoundError
'''
Son los errores cuando importamos mal los modulos
Ej:
Si el modulo se llama math pero ponemos maths me va a tirar ese error

Exception has occurred: ModuleNotFoundError
No module named 'maths'
    import maths
ModuleNotFoundError: No module named 'maths'
'''
import math


# AttributeError
'''
Son errores de escritura o existencia en atributos de los modulos
Ej:
Escribimos mal el atributo:

Exception has occurred: AttributeError
module 'math' has no attribute 'PI'
    print(math.PI)
AttributeError: module 'math' has no attribute 'PI'
'''
print(math.pi)

# KeyError
'''
Son errores por mal escritura de las keys en los diccionarios
Ej:
'Apellido': 'Orazi', mi key es Apellido
Si yo llamo Apellid en vez de apellido

Exception has occurred: KeyError
'Apellid'
    print(my_dict['Apellid'])
KeyError: 'Apellid'
'''
my_dict= {
    'Nombre': 'Roberto',
    'Apellido': 'Orazi',
    'Edad': 26,
}

print(my_dict['Apellido'])



# TypeError
'''
Son errores de tipado por lo general por confundir el tipo de dato
Ej:
En las listas si llamamos es numerico
Exception has occurred: TypeError
list indices must be integers or slices, not str
    print(my_list['1'])
TypeError: list indices must be integers or slices, not str
'''
my_list=[1,2,3,4,5]
print(my_list[1])
print(my_list[False]) # esto lo toma como 0
print(my_list[True]) # Esto lo toma como 1

# ImportError
'''
Le erramos atributo que queremos importar
Antes teniamos error de tipado de modulo pero ahora es error de tipado en la importacion

Exception has occurred: ImportError
cannot import name 'PI' from 'math' (unknown location)
    from math import PI
ImportError: cannot import name 'PI' from 'math' (unknown location)
'''

from math import pi


# ValueError
'''
Son errores de tipo de dato
Ej:
tengo un str que es alfanumerico me va a tirar error
Si tengo un str que es solo numerico anda
Exception has occurred: ValueError
invalid literal for int() with base 10: '10 Años'
    my_int= int("10 Años")
ValueError: invalid literal for int() with base 10: '10 Años'
'''
my_int= int("10")
print(my_int)


# ZeroDivisionError
'''
Tira error cuando divido por 0
Exception has occurred: ZeroDivisionError
division by zero
    print(1/0)
ZeroDivisionError: division by zero
'''
print(2/1)