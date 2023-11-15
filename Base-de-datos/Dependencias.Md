# Dependencias Funcionales
Se refiere a la relación entre dos conjuntos de atributos en una tabla.
Si dos conjuntos de atributos, A y B, están en una relación tal que para cada valor único de A hay un único valor correspondiente de B, entonces se dice que B depende funcionalmente de A.
Esto se denota como A -> B.

Si tenemos t1,t2 tuplas de R tal que:

R={A1,A2,...,An}
X->Y
```
t1[X]=t2[X]
Tenemos
t1[Y]=t2[Y]
```
Los valores de **Y** de la tupla r dependen de los valores de **X**

```
| ID_empleado | Nombre | Departamento | Salario |
| ----------- | ------ | ------------ | ------- |
| 1           | Juan   | Ventas       | 50000   |
| 2           | María  | Marketing    | 55000   |
| 3           | Carlos | Ventas       | 48000   |

Disclaimer, en departamento usar el nombre de departamento en vez de id_dep es mala practica, solo esta hecho asi para mayor facilidad lectora. salu3

| ID_departamento | Nombre    | Localizacion |
| --------------- | --------- | ------------ |
| 1               | Ventas    | Ciudad A     |
| 2               | Marketing | Ciudad B     |
```


## Dependencia Funcional Total
Si la eliminacion de cualquier atributo A de **X** hace que la dependencia deje de ser valida.

- X={ID_empleado}
- Y={Nombre, Departamento, Salario}

La dependencia funcional total sería:
- {ID_empleado}→{Nombre, Departamento, Salario}

```
Esto significa que dado un ID_empleado, puedes determinar de manera única todos los atributos relacionados: Nombre, Departamento y Salario.
```

## Dependencia Funcional Parcial
Si es posible eliminar un atributo de A de **X** y la dependencia sigue siendo valida.

- X={ID_empleado}
- Y={Nombre, Salario}

La dependencia funcional parcial sería:
- {ID_empleado}→{Nombre, Salario}
```
Esto significa que aunque solo se conozca el ID_empleado, puedes determinar de manera única el Nombre y el Salario, pero no necesariamente el Departamento.
```

### Diferencia entre total y parcial
```
la dependencia funcional total implica que el conjunto
X determina todos los atributos en Y, mientras que la dependencia funcional parcial implica que X determina solo algunos atributos en Y.
```

## Dependencia Funcional Transitiva
Una dependencia **X -> Y** es dft si existe un conjunto de atributos **Z** que no sea parte de
cualquier clave y se cumple tanto **X -> Z** y  **Z -> Y**

Por ejemplo:
- X={ID_empleado}
- Y={Localizacion}
- Z={Departamento}

1. ID_empleado→Nombre (cada ID_empleado determina de manera única el Nombre)
2. (Z->Y)Departamento→Localizacion (cada nombre de departamento determina de manera única la localización)
3. (X->Z)ID_empleado→Departamento (cada ID_empleado determina de manera única el Departamento)