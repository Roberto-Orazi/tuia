# 1- 
# a- el print va despues de declarar las funciones
saludo = "Hola";
destino = "Mundo";
puntuacion = "!";
print(saludo + " " + destino + puntuacion)

# b-
cateto1 = 3;
cateto2 = 4;
hipotenusa = ((cateto1  ** cateto2) + (cateto2 ** 2)) ** 0.5;
del cateto1;
del cateto2;
print(hipotenusa)

# c- primero hay que declararlsa y despues borrar su contenido
tengo_hambre = False;
print(tengo_hambre)
del tengo_hambre;
# SI IMPRIMIMOS LA VARIABLE NOS VA A FIGURAR QUE NO ESTA DEFINIDA
tengo_hambre = True;
print(tengo_hambre)
del tengo_hambre;
# SI IMPRIMIMOS LA VARIABLE NOS VA A FIGURAR QUE NO ESTA DEFINIDA

# 2- ENCONTRAR IGUALDADES
# a- 3
print(6/2 == 3)

# b- 3.0
print(6.0/2 == 3.0)

# c- (0.1 + 0.2) * 10

print((0.1 + 0.2) * 10 == 3+0.0000000000000004)

# d- 22 / 7
pi = 3.142857142857143;
print(22/7 == pi)

# e- 22 // 7
print(22//7 == 3)

# 3-
# a- 
print(10+5)
#nos devuelve entero
print(10+5.0)
#nos devuelve real
print(10+5.)
#nos devuelve real

# b- 
print(11/2)
#nos devuelve real es una division comun
print(11//2)
#nos devuelve el entero redondeando siempre para abajo
print(11.0//2)
#nos devuelve el entero redondeado para abajo pero 
# de forma real ya que es division de un real  

#4-
# a- =2
print(1 +1)

# a- = 0 
print(1 -1)

# a- =0
print(1 +-1)

# a- =0
print(1 -1)

#5
# a-
temperatura1 = int(input("Temperatura habitacion 1 "));
temperatura2 = int(input("Temperatura habitacion 2 "));
print((temperatura1 + temperatura2) / 2)

# b-
cantidadGente = 10;
tiempoNombre = 4.5;
tiempoTotal = (tiempoNombre *(cantidadGente * (cantidadGente -1)))
print(tiempoTotal) 

# c-
persona1 = input("ingresa tu nombre ");
persona2 = input("ingresa tu nombre ");

if(persona1 == persona2):
    print("tienen el mismo nombre");
else: print("no tienen el mismo nombre");

if(len(persona1) == len(persona2)):
    print("Tienen el mismo largo")
else: print("No tienen el mismo largo");

# 6- comprobar si son v o f 
# a- FALSO
print(len("Hola, mundo") == 14)


# b- VERDADERO
import math
print(25 == math.sqrt(625) )

# c- VERDADERO
print(3.25 * 2 < 7 and 3.25 * 2 > 6)

# d- FALSO YA QUE 4(2+2) NO ES IGUAL A 5
print(22/7 > 3 and 4 == 5)

# e- TIRA ERROR YA QUE NO SE PUEDE DIVIDIR 0 POR 0 
#print(10 > 5 | 0 / 0 == 0)
#SACAR EL # PARA COMPROBAR EL ERROR
# f- TIRA ERROR YA QUE NO SE PUEDE SUMAR UN STRING CON UN ENTERO O REAL
#print(len("Python")==5 & 1+"1" == 2)
#SACAR EL # PARA COMPROBAR EL ERROR

# 7- PONER PARENTESIS SEGUN REGLA DE PRECEDENCIA
# a- 16.0
print((3 * 5)- ((7 * 4) / 14) + (3 / 1))

# b- 2.0
print((2 ** 1) + (3 / 5) // 4)

# c- 0.125
print(8 / 4 / (2 ** 2 ** 2))

