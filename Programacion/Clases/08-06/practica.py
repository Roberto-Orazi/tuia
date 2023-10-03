'''
Calculadora de Gastos Supongamos que deseas crear un programa para llevar el registro de tus gastos mensuales. Para
ello, se te pide que desarrolles un programa modular que realice las siguientes tareas:

1-Permitir al usuario ingresar los diferentes gastos del mes, junto con sus respectivos montos. prioridad 2-Calcular el
total gastado en cada categoría de gasto. 3-Determinar la categoría de gasto que representa el mayor monto gastado y
mostrar dicho monto. 4-Calcular el gasto total del mes. 5-Mostrar un resumen de los gastos en un formato legible para el
usuario. # Tarea 6-Agregar gastos adicionales. prioridad 7-Mostrar gastos individuales.

Para resolver este problema, se pueden utilizar las siguientes estructuras de datos:

-Un diccionario para almacenar las categorías de gasto como claves y las listas de montos correspondientes como valores.
-Una lista para almacenar las categorías de gasto ingresadas por el usuario. -Un bucle para permitir al usuario ingresar
los gastos y montos de manera interactiva. -Condicionales para determinar la categoría con el mayor monto y calcular el
gasto total. -A continuación se muestra un posible esqueleto de la solución. Por favor, completa las funciones con el
código correspondiente:
'''

def ingresarGastos() -> dict:
  """Esta función permite al usuario ingresar los diferentes gastos del mes y sus respectivos montos.
  Devuelve un diccionario con las categorías de gasto como claves y las listas de montos correspondientes como
  valores."""
  '''
  gastos = {} categorias = [] while categorias != "":
    categorias = input("Ingrese una categoría de gasto: ") if categorias != "":
      monto = int(input("Ingrese el monto del gasto: ")) gastos[categorias] = gastos.get(categorias, []) + [monto]
  return gastos
  '''
  gastos = {}
  categorias = input("Ingrese una categoría de gasto: ")
  while categorias != "":
    montos = []
    monto = float(input("Ingrese el monto del gasto: "))
    while monto != 0:
      montos.append(monto)
      monto = float(input("Ingrese el monto del gasto: "))
    gastos[categorias] = montos
    categorias = input("Ingrese una categoría de gasto: ")
  return gastos



def calcularTotalPorCategoria(gastos: dict) -> dict:
#Esta función calcula el total gastado en cada categoría de gasto y devuelve un diccionario con los resultados.
  total_categoria = {}
  for categoria, montos in gastos.items():
    total_categoria[categoria] = sum(montos)
    #print (f"El total gastado en {categoria} es de {total_categoria[categoria]}")
  return total_categoria



def determinarCategoriaMayorMonto(total_categoria:dict) -> tuple[str, int]:
  """Esta función determina la categoría de gasto con el mayor monto y devuelve dicha categoría junto con el monto."""
  categoria_mayor_monto = ""
  mayor_monto = 0
  for categoria, monto in total_categoria.items():
    if monto > mayor_monto:
      mayor_monto = monto
      categoria_mayor_monto = categoria
  #print (f"La categoría con mayor monto es {categoria_mayor_monto} con un monto de {mayor_monto}")
  return categoria_mayor_monto, mayor_monto

def calcularGastoTotal(total_categoria:dict) -> int:
  """Esta función calcula el gasto total del mes sumando los montos de todas las categorías."""
  gasto_total = 0
  for categoria, monto in total_categoria.items():
    gasto_total += monto
  #print (f"El gasto total del mes es de {gasto_total}")
  return gasto_total


def mostrarResumenGastos(total_por_categoria: dict, categoria_mayor_monto: str, mayor_monto: int, gasto_total: int) -> None:
  """
  Esta función muestra un resumen de los gastos en un formato legible para el usuario.
  """
  print(f"El total gastado en cada categoría es: {total_por_categoria}")
  print(f"La categoría con mayor monto es {categoria_mayor_monto} con un monto de {mayor_monto}")
  print(f"El gasto total del mes es de {gasto_total}")



def agregarGastosAdicionales(*args, **kwargs):
    """Esta función permite agregar gastos adicionales al registro existente.
    Puede aceptar argumentos posicionales (*args) para las categorías de gasto adicionales,
    y argumentos de palabra clave (**kwargs) para los montos de cada categoría."""
    for categoria in args:
        monto = float(input(f"Ingrese el monto para la categoría '{categoria}': "))
        if categoria in gastos:
            gastos[categoria].append(monto)
        else:
            gastos[categoria] = [monto]

    for categoria, monto in kwargs.items():
        if categoria in gastos:
            gastos[categoria].append(monto)
        else:
            gastos[categoria] = [monto]


def mostrarGastosIndividuales(*args, **kwargs):
    """Esta función muestra los gastos individuales de cada categoría en un formato legible para el usuario.
    Puede aceptar argumentos posicionales (*args) para las categorías de gasto a mostrar,
    y argumentos de palabra clave (**kwargs) para mostrar categorías adicionales con sus respectivos montos."""
    for categoria in args:
        if categoria in gastos:
            print(f"Gastos individuales de la categoría '{categoria}':")
            for monto in gastos[categoria]:
                print(f"- {monto}")

    for categoria, monto in kwargs.items():
        if categoria in gastos:
            print(f"Gastos individuales de la categoría '{categoria}':")
            for monto in gastos[categoria]:
                print(f"- {monto}")


# Programa principal
gastos = ingresarGastos()
total_categoria = calcularTotalPorCategoria(gastos)
categoria_mayor_monto, mayor_monto = determinarCategoriaMayorMonto(total_categoria)
gasto_total = calcularGastoTotal(total_categoria)
mostrarResumenGastos(total_categoria, categoria_mayor_monto, mayor_monto, gasto_total)
agregarGastosAdicionales("Transporte", "Ocio", Alimentos=200, Entretenimiento=150)
mostrarGastosIndividuales("Alimentos", "Transporte", Otros=50)