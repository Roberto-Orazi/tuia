### Regular Expressions ###

import re

my_string='Esta es la leccion sobre: Expresiones regulares'
my_other_string='Esta no es la leccion sobre: Expresiones regulares'

match=re.match('Esta es la leccion', my_string, re.I)
print(match)

start, end=match.span()
print(my_string[start:end])


dont_exist=re.match('Esta es la leccion', my_other_string)
print(dont_exist)
if not(dont_exist == None):
    print(dont_exist.span())
    start, end=dont_exist.span()
    print(my_other_string[start:end])
else:
    print('No existe')
exist=re.match('Expresiones regulares', my_string)
print(exist)
