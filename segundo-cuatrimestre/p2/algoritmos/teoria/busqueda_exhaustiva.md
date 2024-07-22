# Iterador
Es un señalador, que va marcando en donde estoy(El libro seria nuestra clase iterable), el libro es la lista y el iterador seria el marcapaginas. Es la referencia que nos indica en que posicion estamos.


# Generador

Los generadores son una nueva forma de devolver valores en python
En este caso yield

Ejemplo de uso:
```python
def f():
    '''
    esto devuelve primero 1, luego 2 y despues sale de la funcion ya que el return retorna
    '''
    yield 1
    return 2
    yield 3

gen=f()
next(gen) # 1
next(gen) # 2
next(gen) # error

```
Cualquier funcion que utilice al menos un yield, va a ser un generador


```python

def es_solucion(intento: list[int])-> bool:
    for i in range(len(intento)-1):
        if intento[i] > intento[i+1]:
            return False


from typing import Iterator

def candidatos(lista: list[int]) -> Iterator:
    if lista==[]:
        yield[]
    if len(lista) == 1:
        yield lista
    else:
        for elemento in lista:
            lista2=copy.copy(lista)
            lista2.remove(elemento)
            for resto in candidatos(lista2):
                yield[elemento]+resto

        '''
        first=lista[0]
        resto=lista[1:]
        generador=candidatos(resto)
        for res in generador:
            yield[first]+res
        '''

```

https://pythontutor.com/visualize.html#mode=edit

un problema es una funcion con una solucion