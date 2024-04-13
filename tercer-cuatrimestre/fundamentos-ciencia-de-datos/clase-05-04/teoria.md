## Poblacion y muestra
Poblacion: Es un conjunto total de elementos que comparten caracteristicas y que resultan de interes para un estudio particular

Muestra: Es un subconjunto de los elementos que constituyen la poblacion

## Variable

Es una caracteristica, cualidad o propiedad observada sobre alguna unidad determinada que puede asumir diferentes valores.
Osea es una caracteristica que uno puede cuantificar o medir como parte de un estudio/investigacion.

Las observaciones registradas de una o mas variables conforman un conjunto o set de datos.

En el formato largo, cada fila del dataset tiene un registro y cada columna contiene la informacion correspondiente a una variable.

### Cuantitativas y Cualitativas
Cualitativas o categoricas:
Son aquellas que no son medibles numericamente, ej: genero, barrio donde vive

Cuantitativas: Son aquellas que toman variables numericas, por lo general operaciones aritmeticas.
```
Discretas: Solo toman valores aislados en dicho intervalo. Por lo general son numeros enteros.
Ejemplos de variable discreta: número de empleados de una fábrica; número de hijos; número de cuentas ocultas en Suiza.
```
```
Continuas: Pueden asumir cualquier valor dentro de un intervalo. Por lo general son numeros reales
Ejemplos de variable continua: temperaturas registradas en un observatorio; tiempo en recorrer una distancia en una carrera; contenido de alcohol en un cuba-libre; estatura; tiempo de discurso de un político en las cortes insultando a los del partido contrario.
```

## Medidas de centralidad o posicion
Describen el centro de la distribucion de los datos.

- Media aritmetica / promedio
Es la suma de los valores observados de la variable x dividida por el numero total de datos de dicha variable.
Para calcularla contamos con el metodo mean() de pandas.

- Mediana (Q2)
La mediana o segundo cuartil se define como el valor de la variable que se encuentra en la posicion central del conunto de datos ordenado de menor a mayor. La mitad de las observaciones menores o iguales a ese valor central y la otra mitad son mayores
Si es impar:
1 2 3 4 5
tenemos que 3 es la Mediana
Si es par:
1 2 3 4 5 6
tenemos que agarrar los 2 valores centrales
3 y 4 y hacer el promedio de los 2 osea 3.5

tambien a veces tenemos que tenemos valores pares y tenemos por ejemplo los 2 numeros centrales iguales:
1 2 3 3 5 6
justo el promedio nos queda 3

```
Media vs Mediana
La media depende de todos los valores registrados de la variable. Algo muy grande o muy pequeño influye en el valor.
temperatura.mean()
La mediana es una medida de tendencia central mas representativa.
temperatura.median()
```

- Fractilas o cuantilos
Fractila de orden r es aquel valor de la variable tal que el r% de las observaciones del conjunto ordenado de datos o menores o iguales a el.
Cuartilos son un tipo de fractila que divide al conjunto de datos ordenados en 4 partes aproximada por el mismo numero de datos

quantile() es el metodo de pandas

Cuartil 1(Q1) es el valor que el 25 de los datos son menores o iguales a el
quantile(0.25)
Cuartil 2(Q2) es el valor que el 50 de los datos son menores o iguales a el
quantile(0.50)
Cuartil 3(Q3) es el valor que el 75 de los datos son menores o iguales a el
quantile(0.75)

- Modo o Moda
La moda es el valor de la variable que se presenta el mayor numero de veces osea la mayor frecuencia.
mode() es el metodo de pandas