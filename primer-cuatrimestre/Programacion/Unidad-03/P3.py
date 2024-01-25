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

#En el centro de la ciudad de reosario el estacionamiento en via se encuentra tarifado y
#esta dividido en tres zonas con tarifas diferenciadas. El vehiculo puede estacionarse
#como maximo por 3 horas en el mismo sitio, luego de este tiempo, para renovar el servicio,
#hay que mover el vehiculo. La siguiente tabla muestra los costos por hora en cada una de las zonas:
# zona a primer hora $57,00, segunda hora $71,20, tercera hora $85,50
# zona b primer hora $47,00, segunda hora $58,70, tercera hora $70,50
# zona c primer hora $37,00, segunda hora $46,20, tercera hora $55,50
#Escribir un programa que dada la zona A, B o C y la cantidad de horas estacionadas devuelva
#el costo a pagar. En caso de que el tiempo de estacionamiento supere las tres horas, devolver
#un mensaje de error acorde.
zonaA = 'a'
zonaB = 'b'
ZonaC = 'c'
zona = input("Ingrese la zona en la que se encuentra: ")
if zona == zonaA:
    hora = int(input("Ingrese la cantidad de horas estacionadas: "))
    if hora == 1:
        print("El costo a pagar es de $57,00")
    elif hora == 2:
        print("El costo a pagar es de $71,20")
    elif hora == 3:
        print("El costo a pagar es de $85,50")
    else:
        print("Error tiempo de estacionamiento superado")
elif zona == zonaB:
    hora =int(input("Ingrese la cantidad de horas estacionadas: "))
    if hora == 1:
        print("El costo a pagar es de $47,00")
    elif hora == 2:
        print("El costo a pagar es de $58,70")
    elif hora == 3:
        print("El costo a pagar es de $70,50")
    else:
        print("Error tiempo de estacionamiento superado")
elif zona == ZonaC:
    hora = int(input("Ingrese la cantidad de horas estacionadas: "))
    if hora == 1:
        print("El costo a pagar es de $37,00")
    elif hora == 2:
        print("El costo a pagar es de $46,20")
    elif hora == 3:
        print("El costo a pagar es de $55,50")
    else:
        print("Error tiempo de estacionamiento superado")

#Una marca de ropa tiene descuentos diferentes dependiendo de la sede del local:
#item zapatillas: rosario 30%, funes 40%, roldan 25%
#item remeras: rosario 20%, funes 30%, roldan 15%
#item pantalon: rosario 10%, funes 5%, roldan 20%
#dado un item y una sede, devolver el descuento que se recibira.
#En caso de que el item o la sede no sean validos, devolver un mensaje de error acorde.
zapatillas = 'zapatillas'
remeras = 'remeras'
pantalon = 'pantalon'
rosario = 'rosario'
funes = 'funes'
roldan = 'roldan'
item = input("Ingrese el item que desea comprar: ")
if item == zapatillas:
    sede = input("Ingrese la sede en la que se encuentra: ")
    if item == zapatillas and sede == rosario:
        print("El descuento es de 30%")
    elif item == zapatillas and sede == funes:
        print("El descuento es de 40%")
    elif item == zapatillas and sede == roldan:
        print("El descuento es de 25%")
    else:
        print("Error sede no valida")
elif item == remeras:
    sede = input("Ingrese la sede en la que se encuentra: ")
    if item == remeras and sede == rosario:
        print("El descuento es de 20%")
    elif item == remeras and sede == funes:
        print("El descuento es de 30%")
    elif item == remeras and sede == roldan:
        print("El descuento es de 15%")
    else:
        print("Error sede no valida")
elif item == pantalon:
    sede = input("Ingrese la sede en la que se encuentra: ")
    if item == pantalon and sede == rosario:
        print("El descuento es de 10%")
    elif item == pantalon and sede == funes:
        print("El descuento es de 5%")
    elif item == pantalon and sede == roldan:
        print("El descuento es de 20%")
    else:
        print("Error sede no valida")
else:
    print("Error item no valido")

#Ahora supongamos que ademas dependiendo del dia de la semana se puede recibir un descuento
#adicional acumulable. Es decir si se recibio un descuento del 10% segun el item y la sede y la
#compra se puede realizar un lunes, el descuento total sera un 20%. Escribir un programa en el que la
#persona pueda ingresar el dia de la semana , el item que va acomprar  y la sede del local, luego
#informar el descuento total a recibir, utilizar la siguiente tabla:
#descuento: Lunes 10%, Miercoles 8% y jueves 5%
#item zapatillas: rosario 30%, funes 40%, roldan 25%
#item remeras: rosario 20%, funes 30%, roldan 15%
#item pantalon: rosario 10%, funes 5%, roldan 20%
dia = input("Ingrese el dia de la semana: ")
if dia == 'lunes':
    input("Ingrese el item que desea comprar: ")
    if item == zapatillas:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 40%")
        elif sede == funes:
            print("El descuento es de 50%")
        elif sede == roldan:
            print("El descuento es de 35%")
        else:
            print("Error sede no valida")
    elif item == remeras:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 30%")
        elif sede == funes:
            print("El descuento es de 40%")
        elif sede == roldan:
            print("El descuento es de 25%")
        else:
            print("Error sede no valida")
    elif item == pantalon:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 20%")
        elif sede == funes:
            print("El descuento es de 15%")
        elif sede == roldan:
            print("El descuento es de 30%")
        else:
            print("Error sede no valida")
    else:
        print("Error item no valido")
elif dia == 'miercoles':
    input("Ingrese el item que desea comprar: ")
    if item == zapatillas:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 38%")
        elif sede == funes:
            print("El descuento es de 48%")
        elif sede == roldan:
            print("El descuento es de 33%")
        else:
            print("Error sede no valida")
    elif item == remeras:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 28%")
        elif sede == funes:
            print("El descuento es de 38%")
        elif sede == roldan:
            print("El descuento es de 23%")
        else:
            print("Error sede no valida")
    elif item == pantalon:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 18%")
        elif sede == funes:
            print("El descuento es de 13%")
        elif sede == roldan:
            print("El descuento es de 28%")
        else:
            print("Error sede no valida")
    else:
        print("Error item no valido")
elif dia == 'jueves':
    input("Ingrese el item que desea comprar: ")
    if item == zapatillas:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 35%")
        elif sede == funes:
            print("El descuento es de 45%")
        elif sede == roldan:
            print("El descuento es de 30%")
        else:
            print("Error sede no valida")
    elif item == remeras:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 25%")
        elif sede == funes:
            print("El descuento es de 35%")
        elif sede == roldan:
            print("El descuento es de 20%")
        else:
            print("Error sede no valida")
    elif item == pantalon:
        input("Ingrese la sede en la que se encuentra: ")
        if sede == rosario:
            print("El descuento es de 15%")
        elif sede == funes:
            print("El descuento es de 10%")
        elif sede == roldan:
            print("El descuento es de 25%")
        else:
            print("Error sede no valida")
    else:
        print("Error item no valido")
else:
    print("Error dia no valido")

