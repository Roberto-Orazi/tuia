class Diccionarioo:
    def verificar_palabra(self,palabra):
        #LOGICA PARA VERIFICAR PALABRAS
        pass

class CorrectorOrtograficoo:
    def __init__(self):
        self.diccionario=Diccionario()

    def corregir_texto(self,texto):
        #usamos el diccionario para corregir el texto
        pass

#TODOO ESTO VIOLA ESTE PRINCIPIO YA QUE CORRECTOR DEPENDE DE DICCIONARIO

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        #logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador=verificador

    def corregir_texto(self,texto):
        # usamos el verificador para corregir texto

corrector=CorrectorOrtografico(Diccionario())
