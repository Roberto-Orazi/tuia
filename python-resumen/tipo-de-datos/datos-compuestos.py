#LISTA VACIA
lista = []
#LISTA CON DATOS DE UN MISMO TIPO ENTERO
lista = [1,2,3,4,5]
#LISTA CON DATOS ENTEROS, STRING Y BOOLEANOS
lista = [1,2,3,4,5,"hola",True]
#LISTA CON DATOS ENTEROS, STRING, BOLEANOS Y LISTAS
lista = [1,2,3,4,5,"hola",True,[1,2,3,4,5]]
#LISTA CON DATOS ENTEROS, STRING, BOLEANOS, LISTAS Y TUPLAS
lista = [1,2,3,4,5,"hola",True,[1,2,3,4,5],(1,2,3,4,5)]
#LISTA CON DATOS ENTEROS, STRING, BOLEANOS, LISTAS, TUPLAS Y DICCIONARIOS
lista = [1,2,3,4,5,"hola",True,[1,2,3,4,5],(1,2,3,4,5),{"nombre":"Juan"}]
#LISTA CON DATOS ENTEROS, STRING, BOLEANOS, LISTAS, TUPLAS, DICCIONARIOS Y NONE
lista = [1,2,3,4,5,"hola",True,[1,2,3,4,5],(1,2,3,4,5),{"nombre":"Juan"},None]
#LISTA CON DATOS ENTEROS, STRING, BOLEANOS, LISTAS, TUPLAS, DICCIONARIOS, NONE Y FLOAT
lista = [1,2,3,4,5,"hola",True,[1,2,3,4,5],(1,2,3,4,5),{"nombre":"Juan"},None,1.2]

#Tipo de datos = list
'''
Metodos de listas
append() = agrega un elemento al final de la lista
clear() = elimina todos los elementos de la lista
copy() = devuelve una copia de la lista
count() = devuelve el numero de elementos con el valor especificado
extend() = agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
index() = devuelve el indice del primer elemento con el valor especificado
insert() = agrega un elemento en la posicion especificada
pop() = elimina el elemento en la posicion especificada
remove() = elimina el primer elemento con el valor especificado
reverse() = invierte el orden de la lista
sort() = ordena la lista
len() = devuelve el numero de elementos de una lista
max() = devuelve el elemento con mayor valor de la lista
'''

#Creando una lista(Se pueden modificar)
lista1 = ["Roberto Orazi", "Soy Hombre", True, 1.93]

# indice = 0, 1, 2, 3 seria elemento 1, 2, 3, 4 de la lista

lista1[0] # Roberto Orazi
lista1[1] # Soy Hombre
lista1[2] # True
lista1[3] # 1.93


#La diferencia con la lista es que no se puede modificar

#Creando una tupla(No se pueden modificar los elementos, si se puede redefinir toda la tupla)
tupla1 = ("Roberto Orazi", "Soy Hombre", True, 1.93)

#Creando un conjunto
conjunto= {"Roberto Orazi", "Soy Hombre", True, 1.93}
#No se puede cambiar los elementos, se puede redefinir todo el conjunto entero
'''
Se puede mostrar entero, pero no por indices
No se puede repetir valores
'''
#Para acceder a los elementos del conjunto se usa un for

#Creando un diccionario
#Estructura key: valor (ES UN JSON DE JS)
diccionario = {
    "nombre": "Roberto Orazi", #0
    "genero": "Soy Hombre", #1
    "vivo": True, #2
    "altura": 1.93 #3
}
#Muestra los datos por el nombre asociado osea el nombre del diccionario y el nombre del dato(key)
diccionario["nombre"] # Roberto Orazi
diccionario["genero"] # Soy Hombre
diccionario["vivo"] # True
diccionario["altura"] # 1.93

#A diferencia de la lista nosotros tenemos un nombre de dato como key y un valor asociado a ese key
#En la lista tenemos el indice como key



