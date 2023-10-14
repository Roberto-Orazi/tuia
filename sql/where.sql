SELECT ProductName FROM Products /*Puedo seleccionar tanto todos los campos como algun campo en especifico*/
WHERE ProductID = 14;
SELECT * FROM Products
WHERE ProductName = "Tofu";
SELECT * FROM Products
WHERE Price <= 40;
/*EL WHERE SE USA PARA FILTRAR O BUSCAR ALGO EN ESPECIFICO*/;
DELETE FROM Products
WHERE ProductId = 15;/*Nos elimina un registro especifico*/;

UPDATE Products SET ProductName = "Tofu salado", Price = 23
WHERE ProductID = 14;

