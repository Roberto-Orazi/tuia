num = int(input("Ingrese un numero: "))
mayor = num

while (num != 00): 
    if int(num)>mayor: 
        mayor=num 
    num = int(input("Ingrese un numero, ingrese 00 para finalizar: "))
    
print("El mayor de los tres numeros" , mayor)

# METODO REVERSED
palabra = 'Python1'
for indice in reversed(range(len(palabra))):
    print('indice actual :', indice, 'letra actual', palabra[indice])
    
# METODO Distinto
palabra = 'Python2'
for indice in (range(1,len(palabra)+1)):
    print('indice actual :-', indice, 'letra actual', palabra[-indice])

# METODO -1 -1 -1 
palabra = 'Python3'
for indice in range(len(palabra) - 1, -1, -1):
    print('indice actual :', indice, 'letra actual', palabra[indice])
    
palabra = 'Python'
print(palabra[2:6])