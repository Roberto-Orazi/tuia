class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Mamifero(Animal):
    def amamantando(self):
        print("El animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass

murcielago=Murcielago()

murcielago.comer()
murcielago.amamantando()
murcielago.volar()

print(Murcielago.mro())