class Estudiante:
    def __init__(self, nombre:str, legajo:str) -> None:
        self.nombre=nombre
        self.legajo=legajo

    def obtener_nombre(self):
        return (self.nombre)

    def obtener_legajo(self):
        return (self.legajo)

roberto=Estudiante('roberto', 'o-1815/5')
juan=Estudiante('juan', 'o-1916/6')
legajo=roberto.obtener_legajo()
print(legajo)

class Escuela():
    def __init__(self) -> None:
        self.lista_estudiantes=[]

    def agregar_estudiante(self, estudiante):
        return self.lista_estudiantes.append(estudiante)

    def eliminar_estudiante(self, legajo):
        for estudiante in self.lista_estudiantes:
            if legajo == estudiante.obtener_legajo():
                self.lista_estudiantes.remove(estudiante)
                return
            else:
                print('El estudiante no esta anotado en la escuela')

    def buscar_estudiante(self, legajo):
        for estudiante in self.lista_estudiantes:
            if legajo == estudiante.obtener_legajo():
                print('true')
            else:
                print('false')

unr=Escuela()
unr.agregar_estudiante(roberto)
unr.agregar_estudiante(juan)

print(len(unr.lista_estudiantes))

unr.buscar_estudiante('o-1916/6')

unr.eliminar_estudiante('o-1916/6')

unr.buscar_estudiante('o-1916/6')

print(len(unr.lista_estudiantes))

