from typing import Any


class Pila:
    '''
    Representa una pila con operaciones de apilar, desapilar y verificar si esta vacia.
    '''
    def __init__(self)->None:
        '''
            Crea una lista vacia
        '''
        self.items=[]

    def pop(self, item: Any)->None:
        '''
            Apila un elemento a la pila
        '''
        self.items.append(items)

    def pop(self, item: Any)->None:
        '''
            Desapila un elemento y lo devuelve . Si la pila esta vacia, imprime un mensaje de error y termina la
            ejecucion inmediatamente
        '''
        if self.isEmpty():
            print('La pila esta vacia')
            return
        return self.items.pop()

    def isEmpty(self)->bool:
        '''
        Devuelve true si la pila esta vacia y false si no
        '''
        return(self.items==[])


    def push(self,item:Any)->None:
        '''
            Apila un elemento a la pila
        '''
        self.items.append(item)