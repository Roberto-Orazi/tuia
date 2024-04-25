## Paradigma orientado a objetos
Los programas se componen de definiciones de objetos y definiciones de funciones.
Cada definicion de objeto se corresponde con algun objeto o concepto del mundo real.
Las funciones que operan en dicho objeto se corresponden con alguna interaccion entre objetos en el mundo real.

## Programacion Orientada a Objetos
Se piensan los problemas como:
Un conjunto de objetos
Los objetos nos permiten agrupar un conjunto de variables y funciones relacionadas en un mismo espacio de nombres.

Un objeto tiene ciertas caracteristicas, que se le llaman atributos.

Cada objeto tiene un comportamiento que lo distintue, que seria como una funcion del objeto y se le llama metodo.

Ejemplo:
Un gato es el objeto, el tamaño o color de pelo serian sus atributos y maullar o caminar serian los metodos.

Definicion: Un objeto es un ente que consta de identidad, estado y de un comportamiento.

Las instancias son los objetos ya creados osea llamar una clase con parametros.

```
class Gato:
  def __init__(self, nombre, color, raza):  # Constructor de la clase
    self.nombre = nombre  # Atributo "nombre"
    self.color = color  # Atributo "color"
    self.raza = raza  # Atributo "raza"

  def maullar(self):  # Método "maullar"
    print(f"El gato {self.nombre} maúlla")

  def caminar(self):  # Método "caminar"
    print(f"El gato {self.nombre} camina")

gato1 = Gato("Michi", "negro", "siamés")  # Instancia "gato1"
gato2 = Gato("Pelusa", "blanco", "persa")  # Instancia "gato2"

gato1.maullar()  # Llamada al método "maullar" de la instancia "gato1"
gato2.caminar()  # Llamada al método "caminar" de la instancia "gato2"
```
### Atributos de clase y instancia
- Los atributos de clase(variables de clase) son compartidos por todas las instancias de la clase
- Los atributos de instancia(variables de instancia) son particulares para cada objeto creado con esa clase
```
class Animal:
  especie = "mamífero"  # Atributo de clase (compartido por todos los animales)

  def __init__(self, nombre):
    self.nombre = nombre  # Atributo de instancia (único para cada animal)

gato1 = Animal("Michi")
gato2 = Animal("Pelusa")

print(gato1.especie)  # Imprime "mamífero"
print(gato2.especie)  # Imprime "mamífero"

print(gato1.nombre)  # Imprime "Michi"
print(gato2.nombre)  # Imprime "Pelusa"
```
### Herencia
La herencia es la habilidad de definir una nueva clase, que es una version modificada de una clase ya existente.

La clase existentse se le llama clase padre y la nueva se llama clase hija o subclase

## Igualdad e identidad
El operador de igualdad (==) que compara los valroes de ambos objetos.
El operador de identidad(is) decide si ambos se refiern al mismo objeto(si esta en el mismo lugar en memoria).

