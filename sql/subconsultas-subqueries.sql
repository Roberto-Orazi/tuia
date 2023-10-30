/*Las subconsultas no alteran la base de datos. Se usan con SELECT*/;
/*Se suelen clasificar por muchas cosas por ejemplo por su resultado, si es una fila, resultado unico, etc PERO NO SE SUELE DECIR
QUE CLASIFICAMOS CON ESOS DATOS SINO QUE CON:
Tenemos Subconsulta tipo FROM, HAVING, SELECT*/;

SELECT  ProductID,
        Quantity,
        (SELECT ProductName FROM Products) as Nombre, /*SE PUEDEN HACER DE A 1 SUBCONSULTA YA QUE YO ESTOY LLAMANDO COLUMNAS NO PUEDO LLAMAR 2 COLUMNAS JUNTAS*/
        (SELECT CategoryId FROM Products)
FROM OrderDetails;


SELECT  ProductID as pID,
        Quantity,
        (SELECT ProductName FROM Products WHERE OD.pID = ProductID) as Nombre, /*SE PUEDEN HACER DE A 1 SUBCONSULTA YA QUE YO ESTOY LLAMANDO COLUMNAS NO PUEDO LLAMAR 2 COLUMNAS JUNTAS*/
        (SELECT Price FROM Products WHERE OD.pID = ProductID) as Precio
FROM OrderDetails AS OD; /*ESTO SE PUEDE HACER COMO FROM [OrderDeatils] OD ES LO MISMO*/

SELECT  ProductID, SUM(Quantity) AS Total_Vendido,
        (SELECT Price FROM Products WHERE ProductID = OD.ProductID) as Price,
        (SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Name,
        round((SUM(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID))) AS Total_Recaudado
FROM [OrderDetails] OD
WHERE Price > 40
GROUP BY ProductID
ORDER BY Total_Recaudado DESC;

/*POR EJEMPLO SI QUEREMOS FILTRAR POR PRECIO PERO NO QUEREMOS MOSTRARLO HACEMOS LO SIGUIENTE HACEMOS LA SUBCONSULTA DIRECTO EN EL WHERE*/
SELECT  ProductID, SUM(Quantity) AS Total_Vendido,
        (SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Name,
        round((SUM(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID))) AS Total_Recaudado
FROM [OrderDetails] OD
WHERE  (SELECT Price FROM Products WHERE ProductID = OD.ProductID) > 40
GROUP BY ProductID
ORDER BY Total_Recaudado DESC;