# Programacion Orientada a Objetos

- Los paradigmas de programacion son diferentes estilos de construir programas

- Al momento de diseñar un lenguaje de programacion, se incluyen construcciones, osea son elementos, caracteristas o
  estructuras que se incorporan para facilitar los estilos.

- Dependiendo de las construcciones los programas siguen uno u otro estilo de programacion.

## Paradigma imperativo
- Los programas se construyen como una serie de ordenes o instrucciones concretas.

- Pensamos paso a paso que es lo que queremos que el programa haga.

- La computacion se lleva a cabo mediante el estado, es la coleccion de variables y sus valores actuales en un momento
  dado. Y la instrucciones describen como alterar el estado.

- Fortran, C o C ++

## Paradigma orientado a objetos
- Es una evolucion del paradigma imperativo.

- Los programas se piensan como una serie de objetos que interactuan con otros.

- A diferencia del imperativo ademas del estado global cada objeto tiene uno propio.

- Java, C#, JS

## PYTHON
- Python es multiparadigma, combina propiedades de distintos lenguajes de programacion.
- Podemos usarlo con distinto estilos segun el problema a resolver
- Podemos mezclar distintos estilos, pero debemos intentar de que el resultado sea un programa claro limpio y legible.

## Programacion orientada a objetos

La idea de un objeto es:
  1. Representar una entidad de la vida real.
  2. Agrupar todas las variables y funciones asociadas con la misma entidad real.


Ejemplo de algo cotidiano, pensado como un objeto un GATO Podemos decir:
- cual es su tamaño
- color de pelo
- mestizaje
ESTOS SON SUS ATRIBUTOS

Despues los objetos tienen comportamientos:
- Maullar
- Arañar
- Trepar
ESTOS SON LOS METODOS.
Que en nuestro caso van a ser comportamientos o funcionalidades.

## OBJETOS

Un objeto es un ente que consta de:
- Identidad
- Estado
- Comportamiento

Una clase es una plantilla para la creacion de nuevos objetos


- Las clases nos permiten modularizar objetos y la funcionalidad asociada a un tipo de objeto
- Al definir una clase tenemos que definir que atributos y que metodos contienen los objetos pertenecientes a esta
  clase.
- Cuando un objeto pertenezca a una clase, diremos que ese objeto es una instancia de la clase.

Por ejemplo:
Los datos integrados de python como int, list, etc estan implementados como clases, y sus instancias son
objetos.

Como definir un tipo de dato creado
```
class Point:
  '''
    Representacion de un punto en un plano cartesiano 2D
  '''
  def __init__(self, x: float, y: float)->None:
    self.x=x
    self.y=y

  def __str__(self)"-> str:
    return('('str(self.x)+','+str(self.y)')')

```
Podemos crear objetos a la clase:
A = Point(3,4)
B = Point(1,2)
Nosotros en el momento que le asignamos a A la clase Point estamos creando el objeto A

Cuando creamos el objeto pasa lo siguiente:
1. Se crea una nueva instancia de la clase point
2. Se ejecuta el constructor init con self hacia la nueva instancia x:3, y:4
3. El constructor asigna los atributos de self.x y self.y
4. Cuando termina el constructor se asigna el punto a la instancia de point creada.
5. El metodo str devuelve la representacion en string del objeto creado


Podemos cambiar los valores de los atributos de una instancia creada:
A.x = 10 ESTO ES PORQUE LOS OBJETOS SON MUTABLES
B.y=5

x e y son los atributos del objeto A en este caso.



## Atributos
En python hay 2 tipos de atributos, de clase y de instancia
### De clase
Son compartidos por todas las instancias de la clase

### De instancia
Son particulares para cada objeto creado con esa clase

Por ejemplo, los 2 atributos de la clase Point son de instancia, ya que representan coordenadas que varian segun el punto que representamos.

SE EVITA EL USO DE ATRIBUTOS DE CLASE EXCEPTO PARA DEFINIR CONSTANTES

## Igualdad e Identidad
El significado de igual y mismo parece perfectamente claro pero contiene sutilezas propias del lenguaje natural.

Por ejemplo cuando dicen que juan tiene un auto igual al mio, seguramente signifique que ambos autos son del mismo fabricante y modelo pero que son dos autos diferentes.

Sin embargo si alguien dice que juan y yo tenemos el mismo profesor, seguramente sea la misma persona, no a que dos personas son iguales.

Por eso cuando hablamos de objetos hay una ambiguedad parecida. Si dos objetos de tipo Point son iguales nos referimos a que tienen los mismo atributos o que son realmente el mismo objeto

Por eso en python se diferencia entre igualdad e identidad

- El operador igualdad == es de comparacion de valores de ambos objetos

- El operador identidad is decide si ambos se refieren al mismo objeto(Osea que estan en el mismo lugar en memoria)

```
p1=Point(3,4)
p2=Point(3,4)
p1 is p2
False
```
Aunque p1 y p2 contengan los mismo atributos no son el mismo objeto.
En cambio si le asignamos p2 a p1 entonces las 2 variables son alias para el mismo objeto

```
p1=p2
p1 is p2
True
```
Para comprobar si dos objetos son iguales en terminos de que contengan los mismos atributos podemos usar el operador == utilizando el metodo eq en la definicion de la clase.

```
def __eq__(self, other: 'Point')-> bool:
  return(
    self.x == other.x and self.y == other.y
    )
```
Una vez definido podemos hacer:
```
p1=Point(3,4)
p2=Point(3,4)
p1==p2
True
```

## FUNCIONES PURAS VS MODIFICADORAS

### PURAS
No modifican ningunn objeto pasado a las mismas


### MODIFICADORAS
Realizan cambios en los objetos pasados a las mismas


## METODOS
Lo principal de POO es agrupar la declaracion de variables(atributos) y de funciones relacionadas(Metodos)

Metodos build-in utilizados a diario son .key() y .values() en diccionarios

Cada metodo esta asociado a una clase y pueden ser invocados en instancias de esa clase.
Son parecidos a las funciones excepto por:
1. Son definidos dentro de una definicion de clase para hacer la relacion entre ambos explicita.
2. La sintaxis para invocar al metodo es diferente.

## HERENCIA

La herencia permite añadir nuevos metodos a una clase sin modificar la clase ya existente.
Se llama herencia porque la nueva clase hereda todos los metodos de la clase existente.
La clase existente se llama clase padre y la nueva clase hija o subclase.
