class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self._edad=edad
    @property
    def nombre(self):
        return self.__nombre #ESTA FUNCION ES UN GETTER

    @nombre.setter
    def nombre(self,new_nombre):
       self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

roberto=Persona('Roberto', 21)
nombre=roberto.nombre
#COMO USAMOS LA PROPIEDAD PROPERTY LO HICIMOS PROPIEDAD
#A GETNOMBRE EN VEZ DE UNA FUNCION()
print(nombre)

roberto.nombre='Rober'
del roberto.nombre #ESTO PROVOCA UN ERROR EN LA LINEA 7 YA QUE ME ELIMINA TODO EL SELF
nombre=roberto.nombre
print(nombre)
