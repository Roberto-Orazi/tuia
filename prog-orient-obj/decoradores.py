def decorador(funcion): #RECORDAR QUE SON COMO LOS CALLBACKS DE JS
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

'''
def saludo():
    print("Hola mundo")

saludo_modificado = decorador(saludo)
saludo_modificado()
'''

@decorador #ESTO ES STANDAR/BUENA PRACTICA
def saludo():
    print("Hola mundo estamos en la funcion")

saludo()
