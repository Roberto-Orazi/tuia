#Crear el constructor de la clase 'Provincia'
#Crear un objeto de la clase 'Provincia'

class Provincia:
  """
  Esta clase representa una provincia.
  Atributos:
    nombre: str
    coordenada: tuple
  """
  def __init__(self
               , nombre: str
               , coordenada: tuple):
    self.nombre = ""
    self.coordenada = (0,0)
    pass

  def __str__(self):
    return f"Provincia: {self.nombre} - Coordenada: {self.coordenada}"
    pass