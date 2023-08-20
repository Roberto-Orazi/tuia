#IMPLEMENTACION: IMPLEMENTAR UN METODO SERIA DEFINIR COMO VA A FUNCIONAR
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengoo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

robikings = Estudiante("Roberto", 25, "Masculino", "programacion")
roberto = Trabajador("Roberto", 26, "Masculino", "Programador")

robikings.presentarse()
robikings.hacer_actividad()
roberto.presentarse()
roberto.hacer_actividad()