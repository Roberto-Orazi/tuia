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