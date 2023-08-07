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




