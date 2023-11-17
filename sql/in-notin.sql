/*OPERADOR IN*/
SELECT * FROM Products
WHERE SupplierID = 3
OR SupplierID = 4
AND SupplierID = 5
AND SupplierID = 6

/*EL OPERADOR IN RESUELVE TODO CON:*/
SELECT * FROM Products
WHERE SupplierID IN (3,4,5,6)

SELECT * FROM Employees
WHERE LastName IN ("Fuller", "King")

/*EL OPERADOR NOT IN DEVUELVE TODO LO DEMAS*/
SELECT * FROM Products
WHERE SupplierID NOT IN (3,4,5,6)

