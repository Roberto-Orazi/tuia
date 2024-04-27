## Lectura de archivos

```
import pandas as pd

data = pd.read_csv('datasets/datos.csv')
data = pd.read_excel('datasets/datos.xlsx', sheet_name= 'hoja-01')
data = pd.read_json('datasets/datos.json')
```

## Lectura de archivos de datos tabulares

```
import json
import pandas as pd

with open('datasets/datos.json', 'r') as f:
    datos = json.load(f)
```

```
pd.read_parquet('datasets/datos.parquet', engine='auto', columns = None, storage_options=None, use_nullable_dtypes = False)
```

Ejemplo de clase
```
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

```
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

```

## Formato ancho a formato largo

```
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

```
data.head()

data.head(10) # las primeras 10

data.tail()

data.tail(10) # las ultimas 10

```