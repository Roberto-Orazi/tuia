/*
Inner join nos devuelve la coincidencia entre ambos
left join
right join
full join
cross join Lo que hace es cruzar todas las tablas con todo si tengo 2 tablas por ejemplo multiplica las filas de una columna por todas las columnas de la otra columna
*/;

/*FORMA EXPLICITA CROSS JOIN*/
SELECT * FROM Employees e, Orders o
WHERE e.EmployeeID = o.EmployeeID;
/*FORMA IMPLICITA CROSS JOIN*/
SELECT * FROM Employees e
CROSS JOIN Orders o;

/* CROSS JOIN NO SE USA MUCHO LA VERDAD
tabla 1     tabla 2        tabla cross (sigo para aca pero seguiria para abajo la tabla) es una sola tabla con las 9 posibilidades
rojo        chico           rojo chico      verde chico     azul chico
verde       mediano         rojo mediano    verde mediano   azul mediano
azul        grande          rojo grande     verde grande    azul grande
*/;

/*EL INNER ES COMO UN INTERSECCION*/
SELECT * FROM Employees e
INNER JOIN Orders o ON e.EmployeeID = o.EmployeeID;
/*EL ON ES LA CONDICION PARA UNIR LAS TABLAS NUESTRA CONDICION ESQ UE TENGA EL MISMO EMPLOYEEID LAS DISTINTAS ORDENES*/;

CREATE TABLE "Rewards" (
    "RewardID" INTEGER,
    "EmployeeIID" INTEGER,
    "Reward" INTEGER,
    "Month" TEXT,
    PRIMARY KEY("RewardID", AUTOINCREMENT)
)