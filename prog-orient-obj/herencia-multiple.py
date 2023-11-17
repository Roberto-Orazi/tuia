class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        print(f'Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}') #aca llama a la clase actual
        #PODEMOS LLAMARLO COMO f'{super().mostrar_habilidad()}'

'''
PARA LLAMAR A LA CLASE PADRE SE USA SUPER()
PORQUE PUEDE HABER CAMBIOS EN UN FUTURO
'''

roberto = EmpleadoArtista('Roberto',43,'argentino','cantar','yamaha', 10000)

roberto.presentarse()

herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
#SI DEVUELVE TRUE ES SUBCLASE de empleado artista
#Ya que empleado artista tiene 2 subclases
noherencia = issubclass(Artista,Persona)
#NOS DEVUELVE FALSE YA QUE ARTISTA Y PERSONA SON CLASES SEPARADAS

instancia = isinstance(roberto, EmpleadoArtista)
print(instancia)# es True
#ROBERTO ES UN OBJETO DE LA CLASE EMPLEADOARTISTA, ya que hereda todo de artista y persona
# osea que es objeto de clase artista y persona

