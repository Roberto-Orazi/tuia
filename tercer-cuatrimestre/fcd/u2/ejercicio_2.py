import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv(
        "incendios-cantidad-causas-provincia_2022.csv", encoding="latin1", skiprows=3
    )
    print(df.columns)
except FileNotFoundError:
    print("El archivo no se encuentra en el directorio especificado.")
except pd.errors.ParserError as e:
    print(f"Error al analizar el archivo: {e}")
except UnicodeDecodeError as e:
    print(f"Error de codificación: {e}")


# 2.1

total_incendio_por_anio = df.groupby("anio")["total"].sum()
anio_mayor = total_incendio_por_anio.idxmax()
mayor_numero = total_incendio_por_anio.max()
print(
    f"el año con mayor incendio fue {anio_mayor} con un numero total de {mayor_numero}"
)

# 2.2
print(df["provincia"].unique())
total_incendio_cordoba = df[
    (df["provincia"] == "Córdoba") & (df["anio"] > 1993) & (df["anio"] < 2021)
]["total"].sum()
print(total_incendio_cordoba)

# 2.3
datos_por_provincia_anio = (
    df.groupby(["anio", "provincia"])["intencional"].sum().reset_index()
)
print(datos_por_provincia_anio)

max_provincia_por_anio = datos_por_provincia_anio.loc[
    datos_por_provincia_anio.groupby("anio")["intencional"].idxmax()
]
print(max_provincia_por_anio)

# 2.4
df_santa_fe = df[
    (df["provincia"] == "Santa Fe") & (df["anio"] > 2014) & (df["anio"] < 2022)
]
print(df_santa_fe)
df_filtrado = df_santa_fe.groupby("anio")[
    ["intencional", "negligencia", "natural"]
].sum()
print(df_filtrado)


x = np.arange(len(df_filtrado.index))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width, df_filtrado["intencional"], width, label="Intencional")
ax.bar(x, df_filtrado["negligencia"], width, label="Negligencia")
ax.bar(x + width, df_filtrado["natural"], width, label="Natural")


ax.set_xlabel("Año")
ax.set_ylabel("Número de Incendios")
ax.set_title("Incendios en Santa Fe (2015-2021)")
ax.set_xticks(x)
ax.set_xticklabels(df_filtrado.index)
ax.legend()

plt.tight_layout()
plt.show()
