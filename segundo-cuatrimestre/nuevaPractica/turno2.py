# Programacion 2 (TUIA)
# Examen 1 - Turno 2
# 24/09/2024

# COMPLETAR
# Nombre, Apellido
# DNI

# Ejercicio 1: Defina la siguiente funcion en forma recursiva.
def aplanar(lista: list[list[int]]) -> list[int]:
    """
    Recibe una lista de lista de enteros y devuelve una unica lista con
    el contenido de todas.

    Ejemplos:
    >>> aplanar([])
    []

    >>> aplanar([[1]])
    [1]

    >>> aplanar([[1], [2]])
    [1, 2]

    >>> aplanar([[1], [2], [3, 4]])
    [1, 2, 3, 4]
    """

# Ejercicio 2: Defina la clase Cola.
class Cola:
    ...

# Ejercicio 3: Defina una clase Caja que represente una caja registradora.
# Asegurese de mantener en su representacion interna la cantidad de
# billetes de cada denominacion.
class Caja:
    def __init__(self) -> None:
        ...

    def agregar(self, billete: int, cantidad: int) -> None:
        """Agrega a la caja la cantidad de billetes indicada
        de una determinada denominacion."""

    def total(self) -> int:
        """Devuelve el importe total almacenado en la caja."""

    def __add__(self, other) -> "Caja":
        """Dadas dos cajas, devuelve una nueva con el contenido de ambas."""
