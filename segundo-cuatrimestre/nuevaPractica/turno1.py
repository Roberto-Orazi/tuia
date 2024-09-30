# Programacion 2 (TUIA)
# Examen 1 - Turno 1
# 24/09/2024

# COMPLETAR
# Nombre, Apellido
# DNI

# Ejercicio 1: Defina la siguiente funcion en forma recursiva.
from typing import List
def enumerar(lista: List[str]) -> str:
    """
    Recibe una lista de cadenas y devuelve una cadena con los elementos
    de la lista separados por coma y finalizados por punto."""


    if not lista:
        return ''
    elif len(lista) == 1:
        return lista[0] + '.'
    else:
        return lista[0] + ', ' + enumerar(lista[1:]) + '.'
    
#Ejemplos:
print(enumerar([]))

print(enumerar(['Hola']))
#'Hola.'

print(enumerar(['Hola', 'Chau']))
#'Hola, Chau.'

print(enumerar(['Hola', 'Chau', 'Adios']))
#'Hola, Chau, Adios.'


# Ejercicio 2: Defina la clase Pila.


class Pila:
    def __init__(self) -> None:
        """ Inicializo la Pila"""
        self.elementos = []

    def push(self, elemento: int) -> None:
        """ Agrego los elementos a la pila"""
        self.elementos.append(elemento)

    def pop(self) -> int:
        """ Elimino y devuelvo elementos de la pila"""
        if not self.elementos:
            print("Pila vacía")
            return None
        return self.elementos.pop()

    def __str__(self) -> str:
        """ Metodo para poder imprimir como string los valores de la pila """
        return str(self.elementos)
    ...

# Ejercicio 3: Defina una clase Caja que represente una caja registradora.
# Asegurese de mantener en su representacion interna la cantidad de
# billetes de cada denominacion.
"""class Caja:
    def __init__(self) -> None:
        ...

    def agregar(self, billete: int, cantidad: int) -> None:
        Agrega a la caja la cantidad de billetes indicada
        de una determinada denominacion.

    def total(self) -> int:
        Devuelve el importe total almacenado en la caja.

    def __str__(self, other) -> str:
        Representa el contenido de la caja de la siguiente manera:
        Cantidad de billetes de $10: XXX.
        Cantidad de billetes de $20: XXX.
        Cantidad de billetes de $50: XXX.
        Cantidad de billetes de $100: XXX.
        Cantidad de billetes de $500: XXX.
        Cantidad de billetes de $1000: XXX.
        Cantidad de billetes de $2000: XXX.
        Cantidad de billetes de $10000: XXX.
        Total: $XXX.
        """

class Caja:
    def __init__(self) -> None:
        """ Inicializo la caja registradora"""
        self.billetes = {
            10: 0,
            20: 0,
            50: 0,
            100: 0,
            500: 0,
            1000: 0,
            2000: 0,
            10000: 0
        }

    def agregar(self, billete: int, cantidad: int) -> None:
        """Agrega a la caja la cantidad de billetes indicada de una determinada denominacion."""
        if billete in self.billetes:
            self.billetes[billete] += cantidad
        else:
            print("Denominación de billete no válida")

    def total(self) -> int:
        """Devuelve el importe total almacenado en la caja."""
        return sum(billete * cantidad for billete, cantidad in self.billetes.items())

    def __str__(self) -> None:
        """Muestra el contenido de la caja sin usar join()."""
        for billete, cantidad in self.billetes.items():
            print(f"Cantidad de billetes de ${billete}: {cantidad}.")
        
        print(f"Total: ${self.total()}.")

# Prueba
caja = Caja()
caja.agregar(10, 5)
caja.agregar(20, 3)
caja.agregar(50, 2)

# Llamamos a mostrar para visualizar el contenido
caja.__str__()
