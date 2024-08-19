class Estudiante:
    def __init__(self, legajo: str, nombre: str) -> None:
        self.legajo=legajo
        self.nombre=nombre

    def obtener_legajo(self):
        return self.legajo

    def obtener_nombre(self):
        return self.nombre

class Escuela:
    def __init__(self) -> None :
        self.estudiantes=[]

    def agregar_estudiante(self, estudiante: Estudiante):
        return self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, legajo: str):
        for estudiante in self.estudiantes:
            if legajo == estudiante.legajo:
                self.estudiantes.remove(estudiante)

    def buscar_estudiante(self, legajo: str):
        for estudiante in self.estudiantes:
            return legajo == estudiante.legajo

roberto=Estudiante('123','roberto')
carlos=Estudiante('456','carlos')
juan=Estudiante('789','juan')

unr=Escuela()

unr.agregar_estudiante(roberto)
unr.agregar_estudiante(carlos)
unr.agregar_estudiante(juan)

print('estudiante legajo 789', unr.buscar_estudiante('123'))

print('Eliminamos estudiante con legajo 789', unr.eliminar_estudiante('123'))

print('estudiante legajo 789', unr.buscar_estudiante('123'))


