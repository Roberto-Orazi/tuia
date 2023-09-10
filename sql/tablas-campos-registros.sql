/*CREAMOS LA TABLA*/
CREATE TABLE "usuarios" (
    "nombre" TEXT DEFAULT 'Nombre',
    "apellido" TEXT,
    "edad" INTEGER
);

/*CONSULTAS O QUERY*/
SELECT * FROM usuarios
SELECT nombres,apellido FROM usuarios
/*cada select devuelve una tabla nueva creada a partir
de los datos filtrados o de todo dependiendo lo que busquemos*/

/*AGREGAR DATOS A MI TABLA*/
INSERT INTO usuarios (nombre,apellido,edad) /*ACA ESTOY INSERTANDO EN LA TABLA USUARIOS EN LOS CAMPOS NOMBRE APELLIDO Y EDAD */
VALUES ('Roberto','Orazi',26),('Juan','Pepito',16) /*Y ACA ESTOY INGRESANDO LOS DATOS QUE QUIERO INSERTAR*/

/*ELIMINAMOS TODO*/
DELETE * FROM usuarios


/*AGREGAMOS ID YA QUE CON LA TABLA ANTERIOR NOS PUEDE PASAR QUE SE REPETIRIAN USUARIOS Y NO TENDRIAMOS COMO DIFERENCIARLOS*/
CREATE TABLE "usuarios" (
    "id_usuario" INTEGER, /*PODEMOS USAR EL AUTOINCREMENT EN EL PROGRAMA Y EL PK QUE SERIA EL PRIMARY KEY
    Lo que hace el autoincrement es que nos evita tener que ingresarlo manualmente
    Y EL PK VA A IR AUTOMATICAMENTE SI ESTA EL AUTOINCREMENT
    */
    "nombre" TEXT DEFAULT 'Nombre',
    "apellido" TEXT,
    "edad" INTEGER
);


/*AGREGAR DATOS A MI TABLA*/
INSERT INTO usuarios (nombre,apellido,edad) /*ACA ESTOY INSERTANDO EN LA TABLA USUARIOS EN LOS CAMPOS NOMBRE APELLIDO Y EDAD */
VALUES ('Roberto','Orazi',26),('Juan','Pepito',16) /*Y ACA ESTOY INGRESANDO LOS DATOS QUE QUIERO INSERTAR*/

SELECT * FROM usuarios

