SELECT * FROM Products
WHERE CustomerID >=50 AND CustomerID < 55;
/*Nos devolveria desde el registro 50 hasta el 54*/

SELECT * FROM Employees
WHERE FirstName = 'Nancy' OR FirstName = 'Anne';
/*Nos devuelve nancy y anne porque una cumple con nancy y otra con anne, solo devuelve o una o otra o ambas que existan*/;


SELECT * FROM Products
WHERE (Price < 20 OR CategoryID = 6) AND SupplierID =7
/*RECORDAR USAR PARENTESIS PORQUE SINO EL AND ES MAS FUERTE QUE EL OR ENTONCES SERIA PRECIO MENOR A 20 O TODO LO OTRO*/;

SELECT * FROM Products
WHERE NOT Price > 40
/*El not funciona igual que en todos los lenguajes.*/;

SELECT * FROM Products
WHERE NOT Country = 'USA' AND NOT Country = 'France';

/*Clausula LIMIT*/
SELECT * FROM Products
WHERE CustomerID >=50
AND NOT Country = 'USA'
AND NOT Country = 'France'
LIMIT 5;
/*SALEN LOS PRIMEROS 5 PAISES QUE SEAN DESPUES DE LOS 50 Y QUE NO SEAN DE USA NI FRANCIA*/;

SELECT * FROM Products
WHERE NOT CategoryID = 6
AND NOT SupplierID = 1
AND PRICE <= 30
ORDER BY RANDOM()
LIMIT 3;
/*Como pusimos el order by random nos va a dar 3 aleatorios cada vez que hagamos la consulta*/;

/*DISTINTO OR NOT?*/;

SELECT * FROM Customers
WHERE Country != 'USA'
/*SERIA LO MISMO QUE*/;
WHERE NOT Country = 'USA';

SELECT * FROM Products WHERE NOT TRUE;
/*
WHERE TRUE DEVUELVE TODO EL REGISTRO
WHERE FALSE NO TE DEVUELVE NADA
*/;

/*
NOT NO ES LO MISMO QUE != YA QUE SI BIEN LLEGAN A LO MISMO EL FUNCIONAMIENTO INTERNO ES DISTINTO YA QUE EL != ES UN COMPARADOR Y EL NOT ES UN CONTRARIO
*/
