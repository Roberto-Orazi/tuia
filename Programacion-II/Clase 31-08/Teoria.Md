# PROGRAMACION ORIENTADA A OBJETOS

## PARADIGMA IMPERATIVO

- En el paradigma imperativo, los programas se construyen como una serie de ordenes o instrucciones concretas

- Es un estilo imperativo lo que hacemos es pensar paso a paso que es lo que queremos que nuestro programa haga

- La computacion se lleva a cabo mediante el concepto de estado, que es la coleccion de variables y sus valores en el
  momento dado. Las instrucciones describen como alterar el estado

- Lenguajes imperativos: FORTRAN(Formula transformation), C, C++

## PARADIGMA ORIENTADO A OBJETOS

- Es una evolucion del paradigma imperativo

- Los programadores pensamos los programas como una serie de objetos que interactuan unos con otros

- La computacion tambien se lleva a cabo mediante el estado, pero la diferencia es que, ademas del estado global, cada
  objeto tiene un estado propio

- Algunos lenguajes orientados a objetos son: Java, C#, JS

```
# PUEDE SER IMPERATIVO
my_list=[1,2,3,4,5]
sum=0
for x in my_list:
    square=x*x
    doble=2*square
    sum+=doble
print(sum)
```

```
class Mylist():
    def __init__(self,any_list):
        self.any_list=any_list

    def square(self):
        return[x*x for x in self.any_list]

    def doble(self):
        return[2*x for x in self.square()]

    def sum(self):
        return sum(self.doble())
my_list=Mylist([1,2,3,4,5])
print(my_list,sum())
```

```
Python es multiparadigma, combina propiedades de distintos lenguajes de programacion
Lo podemos usar con distintos estilos y usar distintos estilos segun sea lo mas apropiado para cada problema
Incluso podemos mezclar estilos dentro del mismo programa, pero debemos intentar siempre que el resultado sea un programa claro, limpio y legible
```

# OBJETOS

1. Un objeto es un ente que constra de identidad, estado, y de un comportamiento

2. Una clase es una plantilla para la creacion de nuevos objetos

### Caracteristicas:

- Las clases nos permiten modularizar los datos y la funcionalidad asociada a un tipo de objeto

- Al definir una clase debemos definir que atributos y que metodos contendran los objetos pertenecientes a esta clase

- Cuando un objeto pertenezca a una clase, diremos que ese objeto es una instancia de la clase


#### Hasta ahora trabajamos con clases y objetos sin saberlo por los tipos de datos integrados(Como int list, etc)

#### COMO DEFINIR UNA CLASE:
```
class Point:
    '''
    representacion de un punto en un plano cartesiano 2D
    '''
    def __init__(self, x: float, y: float)->none:
        self.x=x
        self.y=y

    def __str__(self)->str:
        return( '(' + str(self.x) + ',' + str(self.y) + ')' )

#Podemos crear objetos pertenecientes a la clase del siguiente modo:
A=Point(3,4)
B=Point(1,2)
x e y son atributos del objeto, y decimos que el atributo x del objeto referenciado en la variable A posee el valor 3,4.
```


#### ATRIBUTOS DE CLASE

- Los atributos de clase son compartidos por todas las instancias de la clase(Siempre los mismos para todos los objetos)

#### ATRIBUTOS DE INSTANCIA

- Los atributos de instancia son particulares para cada objeto creado con esa clase(Cambian de objeto a objeto)

```
#Ejemplo:
class Silla:
    cantidad_de_patas=4
    def __init__(self):
        self.color='marron'
```

# DEBE EVITARSE EL USO DE ATRIBUTOS DE CLASE, EXCEPTO PARA DEFINIR CONSTANTES

### IGUALDAD E IDENTIDAD

```
p1=Point(3,4)
p2=Point(3,4)
p1 is p2
# va a retornar false
p1=p2
p1 is p2
# va a retornar true ya que a p1 le estoy asignando p2
#Igualdad p1==p2
#Identidad p1 is p2
```

```
class Point:
    def __init__(self, x: float, y: float)->none:
        self.x=x
        self.y=y
    def __eq__(self, other:'Point')-> Bool:
        return(self.x==other.x and self.y==other.y)
```
