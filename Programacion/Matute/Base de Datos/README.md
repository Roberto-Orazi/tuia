# Base de datos 1


- 2 trabajos practicos para poder aprobar la materia.
- Son grupales de 3 o 4 personas.
- TP1: consta sobre contenidos de la unidades 1 y 2 en la semana 8. Mediados de Octubre
- TP2: consta de las unidades 3 y 4. Mas que nada unidad 3.
- Los trabajos son una continuacion del otro. Podriamos decir que es 1 trabajo practico global con 2 entregas.
- 1 parcial. Semana 14(fines de noviembre)
- Defensa de coloquio


## Unidad 1 


Arquitectura de Von Neumann
Los registros son unidades de memoria.(memoria RAM, volatil)
Memoria auxiliar(velocidad de almacenamiento mas lento que el resto, pero almacena la mayoria de los datos que vamos a utilizar)
Velocidades de las memorias de nuestra computadora: De manera descendiente
* Registros(cpu)
* l1 cache
* l2....l3 cache    (43 ns)
* System RAM    (6min)
* Permanent Storage  (2-6 dias)
* Network Storage (1-12 months)

La mayoria de la informacion con la que vamos a trabajar la vamos a tener en disco. Esto va a hacer que va a ser lenta la busqueda de datos, por eso tenemos que utilizar base de datos para que la pc pueda hacerlo de la manera mas rapida posible.
* Nuestro objeto de estudio hara uso intensivo del almacenamiento secundario.
* Consideraciones de performance.

## Que es una base de datos? 
* Datos de entrada 
* Datos de salida
* Datos persistentes
Una base de datos esta constituida por ciert o conjunto de datos persistentes utilizados por los sistemas de aplicaciones en una organizacion. Estos datos deben estar disponibles para nuestro sistema de aplicaciones.

Archivo de datos: Es una estructura de datos formado por registros(filas), que habitualmente no reside en memoria principal, sino en algun medio de almacenamiento permanente.

La tabla se compone por columnas(campos) y filas(registros)
Sistemas de bases de datos: 
* Microsoft Access (relacional)
* Microsoft SQL Server
* MySQL
* Db2 de IMB
* MariaDB
* MongoDB(orientado a documentos)
* PostgreSQL 