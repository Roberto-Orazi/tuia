SELECT count(firstName) from Employees;
/*Nos devuelve la cantidad de valores que hay en el campo firstName*/;
/*Podemos guardarlo en una variable si queremos y hacemos*/;
SELECT count(firstName) AS Cantidad_de_nombres from Employees;

SELECT SUM(Price) from Products;
/*Esto nos devuelve la suma de todos los valores de la columna price*/

SELECT AVG(Price) from Products;
/*Esto nos devuelve el promedio de todos los valores de la columna price*/;

/*RECORDEMOS QUE PODEMOS FILTRARLOS ANTERIORMENTE Y HACER LA FUNCION DE ESE FILTRADO*/;

SELECT ROUND(AVG(Price), 2) as promedio from Products;
/*Esto nos devuelve el promedio REDONDEADO de todos los valores de la columna price* ROUND REDONDEA POR CANTIDAD DE
DECIMALES O LIBRE, SI NO LE PONEMOS EL PARAMETRO DE LA CANTIDAD DE DECIMALES POR DEFECTO DEJA SOLO LOS ENTEROS
ROUND(N1,N2) N2 ES LA CANTIDAD DE DECIMALES
*/;

SELECT MIN(Price) from Products;
/*Esto nos devuelve el MINIMO SI USAMOS MAX DEVUELVE EL MAXIMO de todos los valores de la columna price*/;

/*Puedo combinar algo asi:*/
SELECT ProductName, MIN(Price) from Products;
WHERE ProductName IS NOT NULL /*Usamos esto porque sino el mas chico va a ser nulo*/
/*En maximo no pasa porque los nulls son minimos en terminos numericos*/

