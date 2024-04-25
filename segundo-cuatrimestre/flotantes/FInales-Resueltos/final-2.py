def calcular(a, b):
    if a == 0:
        return b + 1
    if b == 0:
        return calcular(a - 1, 1)

    intermedio = calcular(a, b - 1)
    return calcular(a - 1, intermedio)


valor=calcular(1, 0)
print(valor)

class Cosa:
    def __init__(self,valor):
        self.valor=valor

class Coleccion:
    def __init__(self):
        self.coleccion = []

    def agregar_cosa(self,cosa: Cosa):
        self.coleccion.append(cosa)

    def __str__(self):
        if not self.coleccion:
            return "Colección vacía"
        else:
            return f"Colección: {', '.join(str(cosa.valor) for cosa in self.coleccion)}"

cosa=Cosa('hola')
cosa2=Cosa('mundo')
coleccion=Coleccion()
coleccion.agregar_cosa(cosa)
coleccion.agregar_cosa(cosa2)

print(coleccion)


