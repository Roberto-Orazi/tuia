class Point:
    """
    Representacion de un punto en un plano cartesiano 2D
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)


class Rectangle:
    """
    Representacion de un rectangulo
    """

    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return f"(width: {self.width}, height: {self.height})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return (
            self.width == other.width
            and self.height == other.height
            and self.corner == other.corner
        )

    def move_rectangle(self, dx: float, dy: float) -> "Rectangle":
        return self.corner.x + dx, self.corner.y + dy


def move_rectangle_up(dx: float, dy: float, other: "Rectangle") -> "Rectangle":
    return Rectangle(
        other.width, other.height, Point(other.x + dx, other.y + dy + other.height)
    )


def distancia(point_A: "Point", point_B: "Point") -> float:
    return 1 / 2 * ((point_B.x - point_A.x) ** 2 + (point_B.y - point_A.y) ** 2)


class Automovil:
    def __init__(
        self,
        patente: str,
        marca: str,
        kilometros_recorridos: float = 0,
        litros_nafta: float = 0,
    ) -> None:
        self.patente = patente
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.litros_nafta = litros_nafta

    def avanzar(
        self,
        kms: float,
    ):
        if self.litros_nafta < ((kms / 100) * 8.8):
            return "Nafta insuficiente"
        self.kilometros_recorridos += kms
        self.litros_nafta -= (kms / 100) * 8.8

    def cargar_nafta(self, litros_a_cargar: float) -> None:
        self.litros_nafta += litros_a_cargar


auto = Automovil("AEF-202", "Peugeot")
auto.cargar_nafta(10)
print(auto.kilometros_recorridos)  # Debería mostrar 0
print(auto.litros_nafta)  # Debería mostrar 10
auto.avanzar(50)
print(auto.kilometros_recorridos)  # Debería mostrar 50
print(auto.litros_nafta)  # Debería mostrar 5.6
auto.avanzar(100)  # Debería mostrar un mensaje de error: "nafta insuficiente"
auto.avanzar(40)
print(auto.kilometros_recorridos)  # Debería mostrar 90
print(auto.litros_nafta)


class Robot:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def mueve(self, orden: str):
        if orden == "A":
            self.y += 1
        elif orden == "R":
            self.y -= 1
        elif orden == "D":
            self.x += 1
        elif orden == "I":
            self.x -= 1
        else:
            "Orden invalida"

    def posicion_actual(self):
        return f"Posicion Actual {self.x} - {self.y}"


mi_robot = Robot()
orden = input("Introduce la orden (A, R, D, I) o 'fin' para salir: ").capitalize()

while orden != "FIN":
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden (A, R, D, I) o 'fin' para salir: ").capitalize()

print("Fin del programa")


class RobotMejorado(Robot):
    def __init__(self, movimientos: str = ""):
        self.movimientos = movimientos
