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
);

INSERT INTO Rewards (EmployeeID,Reward,Month) VALUES

(3, 200, 'January'),
(2, 180, 'February'),
(5, 200, 'March'),
(1, 280, 'April'),
(8, 160, 'May'),
(null, null, 'June');

SELECT FirstName,Reward, Month FROM Employees e
INNER JOIN Rewards r ON e.EmployeeID = r.EmployeeID
RIGHT JOIN Employees e ON e.EmployeeID = r.EmployeeID /*el right es lo contrario al left agarra la parte derecha de la interseccion + la interseccion de las tablas*/
LEFT JOIN Rewards r ON e.EmployeeID = r.EmployeeID;
/*El left join Nos devuelve la tabla de empleados + la interseccion con la tabla B que seria la de rewards y month
Osea que pasa la tabla de firstName la devuelve completa por lo tanto los empleados que no tienen rewards van a aparecer null
*/;

SELECT FirstName,Reward, Month FROM Rewards r
LEFT JOIN Employees e ON e.EmployeeID = r.EmployeeID;
/*Algunos programas no nos dejan usar right join por lo cual invertimos las tablas y listo*/;

/*FULL JOIN*/
/*SERIA UNA UNION DE CONJUNTOS*/
/*SIMULAMOS UN FULL JOIN UNIENDO UN LEFT JOIN CON UN RIGHT JOIN PASA QUE SI USAMOS UN UNION ALL SE REPITEN LOS DATOS YA QUE TENEMOS DATOS DUPLICADOS*/;


