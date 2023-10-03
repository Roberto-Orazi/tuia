#ENCAPSULADOS:
#SE USA PARA OCULTAR ALGUNAS COSAS Y PROTEGERLOS
#ES PARA MEJORAR LEGIBILIDAD DEL CODIGO

class MiClase:
    def __init__(self):
        self.atributo='Valor' #ESTO ES PUBLICO
        self._atributo_privado='Valor' #ESTO ES PROTEGIDO/PRIVADO
        self.__atributo_muy_privado='Valor' #ESTO ES SUPERPRIVADO

objeto=MiClase()
print(objeto._atributo_privado) #ESTO ES PROTEGIDO
#print(objeto.__atributo_privado) ES SUPER PRIVADO Y TIRA ERROR PORQUE HAY QUE ACCEDER DE OTRA MANERA

#SE ACCEDE CON SETTERS Y GETTERS, QUE SON METODOS DE ENCAPSULADO
class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad

    def get_nombre(self):
        return self._nombre #ESTA FUNCION ES UN GETTER

    def set_nombre(self,new_nombre):
        self._nombre=new_nombre #ESTA FUNCION ES UN SETTER

roberto=Persona('Roberto', 21)
nombre=roberto.get_nombre()
print(nombre)

roberto.set_nombre('rober')
roberto._nombre='Robert' # de esta forma NO cambia el nombre si es suepr privado
nombre=roberto.get_nombre()
print(nombre)


