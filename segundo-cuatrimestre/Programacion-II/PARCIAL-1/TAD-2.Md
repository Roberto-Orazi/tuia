# TAD Lista
Metodos:
- str
- len
- append(x)
- insert(i,x)
- remove(x)
- pop(i)
- index(x)

# TAD Pila(Stack)
Metodos:
- init
- push
- pop
- isEmpty
```
class Pila:
    def __init__(self):
        self.items=[]

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if self.isEmpty():
            print('La pila esta vacia')
            return
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])
```

# TAD Cola
Metodos:
- init
- insert
- remove
- isEmpty

class Cola:
    def __init__(self):
        self.items=[]

    def insert(self,x):
        self.item.append(x)

    def remove(self):
        if self.isEmpty():
            print('la cola esta vacia')
            return
        return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0