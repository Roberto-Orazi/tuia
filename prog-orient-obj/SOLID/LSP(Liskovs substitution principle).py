class Ave:
    def volar(self):
        return 'Estoy volando'

class Pinguino(Ave):
    def volar(self):
        return 'No puedo volar' #EL PINGUINO DEBERIA DE PODER HACER TODO LO QUE HACE UN AVE

def hacer_volar(ave=Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))
#COMO DEBERIA DE SER SEGUN LISKOVS
class Avee: #ACA DEFINIMOS LO QUE TODAS LAS AVES PUEDEN HACER
    pass

class AveVoladora(Avee): # Y DESPUES EN SUBCLASES SOMOS MAS ESPECIFICOS HACIA ESAS SUBCLASES
    def volar(self):
        return 'Estoy volando'

class AveNoVoladora(Avee):
    pass



