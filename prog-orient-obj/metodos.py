#Creamos una clase pero va sin ()
class Celular:
    def __init__(self, marca, modelo, camara):
        #init es un metodo constructor que define las propiedades iniciales de un objeto
        self.marca = 'Tu telefono es de:' + ' ' + marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular('Samsung', 'S23', '48MP')
celular2 = Celular('Apple', 'Iphone 15', '24MP')

celular1.cortar()
celular2.llamar()
