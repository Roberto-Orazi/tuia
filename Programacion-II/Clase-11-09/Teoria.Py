"""
**Ejercicio 1**: Definir la interfaz, con la estructura que vimos en teoría, de un TAD para representar una celda. Una
celda es capaz de contener un **único** valor a la vez, es decir, siempre que ponemos un nuevo valor, debemos quitar el
valor anterior.

_Nota: no olvidar describir el \_\_init___
"""


class Celda:
    def __init__(self):
        pass

    def poner_valor(self):
        """
        Dado el valor lo ponemos adentro de la celda
        """
        pass

    def quitar_valor(self):
        """
        Si hay un valor lo saca y deja vacia la celda
        """
        pass

    def obtener_valor(self):
        """
        Dice el valor actual de la celda
        """
        pass

    def esta_vacia(self):
        """
        Dice si tiene un valor o no
        """
        pass


"""
**Ejercicio 2**: Basándose en la interfaz hecha en el ejercicio anterior, implementar en Python una clase Celda que que
respete el comportamiento descrito. Escribir código cliente de dicha interfaz.
"""


class Celda:
    def __init__(self) -> None:
        self.valor = None

    def poner_valor(self, valor):
        """
        Dado el valor lo ponemos adentro de la celda
        """
        self.valor = valor

    def quitar_valor(self):
        """
        Si hay un valor lo saca y deja vacia la celda
        """
        self.valor = None

    def obtener_valor(self):
        """
        Dice el valor actual de la celda
        """
        if self.valor is None:
            return "ficon trolo"
        else:
            return self.valor

    def esta_vacia(self):
        """
        Dice si tiene un valor o no
        """
        return self.valor == None


celda = Celda()
print(celda.esta_vacia())
celda.poner_valor(5)
print(celda.esta_vacia())
print(celda.obtener_valor())
celda.quitar_valor()
print(celda.esta_vacia())

"""
**Ejercicio 3**: Repetir el Ejercicio 1 con un Conjunto matemático. Se definen con elementos preestablecidos, nunca
cambian, y la única operación posible es preguntarnos si un elemento pertenece o no al conjunto.
"""


class Conjunto:
    """
    Representa un conjunto matemático, con elementos preestablecidos, que no cambian, y la única operación posible es
    preguntarnos si un elemento pertenece o no al conjunto.
    """

    def __init__(self) -> None:
        """
        Crea un conjunto con los elementos pasados por parámetro.
        """
        pass

    def pertenece(self, value):
        """
        Devuelve True si el elemento pertenece al conjunto, False en caso contrario.
        """
        pass


"""
**Ejercicio 4**: Basándose en la interfaz hecha en el ejercicio anterior, implementar en Python una clase Conjunto que
respete el comportamiento descrito.

*Ayuda: para el constructor, pueden pasar una lista, o usar la sintaxis *args para recibir una cantidad arbitraria de
argumentos.*
"""


class Conjunto:
    def __init__(self, *elementos) -> None:
        self.elementos = elementos

    def pertenece(self, elemento):
        return elemento in self.elementos


conjunto = Conjunto(1, 2, 3, 4, 5)
print(conjunto.pertenece(1))
print(conjunto.pertenece(6))


"""
**Ejercicio 5**: Dar una implementacion en Python del TAD Vector, que representa un vector de números reales de algebra.
La interfaz queda definida por las siguientes operaciones:

`__init__`: Recibe la dimensión y crea un vector de esa cantidad de ceros.

`get`: Recibe una posición y devuelve el valor en dicha posición del vector. Retorna `None` si la posición es inválida.

`put`: Recibe una posición y un `float`, y actualiza dicha posición del vector con el valor suministrado. **Devuelve el
valor nuevo** si la posición es válida, o `None` si es inválida.

`__add__`: Recibe como parámetro otro vector. Si el tamaño no es compatible, devuelve `None`. Si el tamaño es
compatible, devuelve un nuevo vector con el resultado de la suma componente a componente entre ambos.

_Nota: a la hora de implementar la suma, tratar de utilizar los otros métodos_
"""


class Vector:
    def __init__(self, dimension):
        """
        Recibe la dimensión y crea un vector de esa cantidad de ceros.
        """
        self.dimension = dimension
        self.vector = [0] * dimension

    def get(self, posicion):
        """
        Recibe una posición y devuelve el valor en dicha posición del vector. Retorna `None` si la posición es inválida.
        """
        if posicion < 0 or posicion >= self.dimension:
            return None
        return self.vector[posicion]

    def put(self, posicion, valor):
        """
        Recibe una posición y un `float`, y actualiza dicha posición del vector con el valor suministrado. **Devuelve el
        valor nuevo** si la posición es válida, o `None` si es inválida.
        """
        if posicion < 0 or posicion >= self.dimension:
            return None
        self.vector[posicion] = valor
        return valor

    def __add__(self, otro_vector):
        """
        Recibe como parámetro otro vector. Si el tamaño no es compatible, devuelve `None`. Si el tamaño es compatible,
        devuelve un nuevo vector con el resultado de la suma componente a componente entre ambos.
        """
        if self.dimension != otro_vector.dimension:
            return None
        resultado = Vector(self.dimension)
        for i in range(self.dimension):
            resultado.put(i, self.get(i) + otro_vector.get(i))
        return resultado

    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return str(self)

#TODO: CAMBIAR PARA QUE EN VEZ DE QUE TENGA POS 0 EMPIECE EN 1
v1 = Vector(5)
v2 = Vector(5)
v1.put(0, 1)
v1.put(1, 2)
v1.put(2, 3)
v1.put(3, 4)
v1.put(4, 5)
v2.put(0, 1)
v2.put(1, 2)
v2.put(2, 3)
v2.put(3, 4)
v2.put(4, 5)
print('vector1:', v1)
print('vector2', v2)
print(v1 + v2)

"""
Ejercicio 6 Implemente el TAD Lista de la teoría, utilizando nodos enlazados. __str__ __len__ append(x) insert(i,x)
remove(x) pop(x) index(x)
"""


class Nodo:
    def __init__(self, valor, siguiente=None):
        """
        Modela un nodo de una lista enlazada
        """
        self.valor = valor
        self.siguiente = siguiente

    def __str__(self):
        """
        La funcion str de un nodo es el valor que contiene
        """
        return str(self.valor)

class ListaEnlazada:
    def __init__(self, nodo=None):
        """
        Modela una lista enlazada
        """
        self.nodo = nodo

    def __str__(self):
        """
        La funcion str de una lista es la concatenacion de los str de sus nodos
        """
        if self.nodo == None:
            return "[]"
        else:
            return "[" + str(self.nodo) + "]"

    def __len__(self):
        """
        La longitud de un nodo es 1 mas la longitud del siguiente
        """
        return 1 + len(self.siguiente)

    def append(self, valor):
        """
        Agrega un valor al final de la lista
        """
        if self.siguiente == None:
            self.siguiente = Nodo(valor)
        else:
            self.siguiente.append(valor)

    def insert(self, posicion, valor):
        """
        Inserta un valor en la posicion indicada
        """
        if posicion == 0:
            self.siguiente = Nodo(self.valor, self.siguiente)
            self.valor = valor
        else:
            self.siguiente.insert(posicion - 1, valor)

    def remove(self, valor):
        """
        Elimina el primer valor que coincida con el valor pasado por parametro
        """
        if self.valor == valor:
            self.valor = self.siguiente.valor
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.remove(valor)

    def pop(self, posicion):
        """
        Elimina el valor de la posicion indicada
        """
        if posicion == 0:
            self.valor = self.siguiente.valor
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.pop(posicion - 1)

    def index(self, valor):
        """
        Devuelve la posicion del primer valor que coincida con el valor pasado por parametro
        """
        if self.valor == valor:
            return 0
        else:
            return 1 + self.siguiente.index(valor)


"""
**Ejercicio 7**:

a. Modifique el ejercicio anterior para que insert e index sean métodos recursivos implementados en la clase Nodo. La
   clase ListaEnlazada simplemente llama a estos.

b. ¿Podemos hacer lo mismo con el metodo `remove`? ¿Y para `[]`? Justifique.

c. Escriba codigo cliente que demuestre que las tres implementaciones de listas (list de python, la del ejercicio 7 y la
   de este ejercicio) se comportan igual.
"""


class ListaEnlazada:
    def __init__(self, nodo=None):
        """
        Modela una lista enlazada
        """
        self.nodo = nodo

    def __str__(self):
        """
        La funcion str de una lista es la concatenacion de los str de sus nodos
        """
        if self.nodo == None:
            return "[]"
        else:
            return "[" + str(self.nodo) + "]"

    def __len__(self):
        """
        La longitud de una lista es la longitud de su nodo
        """
        if self.nodo == None:
            return 0
        else:
            return len(self.nodo)

    def append(self, valor):
        """
        Agrega un valor al final de la lista
        """
        if self.nodo == None:
            self.nodo = Nodo(valor)
        else:
            self.nodo.append(valor)

    def insert(self, posicion, valor):
        """
        Inserta un valor en la posicion indicada
        """
        if posicion == 0:
            self.nodo = Nodo(valor, self.nodo)
        else:
            self.nodo.insert(posicion - 1, valor)

    def remove(self, valor):
        """
        Elimina el primer valor que coincida con el valor pasado por parametro
        """
        if self.nodo.valor == valor:
            self.nodo = self.nodo.siguiente
        else:
            self.nodo.remove(valor)

    def pop(self, posicion):
        """
        Elimina el valor de la posicion indicada y retorna el anterior
        """
        if posicion == 0:
            self.nodo = self.nodo.siguiente
        else:
            return self.nodo.pop(posicion - 1)
            # TODO: Corregir el pop

    def index(self, valor):
        """
        Devuelve la posicion del primer valor que coincida con el valor pasado por parametro
        """
        return self.nodo.index(valor)
