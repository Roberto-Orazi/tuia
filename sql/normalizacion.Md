FN = Forma Normal
# First Normal Form(1FN)
Establece que no debe haber valores repetidos en una fila para una clave primaria
Tiene que haber una columna por cada valor, no poner varios y separarlos por coma, por ej: nombre y apellido
# Second Normal Form(2FN)
Cada atributo que no sea una clave, debe depender totalmente de la clave primaria
# Third Normal Form(3FN)
Cada atributo debe depender directamente de la clave primaria. No debe haber dependencia transitiva. Osea que no dependa de otro atributo, que dependa directamente del pk. por ejemplo si tenemos una ubicacion que tenemos provincia ciudad codigo postal podemos
hacer que dependan todos de un id que hacer que dependa que la ciudad dependa de la provincia
# Fourth Normal Form(4FN)
Cada tabla debe tener una clave primaria compuesta.
# Fifth Normal Form(5FN)
Se asegura que no haya dependencias de union entre atributos. Osea si un atributo depende de que se unan atributos de varias tablas
se tiene que mover a otra tabla.

```


```