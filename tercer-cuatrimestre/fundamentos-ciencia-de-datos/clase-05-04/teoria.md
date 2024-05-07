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

```python
df['peso_kg'].mode()
```
Imprime
0 72.8
Name: peso_kg, dtype: float64


## Rango
Es la diferencia entre el mayor y menor valor observado de la variable
```python
rango=round(df['peso_kg'].max() - df['peso_kg'].min(),1)
```
Seria el spread entre el menor y el mayor

## Variancia(S²)
Es una medida de cuanto se desvian en promedio. las observaciones de una variable con respecto a la media aritmetica.
A mayor variabilidad mayor variancia obvioo
```python
variancia=round(df['peso_kg'].var(),1) # Esto nos va a devolver en nuestro caso kg²
```

## Desviacion estandar (S)
Se define como la raiz cuadrada positiva de la variancia.
Es como una distancia promedio de las observaciones con respecto a la media
```python
desviacion_est=round(df['peso_kg'].std(),1) # Esto al ser la raiz de la varianza va a devolver kg en este caso
```
## Metodo .describe()
Dependiendo en que columna lo usamos imprime lo siguiente:

```python
df['peso_kg'].describe() # Esto es Cuantitativa
'''
count
mean
std
min
25%
50%
75%
max
name: peso_kg, dtype:float64
'''
```


```python
df['actividad'].describe() # Cualitativa
'''
count
unique
top
freq
name: actividad, dtype:float64
'''
```

## Boxplots

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x='peso_kg', data=df, showfliers = False) # Usamos el showfliers para mostrar o ocultar los outliers
plt.show

sns.boxplot(x='peso_kg', data=df, whis = [0,100]) # Usamos el whis para los bigotes/whiskers
```

## Tabla de frecuencias
Puede construirse haciendo el value_counts() de pandas
En la version mas simple:
```python
df['actividad'].value_counts()
```

Tabla frecuencia absoluta y relativa mas linda
```python
# Tabla frecuencia absoluta
tabla_actividad = df['actividad'].value_counts().reset_index()
tabla_actividad.rename(columns = {'actividad': 'Actividad', 'count': 'Frec_absoluta'}, inplace=True)
tabla_actividad = tabla_actividad.set_index('Actividad')

# Tabla frecuencia relativa
tabla_actividad['Frec_relativa'] = round(tabla_actividad['Frec_absoluta']/sum(tabla_actividad['Frec_absoluta']), 2)

tabla_actividad['Porcentaje'] = round(tabla_actividad['Frec_absoluta']*100/sum(tabla_actividad['Frec_absoluta']), 2)
```