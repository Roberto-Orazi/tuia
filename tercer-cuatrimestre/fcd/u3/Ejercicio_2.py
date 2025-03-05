import pandas as pd
import matplotlib.pyplot as plt


data_alimentos = pd.read_csv(
    "tercer-cuatrimestre/fcd/u3/datasets_practica_unidad_3/alimentos.csv",
    encoding="latin1",
    sep=";",
)
data_pacientes = pd.read_csv(
    "tercer-cuatrimestre/fcd/u3/datasets_practica_unidad_3/pacientes.csv",
    sep=";",
)

data_alimentos.head()
data_pacientes.head()

len(data_alimentos)
len(data_pacientes)

data_pacientes = data_pacientes.dropna()
data_alimentos = data_alimentos.dropna()

len(data_alimentos)
len(data_pacientes)

"""
Despues de checkear esto podemos ver que no hay na en ninguno de los 2 datasets ya que borramos los na y hay la misma
cantidad de filas
"""

# 2
kcal = data_alimentos["aporte_calorico_kcal"]
kcal_mean = kcal.mean()
print(kcal)
print(
    f"En promedio los alimentos del data set tienen un promedio de {kcal_mean} calorias"
)

print(f"El 50% de los aportes caloricos son menores o iguales a {kcal.quantile(.5)}")

rango_iqr = kcal.quantile(0.75) - kcal.quantile(0.25)
print(f"El rango en el que se encuentra el 50% es {rango_iqr}")

print(f"Los valores que se presentan con mayor frecuencia son {kcal.mode()}")

# 3
plt.boxplot(kcal)
plt.title("Boxplot de calorias")
plt.ylabel("Aporte calorico")
plt.show()

"""
Para empezar podemos ver que la distribucion de esto tiene una asimetria a la derecha, se ve bien la cantidad de valores
atipicos que tiene.

Para centralidad posicion conviene usar la mediana ya que no tiene distribucion normal, y para lo que es dispersion
conviene usar rango intercuartil ya que siempre que haya asimetria o presencia de valores atipicos conviene usarlo antes
que rango o desviacion standar.
"""

# 4
tipos_de_alimentos = data_alimentos.groupby("tipo_de_alimento")[
    "aporte_calorico_kcal"
].median()
print(
    f"Los alimentos {tipos_de_alimentos.idxmax()} tienen la mayor mediana de aporte calorico"
)

# 5
lista_alimentos_boxplot = ["fruta", "verdura", "elaborada"]
data_alimentos_boxplot = data_alimentos[
    data_alimentos["tipo_de_alimento"].isin(lista_alimentos_boxplot)
]
data_alimentos_boxplot.boxplot(
    column="aporte_calorico_kcal", by="tipo_de_alimento", grid=False
)
plt.title("Boxplot de alimentos como fruta, verdura y elaborados")
plt.ylabel("verduras")
plt.show()

"""
Podemos ver en este boxplot que el mas variable es la elaborada con un rango muchisimo mas grande si se nota que tanto
en fruta tipo de alimento y verdura tienen un rango similar, pero tienen distinta distribucion, bigotes, media, median,
y fruta tiene un outlier que es la unica de las 3 variables que la tiene. El menor variable es fruta.
"""

# 6
diferencia_de_peso = data_pacientes["peso_final_kg"] - data_pacientes["peso_inicial_kg"]
print(diferencia_de_peso)
data_pacientes["diferencia_de_peso"] = 0
data_pacientes["diferencia_de_peso"] = diferencia_de_peso
data_pacientes["diferencia_de_peso"]
data_por_sexo = data_pacientes.groupby("sexo")

data_pacientes.boxplot(column="diferencia_de_peso", by="sexo")
plt.title("Boxplot de diferencia de pesos entre sexos")
plt.xlabel("Diferencia de peso")
plt.show()

"""
Podemos ver que en los masculinos pareciera tener una distribucion normal en la cual podemos evaluarla con la media, que
a diferencia del femenino notamos cierta asimetria hacia la izquierda donde tenemos valores atipicos en los valores mas
chicos
"""
