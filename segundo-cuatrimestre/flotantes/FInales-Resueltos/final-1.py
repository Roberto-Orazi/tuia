from typing import Any


def recursiva(num: int) -> str:
    if num == 0:
        return "0"

    digito = num % 10
    resto = recursiva(num // 10)
    print(digito)
    print(resto)
    return str(resto) + str(digito)

recursiva(1155)

class Entidad():
    def __init__(self,vida_inicial)->None:
        self.vida=vida_inicial

class Enemigo(Entidad):
    pass

class Jugador(Entidad):
    def __init__(self,vida_inicial)->None:
        super().__init__(vida_inicial)
        self.enemigos_golpeados = []

    def Golpeado(self,cuanto):
        self.vida-=cuanto

    def Golpear(self,enemigo,cuanto):
        self.enemigo.vida-=cuanto
        self.enemigos_golpeados.append(enemigo)


class Pila:
    def __init__(self)->None:
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if self.isEmpty():
            print('La pila esta vacia')
            return

        return self.items.pop

    def isEmpty(self) -> bool:
        return (self.items == [])

    def size(self) -> int:
        return len(self.items)

    def top(self) -> Any:
        if self.isEmpty():
            print('La pila está vacía')
            return None
        return self.items[-1]

class PilaConDecantar(Pila):
    def decantar(self):
        if self.size() < 2:
            print("No hay suficientes elementos para decantar.")
            return

        self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

pila = PilaConDecantar()
pila.push(1)
pila.push(2)

print("Pila antes de decantar:", pila.items)
pila.decantar()
print("Pila después de decantar:", pila.items)