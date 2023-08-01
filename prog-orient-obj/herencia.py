class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

    #def hablar(self):
    #    print('NO HABLO') SE SOBREESCRIBE LA FUNCION
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas=notas
        self.universidad=universidad

roberto = Empleado('Roberto', 26, 'argentino', 'programador', 2300)

print(roberto.edad)
roberto.hablar()
