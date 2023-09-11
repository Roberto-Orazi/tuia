## Apartado teorico
- Definiciones y usos
- Notacion de chen
- Fundamentos
- Etc

## Apartado practico

# SQL
### Que es?
#### Structured Query Language
### Para que sirve?
- Para todo, ya sea sistema de gestion, ai, web applications.
- Crear, administrar, modificar bases de datos, tablas y otros objetos
- Realizar consultas a una base de datos
- Modificar los datos
- Agregar restricciones y reglas / condiciones
- Generar informas
- Analisis de datos
- Data science
- Usuarios y permisos
- Analizar transacciones
Nosotros lo vamos a usar para:
- Crear, modificar, eliminar y traer datos


## DIAGRAMA ER (CHEN)

### Entidad
Una entidad es como un objeto, es como una representacion de algo.
Una entidad persona no es una persona es una representacion de una persona.

Ejemplo:
Una base de datos de una tienda en linea las entidades pueden ser:
- Clientes
- Productos
- Ordenes de compra
- Proveedores
Y la nomenclatura que se usan para representar las entidades se llaman notacion de chen.
Es una forma de representar entidades y sus relaciones

Dentro de notacion de chen:
Si una palabra esta adentro de un cuadrado es una entidad
Si esta adentro de un circulo es un atributo
Adentro de atributos tenemos:

- ATRIBUTOS SIMPLES(OVALO)
Son datos unicos
Ejemplo:
PRECIO:$2000

- ATRIBUTOS COMPUESTOS(TIENEN MAS DE UN ATRIBUTO SIMPLE)
QUE SE COMPONEN DE OTROS ATRIBUTOS
Ejemplo:
AMBIENTES -> LIVING, COMEDOR, BAÑO

- ATRIBUTOS MULTIVALOR(DOBLE OVALO)
SON MULTIVALOR PORQUE TIENEN MAS DE UN VALOR
Ejemplo:
AMBIENTES YA QUE TIENE MAS DE UNO
- ATRIBUTOS DERIVADOS(OVALO CON BORDE PUNTEADO)
Se pueden obtener con cualquier otra informacion.
Ejemplo:
En el caso de una casa, si decimos que tiene antiguedad=20 años, pero tambien tenemos fecha de construccion, podemos sacar la antiguedad haciendo el calculo con la fecha de construccion. Igual que si tenemos direccion y ubicacion, con uno podes sacar el otro.

Despues tenemos la clave o KEY(Es un atributo asique va en ovalo y va subrayado)
Que es lo que lo hace unico ya que seria el Id de la propiedad.
Es la forma de hacer algo unico



ENTIDAD PERSONA
## ATRIBUTOS SIMPLES
ALTURA
EDAD
NOMBRE
## ATRIBUTOS COMPUESTOS
HOBBIES
## KEY
DNI

## ENTIDAD EMPLEADO
### KEY
- id empleado
### ATRIBUTO COMPUESTO
#### Informacion de contacto
- Telefono
- Mail
- Direccion
### ATRIBUTO MULTIVALOR
- Habilidades
### ATRIBUTO DERIVADO
- Edad(tengo la fecha de nacimiento)
### ATRIBUTO SIMPLE
- Nombre
- Apellido
- Fecha de nacimiento
- Genero
- Estado civil

EN BASES DE DATOS
LAS TABLAS CONTIENEN FILAS Y COLUMNAS
LOS VALORES DE CAMPO SON LOS VALORES
LAS FILAS SE LLAMAN REGISTROS
LAS COLUMNAS SE LLAMAN CAMPOS
LAS QUERY SON LAS CONSULTAS A LAS DB

TIPOS DE DATOS:
INTEGER, ES INT
TEXT, ES CHAR
BLOB, ALMACENA DATOS BINARIOS
REAL, ES FLOAT (es de 8bytes por lo tanto es mas rapido y almacena menos informacion)
NUMERIC, NUMEROS MATEMATICOS MUY ESPECIFICOS, POR EJEMPLO PI QUE TIENEN MUCHA PRECISION (es mas lento pero no tiene limite de almacenmaiento)

SON CAMPOS DINAMICOS YA QUE LO QUE LE INSERTEMOS HACE QUE LA COLUMNA SE TRANSFORME EN ESO, SI YO GUARDO UN TEXTO EN UN CAMPO DE INTEGER EL CAMPO PASA A SER TEXT PERO ES MALA PRACTICA

IDENTIFICADORES:
Son campos que sirven para identificar un registro entero y tenemos 2 tipos

1. PRIMARY KEYS(PK)(Claves primarias)
- Son los id de cada entidad
- No pueden tener valores nulos

2. FOREIGN KEYS(FK)(Claves foraneas)
- Son los id que usamos para hacer referencia a los id de otra entidad/tabla/lugar
- Son las Primary Keys de la tabla a la que hacemos referencia

turnos_medicos      usuarios
id_turno(PK)        id_usuario(PK)
profesional         nombre
id_usuario(FK)      apellido
motivo              edad
horario