#realizar por medio del uso de una estructura de control de flujo interativa la posibilidad de repetir la adivinanza
# hasta que acierte con un limite de hasta 10 intentos.d Tomando de base el enunciado anterior
numero = 5
def guess(numero):
    ad = int(input('Ingrese un entero '))
    if ad == numero:
        print('Muy bien, es el numero que buscaba!!')
        return True
    else:
        print('no hay avierto')
print(guess(numero))

for i in range(10):
    verifica = guess(numero)
    if verifica == True:
        break
    else:
        pass
    i+=1
if(i>9):
    print('se te terminaron todos los aciertos')

#Tomando de base el enunciado del ejercicio 1 proponga un sistema de validacion que al ingresar una nota que no cumpla
#con el rango valido reclame el ingreso nuevamente
def aprobado(nota):
    while(0 > nota > 10):
        print('nota no valida, ingrese un numero entre 0 y 10')
        nota = int(input("ingresar una nota "))
    
    if nota > 0 and nota < 10:
        if nota > 0 and nota < 6:
            print('no aprobado')
        else:
            print('aprobado')
            
aprobado(int(input("ingresar una nota ")))