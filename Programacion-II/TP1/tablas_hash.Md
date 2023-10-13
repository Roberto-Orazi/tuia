# Tablas HASH
Muchas aplicaciones requieren trabajar con 3 operaciones basicas:
1. Insertar
2. Buscar
3. Eliminar

Ejemplos:
## Agenda Telefonica
- El usuario encuentra numeros de telefono a partir del nombre de pila de la persona a quien quiere llamar.
- Se puede añadir nuevos contactos ingresando el nombre(id) y el numero de telefono
- Tambien se puede elminar los contactos.

## Sistema de cache de un navegador
A traves del cache el navegador guarda las respuestas que reicibio de determinados pedidos, por ejemplo los https requests a distintos servidores.
Podemos pensar que el cache del navegador guardara la url de los recursos juntos con su contenido, por ejemplo una imagen. El navegador al tiempo borra la entrada en el cache asociada a la url.

Ademas de las 3 operaciones basicas ya mencionadas, tienen en comun otra cuestion, necesidad de usar claves y valores.

La operacion de busqueda:
- Busca algo por su clave(nombre de pila o url) y obtiene su valor asociado(el numero de telefono o imagen)

Estas aplicaciones son ejemplos de lo que en ciencias de la computacion se conoce como diccionarios.


## Diccionario
Es un conjunto dinamico que admite las tres operaciones:325
1. Insert
2. Search
3. Delete
Y en donde cada elemento del diccionario contiene una clave la cual permite identificarlo.

## Tabla de diccionamiento directo
