import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(
    "tercer-cuatrimestre/fcd/u3/datasets_practica_unidad_3/winequality-red.csv"
)
variables = data.columns
tipos_variables = {}
for var in variables:
    tipo_variable = input(f"ingrese el tipo de variable de: {var}")
    tipos_variables[var] = tipo_variable

print(tipos_variables)

quantile_1 = data.quantile(0.25)
print(
    quantile_1[-2]
)  # 25% de los vinos tienen un contenido de alcohol superior a el valor

# 3
lista_variables = ["density", "pH"]
resultados = pd.DataFrame(
    columns=["Media", "Mediana", "Desvío estándar", "Rango intercuartil"]
)

for var in lista_variables:
    media = data[var].mean()
    mediana = data[var].median
    std = data[var].std()
    iqr = data[var].quantile(0.75) - data[var].quantile(0.24)

    resultados.loc[var] = [media, mediana, std, iqr]

print(resultados)

"""
Para ver la distribucion hay que ver la diferencia entre la media y la mediana Podemos ver que en la densidad son casi
iguales 0.996 y 0.997 mientras que en el ph es 3.31 de media contra 3.51 de mediana como la mediana es mayor que la
media sugiere que tiene una pequeña asimetria a la izquierda, distribuciones simetricas a la izquierda reducen la media.

El ph muestra mayor variabilidad porque tiene mayor desvio estandar, a mayor desvio mayor variabilidad
"""

# 4
plt.boxplot(data["alcohol"])
plt.title("Boxplot de Alcohol")
plt.ylabel("Alcohol")
plt.show()

"""
Podemos ver en el boxplot que tenemos un par de outliers en el limite superior, y tenemos una leve distribucion
asimetrica hacia la derecha, ya que no tenemos una distribucion normal podemos usar la mediana
"""

# 5
quality = data["quality"]
total_wine = len(quality)
print(total_wine)

tabla_frecuencias = quality.value_counts().sort_index()
print(tabla_frecuencias)

max_quality = tabla_frecuencias.idxmax()
max_count = tabla_frecuencias.max()
print(
    f"La calidad que mayor cantidad de vinos tuvo fue {max_quality} y tuvo {max_count} botellas"
)

min_quality = quality.min()
min_count = tabla_frecuencias.min()
min_perc = (min_count * 100) / total_wine
print(
    f"El porcentajes de los vinos que recibieron la calidad mas baja fue {min_perc:.2f}% y la calificacion mas baja fue {min_quality}"
)
