# SE INGRESA SABOR DE HELADO Y CANTIDAD DE HELADO


sabores = []
cantidades = []
def ingresar_ventas():
    siga = True
    while siga == True:    
        sabor = input("Ingrese sabor de helado vendido: ")
        while sabor not in sabores:
            sabores.append(sabor)
            cant = int(input("Ingrese cantidad del sabor vendido: "))
            cantidades.append(cant)
            otro = input("Ingresa otra venta? si/no ")
            if otro == "si":
                continue
            else:
                siga = False
    else:
        print("Gusto ya registrado")
cantidad_vendida = tuple(cantidades)
ingresar_ventas()
ventas = {}
def calcular_total_ventas(precio = 2000):
    for i in range(len(sabores)):
        ventas[sabores[i]] = cantidades[i]*precio
    return ventas
calcular_total_ventas()


def determinar_sabor_mas_vendido(ventas):
    mayorCant = cantidades[0]
    mayorSabor = sabores[0]
    for i in range(len(sabores)):
        if cantidades[i]>mayorCant:
            mayorCant = cantidades[i]
            mayorSabor = sabores[i]
    return "El sabor mas vendido fue:", mayorSabor, "y se vendio", mayorCant



print(ventas)
print(sabores)
print(cantidades)
print (determinar_sabor_mas_vendido(ventas))  