class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre}, esta estudiando ", )

Estudiante1 = Estudiante('Juan',25,2)
Estudiante1.estudiar()
