class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self,otro):
        nuevo_valor=self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

roberto=Persona('Robertito',26)
athena=Persona('Athena',2)
print(roberto)

tupla=(1,2,3)
print(tupla)

representante=repr(roberto)
print(representante)
resultado=eval(representante)
print(resultado.edad)

resultado_suma=roberto+athena
print(resultado_suma.nombre,resultado_suma.edad)