# CONDICIONALES
    #IF
#if(condicion):
    #Una accion si cumple la condicion print("Hola esto es un if")
   
   #ELIF Si no se cumple la condicion anterior 
#elif(condicion):
    #Una accion si cumple la condicion print("Hola esto es un elif")
#else:
    #if(condicion):
        #Una accion si cumple la condicion print("Hola esto es un elif")
        
    #ELSE Va siempre acompañado del if primero else: Otra accion si no cumple la condicion
        #print("Hola esto es un else")
   
    #None es = a null
    

#EJERCICIO 1
    #ESCRIBIR UN PROGRAMA QUE PREGUNTE AL USUARIUO SU EDAD Y MUESTRE POR PANTALLA SI ES MAYOR DE EDAD O NO 

edad = int(input("ingresa tu edad "))
if(edad >0 & edad<18):
    print("Es menor de edad")
elif(edad>=18):
    print("Es mayor de edad")
else:
    print("Edad no valida, ingrese devuelta")

#Ejercicio 2. Escribir un programa que almacene la cadena de caracteres 'pepito' en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la
# variable sin tener en cuenta mayúsculas y minúsculas. Ayuda: investigar los métodos 'upper' y 'lower'

Contraseña1 = 'pepito'
ContraseñaIng = input("Ingrese la contraseña ")
if Contraseña1 == ContraseñaIng:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
    
#Ejercicio 3. Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de
# forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
# del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4
# y 18 años debe pagar 5 pesos y si es mayor de 18 años, 10 pesos.

edad = int(input("Ingrese la edad "))
if(edad<0):
    print("Edad incorrecta reingresela")
else:
    if edad > 0 and edad < 4:
        print("Entra gratis")
    if edad >= 4 and edad < 18:
        print("Tiene que pagar 5 pesos la entrada")
    else:
        print("Tiene que pagar 10 pesos la entrada")
        

#Ejercicio 4. Dada la nota de un parcial se quiere saber en que condición está el alumno.

#Si la nota es mayor igual a 6 se debe mostrar en pantalla un mensaje que diga 'aprobado'. Si la nota es mayor o igual a
#0 y menor a 6: 'desaprobado'. Primero resolver utilizando solo condicional if y luego condicional compuesto.

Nota1 = int(input("Ingresar Nota1 del alumno "))
if Nota1 >= 6 and Nota1 <=10:
    print("Aprobo")
if Nota1 < 6:
    print("No aprobo")
else:
    print("Nota mal cargada")

Nota2 = int(input("Ingresar Nota2 del alumno "))
if 10>= Nota2 >= 6:
    print("Aprobo")
elif(Nota2 < 6):
    print("No aprobo")
else:
    print("Nota mal cargada")
    

#Ejercicio 5. Realizar el mismo programa pero con las verificaciones en el siguiente orden:

#Si la nota no está entre 0 y 10: 'nota inválida'. Si la nota es mayor o igual a 0 y menor a 6: 'desaprobado'. Si la
#nota es mayor igual a 6 se debe mostrar en pantalla un mensaje que diga 'aprobado'.

Nota = int(input("Ingresar Nota del alumno "))
if(0 > Nota > 10):
    print("Nota invalida")
else:
    if(Nota < 6):
        print("Desaprobado")
    elif(Nota <= 10):
        print("Aprobado")
        
#Ejercicio 6. El gobierno nacional implementa un plan de vivienda subsidiado.

#Las condiciones para acceder a este tipo de financiación son las siguientes:

#- tener nacionalidad argentina
#- ser mayor de edad
#- no poseer vivienda propia
#- ser empleado en relacion de dependencia, con ingresos netos no mayores a 2.646.009,01 de pesos anuales
#- ser monotributista, sin superar la categoria G (2.646.009,01 de facturación anual)

#Escribir un programa que pida los datos necesarios, y por medio del control de flujo por declaraciones condicionales
# if-elif-else, pueda evaluar si la persona califica o no para el crédito e imprima por pantalla si califica o no para
# el mismo.

#Ayuda: armar un diagrama de flujo antes de comenzar

Nacionalidad1 = input("Ingrese nacionalidad " )
Edad1 = int(input("Ingrese edad "))
Vivienda1 = input("Tiene vivienda? si o no ")
Ingresos1 = float(input("ingresa tus ganacias "))

if(Nacionalidad1 == "argentina"):
    if(Edad1 >= 18):
        if(Vivienda1 == "si"):
            if(Ingresos1 < 2646009.01):
                print("Podes acceder al plan de vivienda")
            else:
                print("No calificas para el plan de vivienda")


Nacionalidad = input("Ingrese nacionalidad " )
if(Nacionalidad == "argentina"):
    Edad = int(input("Ingrese edad "))
else:
    print("No calificas para el plan de vivienda")
if(Edad >= 18):
        Vivienda = input("Tiene vivienda? si o no ")
else:("No calificas para el plan de vivienda")
if(Vivienda == "si"):
        Ingresos = float(input("ingresa tus ganacias "))
else:("No calificas para el plan de vivienda")
if(Ingresos < 2646009.01):
                print("Podes acceder al plan de vivienda")
else:
                print("No calificas para el plan de vivienda")
                


x = int(input('es argentino')) # 1 SI - 0 NO

if x:
    x = int(input('Es mayor de 18?')) # 1 SI - 0 NO
else:
    print("No calificas para el plan de vivienda")