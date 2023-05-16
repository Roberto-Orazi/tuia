#Dada una contraseña verificar que su longitud es superior a 8 caracteres
password = input("Ingrese su contraseña: ")
if len(password) > 8:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

#Escribir un programa que verifique si un numero es divisible por 4
numero = int(input("Ingrese un numero: "))
if numero % 4 == 0:
    print("El numero es divisible por 4")
else:
    print("El numero no es divisible por 4")

#Determinar e informar el mayor valor de 3 numeros enteros.
#Que cambiarias en el algoritmo si se trataran de 3 numeros reales o de 3 caracteres o de 3 palabras?
#Y si se buscara el menor valor?
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if num1 > num2 and num1 > num3:
    print("El primer numero es el mayor")
elif num2 > num1 and num2 > num3:
    print("El segundo numero es el mayor")
else:
    print("El tercer numero es el mayor")
#Cambiaria el tipo de variable que se le asigna a los numeros
#Si se buscaria el menor valor, cambiaria el signo de la comparacion

#Dado 3 lados de un triangulo informar si es equilatero, isosceles o escaleno
lado1 = int(input("Ingrese el primer lado: "))
lado2 = int(input("Ingrese el segundo lado: "))
lado3 = int(input("Ingrese el tercer lado: "))
if lado1 == lado2 and lado1 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")

#Convertir las calificaciones alfabeticas 'I', 'A', 'B', 'M', 'D' y 'E' en calificaciones numericas
# 5,6,7,8,9,10 respectivamente. Ingresar una califacion alfabetica e informar por pantalla la
# calificacion numerica correspondiente, en caso de ingresar cualquier otra letra mostrar((Error calificacion no valida))
calificacion = input("Ingrese su calificacion: ")
if calificacion == 'I':
    print("Su calificacion es 5")
elif calificacion == 'A':
    print("Su calificacion es 6")
elif calificacion == 'B':
    print("Su calificacion es 7")
elif calificacion == 'M':
    print("Su calificacion es 8")
elif calificacion == 'D':
    print("Su calificacion es 9")
elif calificacion == 'E':
    print("Su calificacion es 10")
else:
    print("Error calificacion no valida")

#Escribir un programa que le pregunte a las personas su fecha de cumpleaños y
# en base a eso imprimit su signo zodiacal.
#Recomendacion, pedirle a la persona que ingrese la fecha con cierto formato, por ejemplo:
# DD/MM y si la persona no la respeta imprimit un mensaje de error
dia = int(input("Ingrese el dia de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))
if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    print("Su signo zodiacal es Aries")
elif dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
    print("Su signo zodiacal es Tauro")
elif dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
    print("Su signo zodiacal es Geminis")
elif dia >= 22 and mes == 6 or dia <= 22 and mes == 7:
    print("Su signo zodiacal es Cancer")
elif dia >= 23 and mes == 7 or dia <= 23 and mes == 8:
    print("Su signo zodiacal es Leo")
elif dia >= 24 and mes == 8 or dia <= 23 and mes == 9:
    print("Su signo zodiacal es Virgo")
elif dia >= 24 and mes == 9 or dia <= 23 and mes == 10:
    print("Su signo zodiacal es Libra")
elif dia >= 24 and mes == 10 or dia <= 22 and mes == 11:
    print("Su signo zodiacal es Escorpio")
elif dia >= 23 and mes == 11 or dia <= 21 and mes == 12:
    print("Su signo zodiacal es Sagitario")
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    print("Su signo zodiacal es Capricornio")
elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
    print("Su signo zodiacal es Acuario")
elif dia >= 20 and mes == 2 or dia <= 20 and mes == 3:
    print("Su signo zodiacal es Piscis")
else:
    print("Error fecha no valida")


