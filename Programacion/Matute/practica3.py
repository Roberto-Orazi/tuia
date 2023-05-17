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
