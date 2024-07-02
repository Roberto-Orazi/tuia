class Libro:
    def __init__(self,autor,titulo) -> None:
        self.autor=autor
        self.titulo=titulo

    def obtener_autor(self):
        return str(self.autor)

    def obtener_titulo(self):
        return str(self.titulo)


class Biblioteca:
    def __init__(self) -> None:
        self.coleccion=[]

    def agregar_libro(self, libro:Libro):
        return self.coleccion.append(libro)

    def sacar_libro(self, autor, titulo):
        for libro in self.coleccion:
            if libro.autor == autor and libro.titulo == titulo:
                self.coleccion.remove(libro)
                return f'El libro "{titulo}" de {autor} ha sido retirado de la biblioteca'
        return 'El libro no se encuentra en la librería'

    def contiene_libro(self, autor, titulo)->bool:
        for libro in self.coleccion:
            if libro.autor == autor and libro.titulo == titulo:
                    return True
            else:
                return False


libro=Libro('roberto', 'tito')
libro1=Libro('roberto2', 'tito2')

libreria1=Biblioteca()

libreria1.agregar_libro(libro)
libreria1.agregar_libro(libro1)
valorFalse=libreria1.contiene_libro('roerto', 'tit')
print('libro inexistente',valorFalse)

valorTrue=libreria1.contiene_libro('roberto', 'tito')
print('libro existente',valorTrue)


libreria1.sacar_libro('roberto','tito')

valorFalseLuego=libreria1.contiene_libro('roberto', 'tito')
print('libro inexistente luego de sacarlo',valorFalseLuego)

libreria1.sacar_libro('roberto2','tito')

valorFalseLuego=libreria1.contiene_libro('roberto2', 'tito2')
print('libro existente luego de sacarlo con valores errados',valorFalseLuego)