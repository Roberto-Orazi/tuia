### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson()) # Aca creamos una instancia y podemos ver el hash(ubicacion en memoria) del objeto
print(MyEmptyPerson) # aca solo imprimimos la representacion de la clase y no una instancia en especifico

class Person:
    def __init__(self, name:str, surname:str)->None:
        self.full_name = f'{name} {surname}'
        self.__name=name
        self.__surname=surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def walk(self):
        return(f'{self.full_name} Esta caminando')

    def __str__(self):
        return(f'Mi nombre es {self.get_name()} y mi apellido {self.get_surname()}')

my_person=Person('roberto','orazi')
print(my_person.walk())

my_other_person=Person('Juancete','troleador')
print(my_other_person)

my_other_person.full_name=('me cambio el nombre')
print(my_other_person.full_name)