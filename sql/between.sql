SELECT * FROM Products WHERE Price BETWEEN 20 AND 40 OR CategoryID = 6
/*Esto nos reemplazaria el price > 20 and price < 40*/
/*Se puede usar tambien un NOT BETWEEN Y SERIA MENOR A 20 Y MAYOR A 40*/
SELECT * FROM Employees WHERE BirthDate BETWEEN "1960-0-1" AND "1970-0-1"
/*CON EL AND Y EL <> SE PUEDE TAMBIEN PERO EL OPERADOR CORRECTO ES BETWEEN*/
/*Incluye los limites osea seria un >= y <=*/
/*Siempre es del menor al mayor osea el primero tiene que ser menor al 2do*/
/*Hay que comparar siempre con mismos tipos de datos/formatos*/