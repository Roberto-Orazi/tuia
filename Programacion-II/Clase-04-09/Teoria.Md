```
def find_center(rectangle:Rectangle)->Point:
    medio_x=(rectangle.corner.x + rectangle.width / 2)
    medio_y=(rectangle.corner.y + rectangle.height / 2)
    return Point(medio_x,medio_y)
```
#### Para esta funcion hay que pasarle como parametro un rectangulo

### En python todos los objetos son mutables, es decir, podemos cambiar sus atributos por otros valores.
#### Ejemplo
```
rectangle.width+=50
rectangle.height+=100
```

## Funciones puras vs modificadoras

- Funciones puras no modifican ningun objeto pasado a las mismas

- Funciones modificadoras realizan cambios en los objetos pasados a las mismas

```
def grow_rectangle(rect:Rectangle, dw:float, dy:float)->None:
    rect.width=rect.width+dw
    rect.height=rect.height+dy

corner=(0,0)
bob=Rectangle(100,200,corner)
grow_rectangle(bob,50,100)
```



## COPIANDO OBJETOS

>>>import copy q = copy.copy(p) p is q False


>>> import copy r2 = copy.deepcopy(r) r is r2 False r.corner is r2.corner False

```
class Time:
    def __init__(self,hh:int,mm:int,ss:int)->None:
        self.hours=hh
        self.minutes=mm
        self.seconds=ss

    def increment(self,seconds:int)->None:
        self.seconds=seconds+self.seconds()

        while self.seconds>=60:
            self.seconds=self.seconds-60
            self.minutes+=1

    TODO: HACER LA FUNCION DE TAREA PDF PAGINA 41
    def convert_to_seconds()->:
```

```
class Point:
    def __init__(self, x:float,y:float)->None:
        self.x=x
        self.y=y

    def __add__(self,other:'Point')->Bool:
        Return Point(self.x+other.x,self.y+other.y)
```
### El metodo __add__ recibe como parametro otro objeto de tipo punto y devuelve un nuevo objeto que es la suma de ambos.

```
class Square:
    def __init__(self,size:float,corner:Point)->None:
        self.size=size
        self.width=self.size
        self.height=self.size
        self.corner=corner

    def get_area(self)->float:
        return self.size**2

```