## Lectura de archivos

```python
import pandas as pd

data = pd.read_csv('datasets/datos.csv')
data = pd.read_excel('datasets/datos.xlsx', sheet_name= 'hoja-01')
data = pd.read_json('datasets/datos.json')
```

## Lectura de archivos de datos tabulares

```python
import json
import pandas as pd

with open('datasets/datos.json', 'r') as f:
    datos = json.load(f)
```

```python
pd.read_parquet('datasets/datos.parquet', engine='auto', columns = None, storage_options=None, use_nullable_dtypes = False)
```

Ejemplo de clase
```python
import pandas as pd

datos = pd.dataframe({
    'nombre': ['Joaquin', 'Luciano', 'Mateo', 'Nancy'],
    'edad': [29, 15, 29, 24],
    'ciudad': ['Rosario', 'Madryn', 'Pueblo Esther', 'Casilda']

})

datos # Esto imprime mi dataframe

pd.DataFrame.to_csv

datos.to_csv(path = 'datos.csv', sep = ',', encoder = 'latin-1')

datos.info() # nos va a dar los tipos de datos, la cantidad de de valores que no tienen valores nulos

datos['Glucosa'] = [100.2, 98.6, 99.7, 100.2]

datos.loc[4] = ['Julian', np.nan, 25, np.nan]

datos.dtypes # Muestra la info de las columnas, osea que tipo de dato son
```

## Manejo de fechas

```python
from datetime import datetime
import pytz

zona_horaria=pytz.timezone('America/Argentina/Buenos_Aires')
fecha_aware = datetime(2024, 3, 15, 18, 00, 0 tzinfo = zona_horaria) # pasamos año, mes, dia, hora, minutos, segundos, y zona horaria via tzinfo


print('Horario de la clase virtual de fundamentos:', fecha_aware)


fecha_naive = datetime(2024, 3, 15, 18, 00, 0) # La diferencia con el aware es el detalle de la zona horaria

pd.to_datetime() metodo

# Por ejemplo tenemos nuestro dataframe llamado data tendriamos

data['Fecha_nacimiento']=pd.to_datetime(data['Fecha_nacimiento'], format = '%d/%m/%y')
reciente=data['Fecha_nacimiento'].max() # me traeria la fecha mas reciente
viejo=data['Fecha_nacimiento'].min() # me traeria la fecha menos reciente
recien - viejo # Nos va a dar un valor en dias

```python

## Formato ancho a formato largo

```python
import pandas as pd

data_long = pd.melt(
    data,
    id_vars=['id_persona', 'modo_elegido'], # Estos son los id que vamos a tomar como referencia
    value_vars=['tiempo_auto', 'tiempo_moto', 'tiempo_bus', 'tiempo_bici'] # Estos los valores que puede tomar nuestra variable
    var_name = 'modo', # Esto el nombre de nombre de la columna donde vamos a tener nuestras variables
    value_name = 'tiempo'
    )

# si ponemos pd.melt? me tira todas las variables que podemos ponerle y asi con todas las cosas de pandas

data_long['modo']=data_long['modo'].str.replace('tiempo_','')
```

## Ver las primeras 5 filas o ultimas

```python
data.head()

data.head(10) # las primeras 10

data.tail()

data.tail(10) # las ultimas 10

```

## Limpieza de datos faltantes

```python
data = pd.DataFrame = ([[1., 6.5, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan]])
columns = ['ColA', 'ColB', 'ColC']

data_dropped = data.dropna() # esto me elimina todas las filas que tengan al menos 1 na
# Hay que tener cuidado si tenemos una columna completa de na que conviene sacar la columna ya que sino nos quedamos sin datos

data_dropped = data.dropna(how = 'all') # esto me elimina todas las filas que tengan todo na
data_dropped = data.dropna(how = 'all' axis = 'columns') # esto me elimina todas las columnas que tengan todo na
```

## Remplazo de datos faltantes

- Podemos reemplazar los datos faltantes, con alguna medida resumen representativa como la media, mediana o el modo.
- Con un valor aleatorio
- Valor estimado mediante interpolacion

Vamos a ver un ejemplo con precios de departamentos de la ciudad de rosario, por distrito, zona, y cantidad de ambientes
```python
data['precio_usd'].isna() # esto nos da un booleano si es o no na

data.loc[data['precio_usd'].isna()] # esto nos da las filas en las cuales el parametro ese es na


# Vamos a calcular la media
media=round(data['precio_usd'].mean(), 2) # Rendodeamos la media con 2 decimales

data1=data.copy() # hacemos una copia

# Ahora vamos a rellenar los faltantes con la media que sacamos anteriormente

data1['precio_usd'] = data1['precio_usd'].fillna(media) # fillna(media, inplace=True) se puede hacer esto en vez de igualar

# Lo que nos pasa ahora es que es una media entre todos los barrios, por lo tanto vamos a segmentar segun barrio

(data.groupby('barrio'))['precio_usd'].mean().sort_values() # aca hacemos una media por barrio y ordenarlo de menor a mayor por defecto de la funcion sort value

data2=data.copy()
data2['precio_usd'] = data2['precio_usd'].fillna((data.groupby('barrio'))['precio_usd'].transform('mean'))
# Tenemos que usar el transform ya que te transforma el valor na por la media del groupby
# Tener en cuenta que tambien la mediana conviene mas que el promedio por los valores muy distantes que me afectan en el promedio
```

```
Imputacion por interpolacion

Tenemos:
- interpolacion lineal
- interpolacion polinomica
```

## Combinaciones de conjuntos de datos

```
En pandas tenemos varios metodos para combinar df:
- merge()
- concat()
- join()
```

```python
df1=pd.DataFrame({'A': [1,2,3], 'B': [4,5,6], index = [0,1,2]})

df1=pd.DataFrame({'A': [4,5,6], 'B': [7,8,9], 'C': [10,11,12], index = [3,4,5]})

nuevo_df = pd.concat([df1,df2], axis = 0)

```