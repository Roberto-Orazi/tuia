class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre}, esta estudiando ", )

nombre=input('Ingrese su nombre: ')
edad=input('Ingrese su edad: ')
grado=input('Ingrese su grado: ')

estudiante=Estudiante(nombre,edad,grado)
print(
    f"""
    El estudiante se llama {estudiante.nombre},
    tiene {estudiante.edad} años y esta
    cursando el {estudiante.grado} año de ingenieria
    """
)
while True:
    estudiar = input('Ingrese estudiar: ')
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()
