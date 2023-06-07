"""" 
. Escriba los siguientes programas. Nota: No utilice los metodos index, min, max, reverse.
a. Dada una lista de números list y un número n, determine en qué índice de la lista list se
encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. Ejemplos
list = [11 ,25 ,3 , -4 ,95]
n = 3
# El programa deber ía mostrar
2

"""
list = [11 ,25 ,3 , -4 ,95]
n = 3
c = n in list
if c == True:
    print(list.index(n))
else:
    print("-1")
""""
list = [1 ,2 ,3 ,4 ,5]
n = 10
# El programa deber ía mostrar
-1
"""
list = [1 ,2 ,3 ,4 ,5]
n = 10
c = n in list
if c == True:
    print(list.index(n))
else:
    print("-1")


""""
b. Dada una lista de números, calcule el mínimo y el máximo de la lista. Nota: es posible hacerlo
recorriendo una única vez la lista o recorriéndola dos veces. Piense las ventajas y desventajas de
ambos métodos.
numeros = [11 ,25 ,3 , -4 ,95]
# El programa deber ía mostrar
El m í nimo es -4
El m á ximo es 95
"""
numeros = [11 ,25 ,3 , -4 ,95]
numeromin = 0
numeromax = 0
for i in range(len(numeros)):
    if numeros[i] == 0:
        numeromin = numeros[i]
        numeromax = numeros[i]
    elif numeros[i] != 0:
        if numeros[i] < numeromin:
            numeromin = numeros[i]
        elif numeros[i] > numeromax :
            numeromax = numeros[i]
print("El minimo es ",numeromin)
print("El maximo es: ",numeromax)

"""
c. Dada una lista de números, cree una nueva lista sumando 1 a cada elemento.
numeros = [0 ,1 ,2 ,3 ,4]
# El programa deber ía mostrar
[1 ,2 ,3 ,4 ,5]

"""
numeros = [0, 1, 2, 3, 4]
nueva_lista = []
for numero in range(len(numeros)):

    nueva_lista.append(numeros[numero]+1)

print(nueva_lista)

"""
d. Dada una lista palabras de cadenas de texto, devuelva una nueva lista formada sólo por las
cadenas de palabras que empiezan con "a".

palabras = [" arbol ", " barco ", " artificial ", " casa ", " dado ", "a"]
# El programa deber ía mostrar
[" arbol ", " artificial ", "a"]
"""

palabras = ["arbol", "barco", "artificial", "casa", "dado ", "a"]
nueva_lista = []
for letra in range(len(palabras)):
    if palabras[letra][0] == "a":
        nueva_lista.append(palabras[letra])
print(nueva_lista)
"""
e. Dada una lista de numeros, calcule, por un lado, la suma de los elemetos que se encuentran en un indice par en la lista y , por otro lado, el producto de los elementos de posiciones con indice impar

"""
numeros = [0,1,2,3,4,5]
suma = 0
producto = 1
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        suma = suma + i     
    else:
        producto = producto * i
print("La suma de los indices pares es ",suma )
print("El producto de indices impares es ",producto)  

"""
f. dada una lista cualquiera, cree una nueva lista con los mismos elementos pero en el orden iverso
"""
numeros = [0 ,1 ,2 ,3 ,4 ,5]
a,b,c,d,e,f = numeros
nueva_lista= [f,e,d,c,b,a]
print(nueva_lista)

"""
2. Escriba un programa que dada una lista de números list devuelva otra lista cuyos elementos sean las
sumas acumuladas de los elementos de list en cada posición. Es decir, una nueva lista donde el primer
elemento es el mismo que en la lista original list, el segundo elemento es la suma del primer y segundo
elementos de list, el tercer elemento es la suma del resultado anterior con el tercer elemento de la
lista original y así sucesivamente. Por ejemplo, dada la lista [1, 2, 3], la suma acumulada debería
ser [1, 3, 6].

"""

numeros = []
numeros2= []
suma = 0

numero = int(input("Ingrese al menos 3 numeros para agregar al a lista( -1 para finalizar): "))
while numero != -1:
    numeros.append(numero)
    numero = int(input("Ingrese al menos 3 numeros para agregar al a lista( -1 para finalizar): "))
for num in range(len(numeros)):
    if numeros[num] == 0:
        numeros2.append(numeros[num])
        suma = numeros[num]
    elif numeros[num] != 0:
        suma += numeros[num]
        numeros2.append(suma)
print("La nueva lista es: ", numeros2)