# ASIGNACIONES
#ENTEROS
#ASIGNACIONES INDIVIDUALES
a = 4 # a es una variable de tipo entero
b = 5
#ASIGNACIONES MULTIPLES
c, d = 6, 7
#STRINGS
e = 'hola' # e es una variable de tipo cadena

# OPERACIONES
#SUMA
suma = a + b
#RESTA
resta = a - b
#MULTIPLICACION
multiplicacion = a * b
#DIVISION
division = a / b
#POTENCIA
potencia = a ** b
#MODULO
modulo = a % b
#DIVISION ENTERA
division_entera = a // b

#ESTO ES UN COMENTARIO
'''
ESTO ES UN
COMENTARIO
DE VARIAS LINEAS
'''
"""
ESTO ES UN
COMENTARIO
DE VARIAS LINEAS
"""

#IDENTACION EN PYTHON
if a > b:
    print('a es mayor que b')
else:
    print('a es menor o igual que b')
#DEJAMOS UN ESPACIO

#DETALLES PARA DECLARAR VARIABLES
'''
1-NO SE PUEDE DECLARAR UNA VARIABLE CON UN NUMERO AL INICIO
2-NO SE PUEDE DECLARAR UNA VARIABLE CON ESPACIOS
3-NO SE PUEDE DECLARAR UNA VARIABLE CON CARACTERES ESPECIALES
4-NO SE PUEDE DECLARAR UNA VARIABLE CON PALABRAS RESERVADAS
5-NO SE PUEDE DECLARAR UNA VARIABLE CON ACENTOS
6-NO SE PUEDE DECLARAR UNA VARIABLE CON Ñ
'''
#PEDIR POR PANTALLA
nombre = input('Ingrese su nombre: ')
print('Hola', nombre)

#SCOPE DE LAS VARIABLES
#GLOBAL
def funcion():
    global nombre
    nombre = 'Juan'
    print(nombre)
funcion()
print(nombre)

#LOCAL
def funcion2():
    nombre = 'JORGE'
    print(nombre)
funcion2()
print(nombre)

#TIPOS DE DATOS
#ENTEROS
a = 4
b = 5
c = 6
#FLOAT
d = 4.5
e = 5.6
f = 6.7
#COMPLEJOS
g = 4 + 5j
h = 5 + 6j
i = 6 + 7j
#BOOLEANOS
j = True
k = False
#CADENAS
l = 'hola'
m = 'mundo'
n = 'como estas'
#LISTAS
o = [1, 2, 3, 4, 5]
p = [6, 7, 8, 9, 10]
q = [11, 12, 13, 14, 15]
#TUPLAS
r = (1, 2, 3, 4, 5)
s = (6, 7, 8, 9, 10)
t = (11, 12, 13, 14, 15)
#CONJUNTOS
u = {1, 2, 3, 4, 5}
v = {6, 7, 8, 9, 10}
w = {11, 12, 13, 14, 15}
#DICCIONARIOS
x = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
y = {'nombre': 'Jorge', 'edad': 23, 'dni': 87654321}
z = {'nombre': 'Jose', 'edad': 24, 'dni': 12345678}

#CONVERSION DE TIPOS DE DATOS
#ENTEROS
a = int(4)
b = int(5.6)
c = int('6')
#FLOAT
d = float(4)
e = float(5.6)
f = float('6.7')
#COMPLEJOS
g = complex(4)
h = complex(5.6)
i = complex('6.7')
#BOOLEANOS
j = bool(4)
k = bool(5.6)
l = bool('6.7')
#CADENAS
m = str(4)
n = str(5.6)
o = str('6.7')
#LISTAS
p = list((1, 2, 3, 4, 5))
q = list([6, 7, 8, 9, 10])
r = list({'nombre': 'Juan', 'edad': 22, 'dni': 12345678})
#TUPLAS
s = tuple([1, 2, 3, 4, 5])
t = tuple((6, 7, 8, 9, 10))
u = tuple({'nombre': 'Juan', 'edad': 22, 'dni': 12345678})
#CONJUNTOS
v = set([1, 2, 3, 4, 5])
w = set((6, 7, 8, 9, 10))
x = set({'nombre': 'Juan', 'edad': 22, 'dni': 12345678})
#DICCIONARIOS
y = dict([(1, 2), (3, 4), (5, 6)])
z = dict(((1, 2), (3, 4), (5, 6)))
a1 = dict([['nombre', 'Juan'], ['edad', 22], ['dni', 12345678]])

#OPERADORES ARITMETICOS
#SUMA
a = 4
b = 5
c = a + b
#RESTA
d = 4
e = 5
f = d - e
#MULTIPLICACION
g = 4
h = 5
i = g * h
#DIVISION
j = 4
k = 5
l = j / k
#POTENCIA
m = 4
n = 5
o = m ** n
#MODULO
p = 4
q = 5
r = p % q
#DIVISION ENTERA
s = 4
t = 5
u = s // t

#OPERADORES DE ASIGNACION
#SUMA
a = 4
b = 5
a += b
#RESTA
c = 4
d = 5
c -= d
#MULTIPLICACION
e = 4
f = 5
e *= f
#DIVISION
g = 4
h = 5
g /= h
#POTENCIA
i = 4
j = 5
i **= j
#MODULO
k = 4
l = 5
k %= l
#DIVISION ENTERA
m = 4
n = 5
m //= n

#OPERADORES DE COMPARACION
#IGUAL
a = 4
b = 5
c = a == b
#DIFERENTE
d = 4
e = 5
f = d != e
#MAYOR
g = 4
h = 5
i = g > h
#MENOR
j = 4
k = 5
l = j < k
#MAYOR O IGUAL
m = 4
n = 5
o = m >= n
#MENOR O IGUAL
p = 4
q = 5
r = p <= q

#OPERADORES LOGICOS
#AND && SE TIENEN QUE CUMPLIR LAS 2 CONDICIONES PARA QUE SEA VERDADERO
a = 4
b = 5
c = a == 4 and b == 5
#OR || SE TIENE QUE CUMPLIR O UNA O LA OTRA CONDICION PARA QUE SEA VERDADERO
d = 4
e = 5
f = d == 4 or e == 5
#NOT ! NIEGA LA CONDICION
g = 4
h = 5
i = not(g == 4 and h == 5)

#OPERADORES DE PERTENENCIA
#IN
a = 4
b = [1, 2, 3, 4, 5]
c = a in b
#NOT IN
d = 4
e = [1, 2, 3, 4, 5]
f = d not in e

#OPERADORES PARA CADENAS DE TEXTO
#CONCATENACION
a = 'hola'
b = 'mundo'
c = a + ' ' + b
#REPETICION
d = 'hola'
e = d * 3
#SLICING
f = 'hola mundo'
g = f[0:4]
#LONGITUD
h = 'hola mundo'
i = len(h)
#ITERACION
j = 'hola mundo'
for k in j:
    print(k)
#COMPARACION
l = 'hola'
m = 'mundo'
n = l == m
#MAYOR
o = 'hola'
p = 'mundo'
q = o > p
#MENOR
r = 'hola'
s = 'mundo'
t = r < s
#MAYOR O IGUAL
u = 'hola'
v = 'mundo'
w = u >= v
#MENOR O IGUAL
x = 'hola'
y = 'mundo'
z = x <= y

#ESTRUCTURAS DE CONTROL
#CONDICIONALES
#IF
a = 4
b = 5
if a > b:
    print('a es mayor que b')
else:
    print('a es menor o igual que b')
#ELIF
c = 4
d = 5
if c > d:
    print('c es mayor que d')
elif c == d:
    print('c es igual a d')
elif c != d:
    print('c es diferente a d')
else:
    print('c es menor que d')
#ANIDADOS
e = 4
f = 5
g = 6
if e > f:
    if e > g:
        print('e es mayor que f y g')
    else:
        print('e es mayor que f pero menor que g')
else:
    print('e es menor que f y g')
#OPERADOR TERNARIO
h = 4
i = 5
print('h es mayor que i') if h > i else print('h es menor o igual que i')

#CICLOS DEFINIDOS
#FOR CON RANGE
for c in range(1, 6):
    print(c)
#FOR CON RANGE Y PASO
for d in range(1, 6, 2):
    print(d)
#FOR CON CADENAS
e = 'hola mundo'
for f in e:
    print(f)
#FOR CON LISTAS
a = [1, 2, 3, 4, 5]
for b in a:
    print(b)
#FOR CON TUPLAS
g = (1, 2, 3, 4, 5)
for h in g:
    print(h)
#FOR CON CONJUNTOS
i = {1, 2, 3, 4, 5}
for j in i:
    print(j)
#FOR CON DICCIONARIOS
k = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
for l in k:
    print(l)
#FOR CON DICCIONARIOS Y METODO ITEMS
m = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
for n, o in m.items():
    print(n, o)
#FOR CON DICCIONARIOS Y METODO KEYS
p = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
for q in p.keys():
    print(q)
#FOR CON DICCIONARIOS Y METODO VALUES
r = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
for s in r.values():
    print(s)

#CICLOS INDEFINIDOS
#WHILE
a = 1
while a < 6:
    print(a)
    a += 1
#BREAK
b = 1
while b < 6:
    print(b)
    if b == 3:
        break #INTERRUMPE EL CICLO
    b += 1
#CONTINUE
c = 1
while c < 6:
    c += 1
    if c == 3:
        continue #SALTA LA ITERACION
    print(c)
#ELSE
d = 1
while d < 6:
    print(d)
    d += 1
else:
    print('d es mayor o igual que 6')

#CICLO CON CENTINELA
a = 1
while a != 0:
    a = int(input('Ingrese un numero: (INGRESAR 0 PARA FINALIZAR)'))
    print(a)

#CONTROL DE CICLOS
#BREAK
a = 1
while a < 6:
    print(a)
    if a == 3:
        break #INTERRUMPE EL CICLO
    a += 1
#CONTINUE
b = 1
while b < 6:
    b += 1
    if b == 3:
        continue #SALTA LA ITERACION
    print(b)
#ELSE
c = 1
while c < 6:
    print(c)
    c += 1
else:
    print('c es mayor o igual que 6')
#PASS
d = 1
while d < 6:
    if d == 3:
        pass #NO HACE NADA
    print(d)
    d += 1

#ESTRUCTURAS DE DATOS
#LISTAS
o = [1, 2, 3, 4, 5]
p = [6, 7, 8, 9, 10]
q = [11, 12, 13, 14, 15]
#TUPLAS
r = (1, 2, 3, 4, 5)
s = (6, 7, 8, 9, 10)
t = (11, 12, 13, 14, 15)
#CONJUNTOS
u = {1, 2, 3, 4, 5}
v = {6, 7, 8, 9, 10}
w = {11, 12, 13, 14, 15}
#DICCIONARIOS
x = {'nombre': 'Juan', 'edad': 22, 'dni': 12345678}
y = {'nombre': 'Jorge', 'edad': 23, 'dni': 87654321}
z = {'nombre': 'Jose', 'edad': 24, 'dni': 12345678}

