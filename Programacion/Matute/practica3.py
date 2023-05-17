#Enunciado 
#
contrasenia = input("Ingresar tu contraseñá:")
if len(contrasenia) > 8:
    print("Contraseña correcta")
else: 
    print("Repita su contraseña")

#2. Escribir un programa que verifique si un numero es divisible por 4

divisible = int(input("Ingrese un numero, y te vamos a decir si es divisible por 4: "))
if (divisible % 4) == 0 :
    print("Es divisible por 4")
else:
    print("Te puse")

#3. Determinar e informar el mayor valor de 3 numeros enteros. ¿Que cambiarıas en el algoritmo si se trataran de 3 numeros reales o de 3 caracteres o de 3 palabras?. ¿Y si se buscara el menor valor?


def valorMasAlto(valor1,valor2,valor3):
    if valor1 > valor2 and valor1 > valor3:
        print("El",valor1,"es el mayor")
    elif valor2 > valor1 and valor2 > valor3:
        print("El",valor2,"es el mayor")
    else:
        print("El",valor3,"es el mayor")
    return 

#4. Dados 3 lados de un tri´angulo, informar si el mismo es equil´atero, is´osceles o escaleno

lado1 = int(input("Ingrese la medida del primer lado: "))
lado2 = int(input("Ingrese la medida del segundo lado: "))
lado3 = int(input("Ingrese la medida del tercer lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("El triangulo es el equilatero")
elif lado2 == lado1 and lado2 != lado3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")

#5. Convertir las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en calificaciones numericas 5, 6, 7, 8, 9 y 10 respectivamente. Ingresar una calificacion alfabetica e informar por pantalla la calificacion numerica correspondiente, en caso de ingresar cualquier otra letra mostrar ((error calificacion inexistente)).

ingreseUnaLetra = str(input("Ingrese una de estas letras para saber el valor de su calificacion: I, A, B, M, D y E: "))
letraElegida = ingreseUnaLetra.lower()
if letraElegida == "i":
    print("La nota es: 5")
elif letraElegida == "a":
    print("La nota es:6")
elif letraElegida == "b":
    print("La nota es: 7")
elif letraElegida == "m":
    print("La nota es: 8")
elif letraElegida == "d":
    print("La nota es: 9")
elif letraElegida == "e":
    print("La nota es: 10")
else:
    print("Calificacion incorrecta")

#6. Escribir un programa que le pregunte a las personas su fecha de cumpleanos y en base a eso imprimir su signo zodıaco. Recomendacion, pedirle a la persona ingresar la fecha con cierto formato, por ejemplo DD/MM y si la persona no lo respeta, imprimir un mensaje de error.





#7. En el centro de la ciudad de Rosario el estacionamiento en vıa se encuentra tarifado y esta dividido en tres zonas con tarifas diferenciadas. El vehıculo puede estacionarse como maximo por 3 horas en el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el vehıculo. La siguinte tabla muestra los costos por hora en cada una de las zonas:
cospel = str(input("Ingrese la zona, ingresando: A, B o C ")).lower()
if cospel == "a":
    cantidad = int(input("Ingrese la cantidad de horas que quieres quedarte, maximo 3hs: "))
    if cantidad == 1: 
        print("Ustedes debe pagar $57,00")
    elif cantidad == 2:
        print("Usted debe abonar $71,20")
    elif cantidad == 3:
        print("Usted debe abonar $85,50")
    else: 
        print("Ingresaste mal la informacion por favor intente otra vez.")
elif cospel == "b":
    cantidad = int(input("Ingrese la cantidad de horas que quieres quedarte, maximo 3hs: "))
    if cantidad == 1:
        print("Usted debe abonar $47,00")
    elif cantidad == 2:
        print("Usted debe abonar $58,70")
    elif cantidad == 3:
        print("Usted debe abonar $70,50")
    else: 
        print("Ingresaste mal la informacion por favor intente otra vez.")
elif cospel == "c":
    cantidad = int(input("Ingrese la cantidad de horas que quieres quedarte, maximo 3hs: "))
    if cantidad == 1:
        print("Usted debe abonar $37,00")
    elif cantidad == 2:
        print("Usted debe abonar $46,70")
    elif cantidad == 3:
        print("Usted debe abonar $55,50")
    else: 
        print("Ingresaste mal la informacion por favor intente otra vez.")
else: 
    print("Ingresaste mal la informacion por favor intente otra vez.")



# Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local
"""
prenda = str(input("Ingrese que tipo de prenda quiere(zapatillas, remeras, pantalones): ")).lower()
if prenda == "zapatillas":
    ciudad = str(input("Ingrese de que ciudad sos(Rosario,Funes y Roldan): "))
    if ciudad == "rosario":
        print("El descuento es de 30%")
    elif ciudad == "funes":
        print("El descuento es del 40%")
    elif ciudad == "roldan":
        print("El descuento es de 25%")
    else:
        print("Ingresaste mal la informacion por favor intente devuelta.")
elif prenda == "remeras":
    ciudad = str(input("Ingrese de que ciudad sos(Rosario,Funes y Roldan): "))
    if ciudad == "rosario":
        print("El descuento es de 20%")
    elif ciudad == "funes":
        print("El descuento es del 30%")
    elif ciudad == "roldan":
        print("El descuento es de 15%")
    else:
        print("Ingresaste mal la informacion por favor intente devuelta.")
elif prenda == "pantalones":
    ciudad = str(input("Ingrese de que ciudad sos(Rosario,Funes y Roldan): "))
    if ciudad == "rosario":
        print("El descuento es de 10%")
    elif ciudad == "funes":
        print("El descuento es del 5%")
    elif ciudad == "roldan":
        print("El descuento es de 20%")
    else:
        print("Ingresaste mal la informacion por favor intente devuelta.")
else:
    print("Ingresaste mal la informacion por favor intente devuelta.")
"""
# . Ahora, supongamos que ademas dependiendo del dıa de la semana se puede recibir un descuento adicional acumulable. Es decir, si se recibio un descuento del 10 % segun el ıtem y la sede y la compra se realiza un lunes, el descuento total sera un 20 % . Escribir un programa en el que la persona pueda ingresar el d´ıa de la semana, el item a comprar y la sede del local. Luego, informar el descuento total a recibir. Utilizar la siguiente tabla de descuentos:

dia = str(input("Ingrese el dia de la semana(lunes,martes,miercoles,jueves,viernes): ")).lower()
if dia == "lunes":
    prenda = str(input("Ingrese que prenda quiere comprar(zapatillas, remeras, pantalones): ")).lower()
    if prenda == "zapatillas":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de %40.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 50%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 35%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "remeras":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 30%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 40%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 25%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "pantalones":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 20%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 15%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 30%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    else:
        print("Ingresaste mal la informacion por favor intente devuelta")
elif dia == "miercoles":
    prenda = str(input("Ingrese que prenda quiere comprar(zapatillas, remeras, pantalones): ")).lower()
    if prenda == "zapatillas":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 28%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 48%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 32%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "remeras":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 28%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 38%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 22%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "pantalones":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 18%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 13%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 28%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
elif dia == "jueves":
    prenda = str(input("Ingrese que prenda quiere comprar(zapatillas, remeras, pantalones): ")).lower()
    if prenda == "zapatillas":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 35%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 45%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 30%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "remeras":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 25%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 35%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 20%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
    elif prenda == "pantalones":
        localidad = str(input("Ingrese de que localidad es(Rosario, Funes y Roldan): ")).lower()
        if localidad == "rosario":
            print("Su descuento por el dia y por el producto sera de 15%.")
        elif localidad == "funes":
            print("Su descuento por el dia y por el producto es de 10%.")
        elif localidad == "roldan":
            print("Su descuento por el dia y por el producto es de 25%.")
        else:
            print("Ingresaste mal la informacion, intente otra vez.")
else:
    print("Ingresaste mal la informacion, intente otra vez.")