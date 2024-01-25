<<<<<<< Updated upstream
print(nueva_lista)
=======
#1. Imprimir los primeros 20 números naturales.
for i in range(1,21):
    print(i)
# 2. Imprimir la tabla de multiplicar del número 5
num = 5
for e in range(0,11):
    print(num*e)

#3. Imprima los números de -10 a -1.
for b in range(-10,0):
    print(b)

#4. Dada la siguiente secuencia de números: numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50] #lista
for index in numeros:
    if index % 5 == 0 and index < 150:
        print(index)

#5. Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie de números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la suma de los dos números anteriores. Resultado esperado: 0 1 1 2 3 5 8 13 21 34
v = 0
v1 = 1
for f in range(10):
    print(v)
    v,v1 = v1, v+v1
#6. Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120
a = 1
for i in range(1,6):
    a = a*i
    
print(a)

# 7 Explica
lista = []
for j in lista:
    print(j) #no imprime nada 
#8 Resuelva los siguientes ejercicios: 
# a. Calcular el cuadrado de los primeros 10 números enteros. 
# b. Calcular la suma de los números enteros entre 0 y 100 inclusive. 
# c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a 100? 
# d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores a 100?
#a
for i in range(0,10):
    print(i*i)
#b
suma = 0
for i in range(0,101):
    suma = suma+i

print(suma)

#c 
pares = 0
contador = 0
for i in range(2,102,2):
    contador += 1
    pares = pares+i
print(pares)
print(contador)

# c
impares = 0
contador = 0
for i in range(1,101,2):
    impares = impares+i
    contador += 1
print(impares)
print(contador)

# 10. Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los números de la secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución del bucle cuando la suma alcance el umbral.

umbral = 21
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
suma = 0
for i in valores:
    suma = suma + i
    if suma >= umbral:
        break
print(suma)
# b
umbral = 34
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
suma2 = 0
for i in valores:
    suma2 = suma2 + i
    if suma2 >= umbral:
        break
print(suma2)

#11. Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
valores = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
sumapares = 0
i = 0
while i < len(valores):
    num = valores[i]
    if num % 2 != 0:
        i += 1
        continue
    sumapares = num+sumapares
    i += 1
print(sumapares)

#12 Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero al usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario ingresa "salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle. Ejemplos:

salir = True
while salir:
    suma = 0
    numero = int(input("Ingrese un numero entero (-1 para finalizar): "))
    for i in range(numero):
        suma = suma + i
        if i >= numero:
            continue
    print(suma)
    if numero == -1:
        break


#13. Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar a resolver el problema:
billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # altura en metros
altura_pila = billete_grosor
dia = 1

while  altura_pila <= altura_monumento:
    altura_pila *= 2 
    dia +=1
print(dia)

# 14. Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero hay, que sean menores que el segundo.a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo. b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo. c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
num1 = int(input("Ingrese el primer parametro: "))
num2 = int(input("Ingrese el segundo parametro: "))
>>>>>>> Stashed changes
