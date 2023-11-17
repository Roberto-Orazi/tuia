#QUE SON LAS VARIABLES?
'''
Las variables son espacios que se almacenan en la memoria de nuestro programa.
Porque son datos que se reutilizan
'''
#EJEMPLO
a = 1
b = 2
c = a + b
a = c
declaracion = 'definiendo la variable'
'''
- Solo se declara la primera vez, despues de redefine el valor
- Son variables porque como dice su nombre varia, su valor puede cambiar
- Siempre va a tomar el ultimo valor asignado/definido
'''
#Definiendo variables
nombre = 'Roberto'
apellido = 'Orazi'
#Concatenar con el operador +
print('Mi nombre es' + ' ' + nombre + ' ' + apellido)
despedida = 'Adios' + ' ' + nombre + ' ' + apellido
#Concatenar con f-string
print(f'Mi nombre es {nombre} {apellido}')
saludo = f'Mi nombre es {nombre} {apellido}'

#En python se usa snake_case para definir variables
mi_variable = 'mi variable'
#En python se usa PascalCase para definir clases
MiClase = 'Mi clase'
#En python se usa camelCase para definir funciones
miFuncion = 'mi funcion'
#En python se usa UPPER_CASE para definir constantes
MI_CONSTANTE = 'mi constante'
#En python se usa kebab-case para definir archivos
mi_archivo = 'mi archivo'

