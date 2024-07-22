from typing import Iterator
import copy
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


l = [8,3,7,5]
gen=candidatos(l)

for i in range(12):
    print(next(gen))
