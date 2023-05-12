def menu():
    print("Menu")
    print("1- Crear contacto")
    print("2- Modificar contacto")
    print("3- Borrar contacto")
    print("4- Mostrar Agenda")
    print("0- Salir")

selector = int(input("Ingrese un valor de 0 a 4: "))

while(selector > 4 or selector < 0):
    selector = int(input("Error, Ingrese un valor de 0 a 4 "))


def crearContacto(agenda: dict):
    nombre = input("Ingrese el nombre: ")
    if nombre in agenda:
        print("El contacto ya existe")
    else:
        numero = input("Ingrese el numero de telefono: ")
        agenda[nombre] = numero
        print("El contacto fue agregado exitosamente")
    
    
def modificarContacto(agenda: dict)-> None:
    nombre = input("Ingrese el nombre: ")
    if nombre in agenda:
        nombre = input("Ingrese el nuevo nombre: ")
        numero = input("Ingrese el numero de telefono: ")
        agenda[nombre] = numero
        print("El contacto fue modificado exitosamente")
    else:
        print("El contacto no existe")

def eliminarContacto(agenda: dict):
    nombre = input("Ingrese el nombre: ")
    if nombre in agenda:
        agenda.pop(nombre)
        print("El contacto fue eliminado correctamente")
    else:
       print("El contacto no existe")

def mostrarAgenda(agenda:dict):
    pass

def principal():
    agenda = {}
    ingreso = menu()
    while ingreso!=0:
        if ingreso == 1:
            crearContacto(agenda)
        elif ingreso == 2:
            modificarContacto(agenda)
        elif ingreso == 3:
            eliminarContacto(agenda)
        elif ingreso == 4:
            mostrarAgenda(agenda)
    ingreso = menu()



print("Saludos")
    


    
    