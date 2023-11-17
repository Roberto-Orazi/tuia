#Creamos una clase pero va sin ()
class Celular:
   def __init__(self, marca, modelo, camara):
    #self hace referencia a si mismo
    #__init__ ES UN METODO CONSTRUCTOR
    self.marca = 'Tu telefono es de:' + ' ' + marca
    self.modelo = modelo
    self.camara = camara

#En definitiva las propiedades son cualidades/atributos de un objeto
#Un objeto puede tener una accion, por lo cual usamos metodos
celular1 = Celular('Samsung', 'S23', '48MP')
print(celular1.marca)
print(celular1.modelo)
print(celular1.camara)

celular2 = Celular('Apple', 'Iphone 15', '24MP')
print(celular2.marca)
print(celular2.modelo)
print(celular2.camara)
