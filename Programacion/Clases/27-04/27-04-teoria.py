#Dado los 3 lados de un triangulo:
    #Determinar si es Equilatero isosceles o escaleno.

#1ER RESOLUCION 
l1 = input("Ingresar lado 1 ") 
l2 = input("Ingresar lado 2 ") 
l3 = input("Ingresar lado 3 ") 
if(l1 == l2 and l2 == l3): 
    print("El triangulo es Equilatero") 
elif(l1 == l2 and l2 != l3 or l1 != l2 and l2 == l3 ):
    print("El triangulo es isosceles") 
else: 
    print("El triangulo es escaleno")
#2DA RESOLUCION 
l4 = input("Ingresar lado 1 ") 
l5 = input("Ingresar lado 2 ") 
l6 = input("Ingresar lado 3 ") 
if(l4 ==l5):
    if(l5==l6):
        print("El triangulo es Equilatero") 
    else:
        print("El triangulo es isosceles")
if(l4 != l5):
    if(l5 == l6):
        print("El triangulo es isosceles")        
    else:
        print("El triangulo es escaleno")
#3ER RESOLUCION 
l7 = input("Ingresar lado 1 ") 
l8 = input("Ingresar lado 2 ") 
l9 = input("Ingresar lado 3 ") 
if(l7==l8 and l8==l9):
    print("El triangulo es equilatero")
elif(l7==l8 or l7==l9 or l8==l9):
    print("El triangulo es iscosceles")
else:
    print("El triangulo es escaleno")
'''
    CASO PRACTICO FUNCION DEL TRIANGULO PERO COMO FUNCION
'''
print("1ER MANERA")
def definir_triangulo(lado_1,lado_2,lado_3) :
    if(lado_1 == lado_2 and lado_2 == lado_3):
        print("Equilatero")
    elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
        print("Isosceles")
    else: 
        print("Escaleno")
    return
definir_triangulo(1,2,3)
print("2DA MANERA")
def definir_triangulo():
    lado_4 = input("Ingresar lado 1 ") 
    lado_5 = input("Ingresar lado 2 ") 
    lado_6 = input("Ingresar lado 3 ") 
    if(lado_4==lado_5 and lado_5==lado_6):
        print("El triangulo es equilatero") #ESTA MAL USAR PRINT YA QUE LO IMPRIME EN PANTALLA
    elif(lado_4==lado_5 or lado_4==lado_6 or lado_5==lado_6):
        print("El triangulo es iscosceles")
    else:
        print("El triangulo es escaleno")    
    return
definir_triangulo()
print("3RA MANERA")
def triangulo(L1,L2,L3):
    if(L1==L2==L3):
        return "Equilatero"
    elif(L1==L2 or L1==L3 or L2==L3):
        return "Isosceles"
    else:
        return "Escaleno"
x = triangulo(1,2,3)
print(x)
x = triangulo(2,2,2)
print(x)