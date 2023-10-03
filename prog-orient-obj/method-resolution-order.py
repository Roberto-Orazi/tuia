class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")
class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B,C): #TIENE PRIORIDAD SIEMPRE EL PRIMER PARAMETRO Y TODA SU LINEA, LUEGO PASA AL SEGUNDO PARAMETRO
    def hablar(self):
        print("Hola desde D")

d = D()

d.hablar()

C.hablar(d)

print(D.mro()) #PARA VER EL ORDEN DE RESOLUCION
''' ESTO SERIA SI B Y C TIENEN EL PARAMETRO DE LA CLASE A DE PADRE
[<class '__main__.D'>,
<class '__main__.B'>,
<class '__main__.C'>,
<class '__main__.A'>,
 <class 'object'>]
'''

'''
[<class '__main__.D'>,
<class '__main__.B'>,
<class '__main__.A'>,
<class '__main__.C'>,
<class '__main__.F'>,
<class 'object'>] #TODOS SON OBJETOS POR ESO SIEMPRE EL PADRE ES OBJECT
'''
