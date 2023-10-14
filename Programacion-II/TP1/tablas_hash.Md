# Tablas HASH
Muchas aplicaciones requieren trabajar con 3 operaciones basicas:
1. Insertar
2. Buscar
3. Eliminar

Ejemplos:
## Agenda Telefonica
- El usuario encuentra numeros de telefono a partir del nombre de pila de la persona a quien quiere llamar.
- Se puede añadir nuevos contactos ingresando el nombre(id) y el numero de telefono
- Tambien se puede elminar los contactos.

## Sistema de cache de un navegador
A traves del cache el navegador guarda las respuestas que reicibio de determinados pedidos, por ejemplo los https
requests a distintos servidores. Podemos pensar que el cache del navegador guardara la url de los recursos juntos con su
contenido, por ejemplo una imagen. El navegador al tiempo borra la entrada en el cache asociada a la url.

Ademas de las 3 operaciones basicas ya mencionadas, tienen en comun otra cuestion, necesidad de usar claves y valores.

La operacion de busqueda:
- Busca algo por su clave(nombre de pila o url) y obtiene su valor asociado(el numero de telefono o imagen)

Estas aplicaciones son ejemplos de lo que en ciencias de la computacion se conoce como diccionarios.


## Diccionario
Es un conjunto dinamico que admite las tres operaciones:325
1. Insert
2. Search
3. Delete Y en donde cada elemento del diccionario contiene una clave la cual permite identificarlo.

## Tabla de direccionamiento directo
Como vamos a implementar los diccionarios? Con una tabla de direccionamiento directo

Tenemso una empresa de turismo que decide hacer descuentos en ciertos descuentos dependiendo del mes:
   - enero=bariloche
   - febrero=ushuaia
   - marzo=cordoba
   - etc Cuando necesitamos un conjunto dinamico tenemos que cada elemento posee una clave dentro de un universo. U =
{0,1,2,...,m-1} m no es muy grande y son claves diferentes. Para representar el diccionario usamos una tabla de
direccionamiento directo.(DirectAccessTable) T[0,1,2,...,m-1] En el cual cada posicion de la tabla corresponde con una
clave en el universo(U)

Podemos implementar esta tabla usando listas.

```
class DirectAccessTable():
    def __init__(self, capacity):
        self.m=capacity # ACA INGRESAMOS LA CAPACIDAD DEL U
        self.T=[None] * self.m # ACA TENEMOS LA INICIALIZACION DE LA TABLA VACIA POR LA CANTIDAD DE ELEMENTOS.

    def insert(self,key,element):
        self.T[key]=element # ACCEDEMOS A LA POSICION DE LA TABLA CON LA LLAVE Y LE ASIGNAMOS EL ELEMENTO

    def search(self,key):
        return(self.T[key]) # PARA BUSCAR CON LA LLAVE YA VAMOS DIRECTAMENTE A LA POSICION DE LA TABLA

    def delete(self,key):
        self.T[key]=None # CON LA LLAVE LE ASIGNAMOS NONE Y LISTO

'''
DEVUELTA AL EJEMPLO DE TURISMO
CON LOS 12 ELEMENTOS DEL AÑO
'''
discounts=DirectAccessTable(12)
discounts.insert(0,'Bariloche')
discounts.insert(1,'Ushuaia')
discounts.insert(2,'Cordoba')
```

Cada una de las operaciones de diccionario, se ejecutan en tiempo constante. El espacio en memoria ocupado es del orden
del tamaño del universo U.

### CONS DE USAR TDD
- Cuando el tamaño del universo U de claves es grande
- Cuando la cantidad de elementos del diccionario es mucho mas pequeño que el tamaño de U No resulta conveniente
implementar el diccionario mediante una tabla de direccionamiento directo.

## Tablas hash
Debemos contar con dos puntos fundamentales:
1. Hay que definir una tabla de tamaño m
    - t[0,1,2,...,m-1]
    - m es la maxima cantidad de claves que soporta
    - Se espera que m sea menor que el tamaño del universo de claves osea que m<|U|
2. Hay que definir una funcion h: U->{0,...,m-1} que llamamos funcion hash h calcula para cada clave k la posicion o
    slot de la tabla que le corresponde.

En una tabla hash el elemento con clave k se almacena en T[h(k)]

Que pasa con este metodo puede pasar que haya una colision, que es una colision? que 2 claves mapean a la misma posicion
de la tabla, por ej: h(k2) = h(k3)

Para resolver las colisiones luego veremos que hacemos.

Tabla hash:
```
class HashTable():
    def __init__(self,capacity, hashFunction):
        self.m=capacity
        self.h=hashFunction
        self.T=[None]*self.m

    def insert(self,key,element):
        pass

    def search(self,key):
        pass

    def delete(self,key):
        pass
```
Una buena funcion hash debe:
- Poder calcularse en tiempo constante
- Satisfacer la hipotesis del hashing uniforme:
Osea es equiprobable que una clave tenga cualquier valor hash entre 0 y (m-1)

Algunas funciones hash asumen que el universo de las claves es el conjunto N de numeros naturales.
Si las claves no son numeros naturales debemos encontrar la forma de interpretarlas como si lo fueran.
Dada una cadena c, podemos transformar la cadena usando la siguiente funcion:
    c='hola'
    27 es el numero de letras por lo tanto tenemos 27 valores en el arreglo
    stringtonat(c)= ((ord'h')*(27^0))+((ord'o')*(27^1))+((ord'l')*(27^2))+((ord'a')*(27^3))= a un valor numerico = 1991084
    el ord lo que hace es darnos el valor ascii de la letra


Metodo de Resto
h(k)=k mod m
- Hay que tener que cuidado con el valor de m
- Funciona mal ocn valores m=2^p, h(k) estara dado por los primeros p bits de k, sin tener en cuenta los bits de orden superior
- Funciona bien con m primos.

si tenemos una tabla de tamaño m = 523

h(stringtonat('hola'))= stringtonat('hola') mod 523 = 1991084 mod 523 = 23

El elemento con clave hola se va a guardar en la pos 23 de la tabla hash con el metodo del resto

Metodo de la multiplicacion
h(k)=L m * (k*A - L k*A L) L
L es para indicar el piso
A = un valor entre 0 y 1
