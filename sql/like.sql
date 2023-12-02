/*Filtra mediante strings/patrones de texto*/
SELECT * FROM Employees WHERE LastName LIKE "%Fuller"
/*El % adelante es que termina con r*/
SELECT * FROM Employees WHERE LastName LIKE "%r"
/*probablemente nos traiga el mismo apellido y otro mas que tenga una r en el lastName*/

SELECT * FROM Employees WHERE LastName LIKE "f%"
/*asi podemos buscar algo que empiece con f RECORDAR QUE sqllite NO ES CASE SENSITIVE depende el gestor igual conviene
trabajar siempre como es*/
SELECT * FROM Employees WHERE LastName LIKE "F%"
/*El porcentaje atras significa que el apellido va a mpezar con F y despues sigue con cualquier cosa*/
/*Si ponemos una letra y porcentaje adelante y atras nos busca cualquier apellido que tenga una r en cualquier parte*/
SELECT * FROM Employees WHERE LastName LIKE "%r%"

/*EL OPERADOR = FUNCIONA IGUAL QUE EL LIKE SOLO QUE NO TIENE LOS PATRONES DE BUSQUEDA*/
SELECT * FROM Employees WHERE LastName = "Fuller"

/*Puede ser con cualquier letra o letras, por ejemplo si pongo %er% Me buscaria cualquier apellido que tenga er en el
string
*/

/*Nos busca un apellido que empiece con F tenga 4 caracteres cualquiera en el nombre y termine con r*/
SELECT * FROM Employees WHERE LastName LIKE "F____r"
/*PUEDE SER CUALQUIER COMBINACION PODRIA SER "F_F__R" POR EJEMPLO O Full____ y no nos devolveria nada ya que si ponemos
_ es un char*/

/*si no sabemos la cantidad de caracteres que pueden tener podemos hacer esto*/
SELECT * FROM Employees WHERE LastName LIKE "_r__%"
/*ESTO NOS TRAE UNA PALABRA QUE TIENE 1 CHAR LA LETRA R 2 CHARS Y PUEDE TENER MAS CHARS SI EXISTIESE*/

/*SON TODOS BUSQUEDA DE PATRONES DE TEXTO*/
