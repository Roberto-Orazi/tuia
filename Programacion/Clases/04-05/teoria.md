# CLASE DE TEORIA 05/04

## Estructuras de control Interacion

Cantidad conocida de repeticiones osea ciclos definidos

````
for <variable> in <secuencia de valores>:
    instrucciones
````
secuencia de valores: puede ser generada por otros medios: range(inicio, fin, salto)

El unico parametro obligatorio es el fin, ya que sino no seria definido
````
range(2)
secuencia[0,1]
tenemos solo el fin, que es 2 y por defecto el salto es de 1

range(1,2)
secuencia(1)
Ya que seria inicio en 1 y fin en 2 

ramge(1,10,2)
secuencia(1,3,5,7,9)
Inicia en 1 salta de a 2 y termina en 10
````
````
num = int(input("Ingrese un numero: "))
mayor = num
for i in range(2):
    num = int(input("Ingrese un numero: "))
    if num>mayor:
        mayor=num
print("El mayor de los tres numeros" , mayor)


````

A veces no sabemos la cantidad de repeticiones, entonces:

````
cant=int(input("Cuantos numeros ingresara: "))
num = int(input("Ingrese un numero: "))
mayor = num

for i in range(cant - 1):
    num = int(input("Ingrese un numero: "))
    if num>mayor:
        mayor=num

print("El mayor de los tres numeros": , mayor)

````

Cuando no se sabe la cantidad que voy a ingresar:

### Cantidad desconocida de repeticiones osea ciclos indefinidos
## Estructura while

````
while <condicion>:
    instrucciones
````

````
num = int(input("Ingrese un numero: "))
mayor = num

while (mas_datos.lower()== "si"):
    num = int(input("Ingrese un numero: "))
    if num>mayor:
        mayor=num
    mas_datos=input("Hy mas nums para ingresar(si-no)?: ")

print("El mayor de los tres numeros" , mayor)
````

````
num = int(input("Ingrese un numero: "))
mayor = num

while i < 1000:
    num = int(input("Ingrese un numero: "))
    if num>mayor:
        mayor=num
    i++
print("El mayor de los tres numeros" , mayor)
````

````
num = int(input("Ingrese un numero: "))
mayor = num

while (num != 00):
    if int(num)>mayor:
        mayor=num
    num = int(input("Ingrese un numero, ingrese 00 para finalizar: "))

print("El mayor de los tres numeros" , mayor)
````
## Condicion BREAK
### SALTA TODA LA ITERACION
````
while <condicion>:
    <hacer_algo1>
    if <condicion if>:
        break
    <hacer_algo2>
````

````
num = int(input("Ingrese un numero: "))
mayor = num

while (True):
    if num > mayor
        mayor = num
    num = int(input("Ingrese un numero, ingrese -1 para finalizar: "))
    if (num == -1):
        break

print("El mayor de los tres numeros" , mayor)


````

## Condicion CONTINUE
### ES PARA SALTAR UNA SOLA INTERACION
````
for letra in 'Python':
    if letra == 'h':
        continue
    print('Letra actual : , letra')

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Valor actual : ', var)
print('Fin!')
````
## Condicion PASS
### Cuando todavia no sabemos lo que tenemos que hacer usamos el pass para que no tire error.
````
i = 0

if(i<5):
    pass

print('Fuera del bucle')
````

### Recorriendo Strings
````
palabra = 'Python'
for indice in range(len(palabra)):
    print('indice actual :', indice, 'letra actual', palabra[indice])

````

### Recorriendo Strings en reversa

````
palabra = 'Python'
for indice in range(len(palabra)):
    print(palabra[len(palabra)-indice-1])
````

### Recorriendo Strings en reversa indice negativo

````
palabra = 'python'
for indice in range(-1, len(palabra)-1, -1):
    print('indice actual :', indice, 'letra actual :', palabra[indice])
````

## STRING SLICING

````
palabra = 'Python'
print(palabra[2:5])
#tho
````






