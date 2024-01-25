#Imprimir los primero 20 numeros naturales
for i in range(1,21):
    print(i)

#Imprimir la table de multiplicar del 5
for i in range(1,11):
    print("5 x",i,"=",5*i)

#Imprima los numeros de -10 a -1
for i in range(-10,0):
    print(i)

#Dada la siguiente secuencia de numeros:
# numeros = [12, 75, 150, 180, 145, 525, 50]
#Imprima todos los numeros divisibles por 5 menores a 150
numeros = [12, 75, 150, 180, 145, 525, 50]
for i in numeros:
    if i%5==0 and i<150:
        print(i)

#Imprimir los primeros 10 valores de la secuencia de fibonacci. La secuencia de fibonacci es
#una serie denumeros en la cual los dos primeros numeros son 0 y 1, y el siguiente numero se corresponde
#a la suma de los 2 numeros anteriores
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
a=0
b=1
for i in range(10):
    print(a)
    a, b=b, a+b
#Imprimir el valor factorial del numero 5 usando un bucle. El valor factorial
#se optiene de multiplicar todos los numeros enteros desde el numero elegido
#hasta 1. Por ejemplo, el factorial de 5 es 5*4*3*2*1 = 120
a=1
for i in range(1,6):
    a=a*i
print(a)

#Explique el resultado de los siguientes programas
#A
lista=[]
for j   in  lista:
    print(j)
#El programa no imprime nada porque la lista esta vacia
#B
i=1
for i in [1,2,3]:
    print(i)
print(i)
#El programa imprimita 1,2,3 y 3 porque el ultimo valor de i es 3

#Resolver los siguientes ejercicios
#A Calcular el cuadrado de los primeros 10 numerois enteros
for i in range(1,11):
    print('Ej 8-A',i**2)
#B Calcular la suma de los numeros enteros entre 0 y 100 inclusive
a=0
for i in range(101):
    a=a+i
print('Ej 8-B',a)
#Calcular la suma de los numeros pares menores a 100, Cuantos numeros pares
#hay menores a 100?
a=0
for i in range(101):
    if i%2==0:
        a=a+i
print('Ej 8-C',a)
#Calcular la suma de los numeros impares menores a 100, Cuantos numeros impares
#hay menores a 100?
a=0
for i in range(101):
    if i%2!=0:
        a=a+i
print('Ej 8-D',a)

#Cual es el problema asociado al siguiente programa, no hace falta
#ejecutarlo para responder esta pregunta
x = 0
while x < 5:
    print(x)
    break #USO EL BREAK PARA QUE NO ENTRE EN BUCLE INFINITO pero no esta incluido en el programa
#Entra en bucle infinito porque x siempre es menor a 5

#Escriba un programa que dada una secuencia de numeros y un valro de umbral vaya sumando los numeros
# de la secuencia hasta que la suma alcance el umbral. Utilice break para temrinar la ejecucion
#del bucle cuando la suma alcance el umbral.
umbral = 21
valores = [3,5,4,4,5,5,3,5,2,7]
#suma = 21
suma=0
for i in valores:
    suma=suma+i
    if suma>=umbral:
        break
print('Ej 9',suma)

umbral=34
valores=[3,5,4,4,5,5,3,5,2,7]
#suma->34
suma=0
for i in valores:
    suma=suma+i
    if suma>=umbral:
        break
print('Ej 10',suma)
umbral=100
valores=[3,5,4,4,5,5,3,5,2,7]
#suma->43
suma=0
for i in valores:
    suma=suma+i
    if suma>=umbral:
        break
print('Ej 11',suma)

#Escriba un programa que dada una secuencia de numerica compute la suma de los numeros pares.
#utilice un bucle while y la secuencia continue para saltear los casos donde el numero no sea par.
#valores=[1,2,3,4,5,6,7,8,9,10]
#suma=30
valores=[1,2,3,4,5,6,7,8,9,10]
suma=0
while len(valores)>0:
    if valores[0]%2==0:
        suma=suma+valores[0]
    valores.pop(0)
print('Ej 12',suma)


#valores=[1,4,7,10]
#suma->14
valores=[1,4,7,10]
suma=0
while len(valores)>0:
    if valores[0]%2==0:
        suma=suma+valores[0]
    valores.pop(0)
print('Ej 13',suma)

#escriba un programa que solicite un numero entero al usuario y compute la
# suma de todos los numeros naturales menores a el. Este programa debe ser
# interactico, es decir el programa solicita un numero al usuario y devuelve
# la suma, y solicita un numero numero, esto continua asi hasta que el
# usuario ingresa salir, determinando que el programa debe terminar. utilice
# un bucle while para resolver este problema, tenga en cuenta la sentencia
# break para determinar la interrupcion del bucle.
#Ejemplo de ejecucion:
#Ingrese un numero: 5
#la suma de los numeros naturales menores a 5 es 10
numero = int(input('Ingrese un numero: '))
suma=0
while numero!='salir':
    for i in range(numero):
        suma=suma+i
    print('la suma de los numeros naturales menores a',numero,'es',suma)
    numero = input('Ingrese un numero: ')
    if numero != 'salir':
        numero=int(numero)
    suma=0
print('Ej 14')

grosorBillete = 0.11 * 0.001 # 0.11 mm en metros 0,00011m
alturaMonumento = 70 # altura en metros
numBilletes = 1
dia = 1
while numBilletes * grosorBillete <= 70:
    print(dia, numBilletes, numBilletes * grosorBillete)
    dia = dia + 1
    numBilletes = numBilletes * 2
print('Cantidad de dias', dia)
print('Cantidad de billetes', numBilletes)
print('Altura final', numBilletes * grosorBillete)

