# 1FN
```
Una relacion esta en la primera forma normal si y solo si cada atributo tiene valor atomico para cada tupla.
```
No Cumple 1Fn ya que tiene multiples valores
| Pedido_ID | Producto                          | Categoria               | Precio   | Cliente_ID | Nombre          |
|-----------|-----------------------------------|-------------------------|----------|------------|-----------------|
| 1         | Laptop, Smartphone                | Electrónica             | 1200, 700| 101        | Juan, Juan      |
| 2         | Refrigerador                      | Electrodomésticos       | 1500     | 102        | María           |

Cumple con 1FN pero no con 2FN ya que nombre depende de cliente_id tambien, no solo de pedido_id
| Pedido_ID | Producto      | Categoria   | Precio   | Cliente_ID | Nombre     |
|-----------|---------------|-------------|----------|------------|------------|
| 1         | Laptop        | Electrónica | 1200     | 101        | Juan       |
| 2         | Smartphone    | Electrónica | 700      | 101        | Juan       |
| 3         | Refrigerador  | Electrodom. | 1500     | 102        | María      |
# 2FN
```
Una relacion esta en la segunda forma normal si y solo si esta en 1FN y todos los atributos no clave son completamente dependientes de la clave.
```
para que la tabla anterior cumpla 2fn tenemosq ue hacer una tabla cliente:
| Pedido_ID | Producto      | Categoria   | Precio   | Cliente_ID |
|-----------|---------------|-------------|----------|------------|
| 1         | Laptop        | Electrónica | 1200     | 101        |
| 2         | Smartphone    | Electrónica | 700      | 101        |
| 3         | Refrigerador  | Electrodom. | 1500     | 102        |

| Cliente_ID | Nombre  |
|------------|---------|
| 101        | Juan    |
| 102        | María   |
# 3FN
```
Una relacion esta en tercera forma normal si y solo si esta en 2FN y todos los atributos no clave dependen de manera no transitiva de la clave primaria.
```
La tabla anterior cumple 3fn ya que no hay dependencia transitiva