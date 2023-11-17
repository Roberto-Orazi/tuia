# PROGRAMACION ORIENTADA A OBJETOS

## PARADIGMA IMPERATIVO

- En el paradigma inmperativo, los programas se construyen como una serie de ordenes o instrucciones correctas

## PARADIGMA ORIENTADO A OBJETOS

- La programcion orientada a objetos es una evolucion de lparadigma imperativo.
- Pensamos los programas como objetos que interactuan unos con otros
- La computacion tambien se lleva a cabo mediante el estado, osea tenemos el global y el estado del objeto
- Otros lenguajes oo son java, c # y js

````
class Mylist():
    def __init__(self, any_list):
        self.any_list = any_list

    def square(self):
        return[x * x for x in self.any_list]

    def doble(self):
        return[2*x for x in self.square()]

    def sum(self):
        return sum(self.double())

my_list = my_list([1,2,3,4,5])
print(my_list.sum())
````

### Por ejemplo, un programa imperativo podria ser:
````
nombrePerro = 'Juan'
nombreGato = 'Carlo'
edadPerro = 1
edadGato = 2
````

### Tambien podemos tener algo asi:
````
perro.nombre = 'Juan'
perro.edad = 12
perro.calcularEdad()

gato.nombre = 'Jose'
gato.edad = 12
gato.calcularEdad()
````
Agrupamos las variables y las funciones.

## IMPORTANTE
### Un objeto tiene:
- ## Identidad:
   ### Es lo que lo diferencia del resto
- ## Estado
    ### Son las caracteristicas/propiedades
- ## Comportamiento:
    ### El comportamiento me lo da los metodos, serian las acciones/funciones

````
class Cat:
    def __init__(
        self,
        name,
        weight,
        owner,
        sex,
        hairColor
    )
    self.name = name
    self.weight
    self.owner = owner
    self.sex = sex
    self.hairColor = hairColor

    def meow(self):
        print(f"(self.name) says 'meow'")
    def play(self, toy):
        print(f"(self.name) says 'toy'")
````

## EN PYTHON
### El estado esta dado por los atributos o variables

### El comportamiento del objeto esta dado por los metodos que modifican el estado

## Instannciacion
````
Llamamos instanciacion al proceso de crear nuevos objetos en base a su clase
````

## Composicion

````
Como una clase define un nuevo tipo de datos, nada impide usar est enuevo tipo de datos como tipo de uno de los atributos de otra clase.
````

