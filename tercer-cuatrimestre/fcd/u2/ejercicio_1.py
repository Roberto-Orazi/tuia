import pandas as pd

# Load all sheets from the Excel file
df = pd.read_excel("ejercicio_1.xlsx", sheet_name=None, header=4)

# Get the name of the first (and possibly only) sheet
nombre_unica_hoja = list(df.keys())[0]
print(nombre_unica_hoja)
df_hoja = df[nombre_unica_hoja]

# Obtener las columnas del DataFrame
columnas = df_hoja.columns
print("Columnas:", columnas)

# Si prefieres obtenerlas como una lista
columnas_lista = list(columnas)
print("Columnas como lista:", columnas_lista)

# Analyze the data
conteo_vuelos = df[nombre_unica_hoja]["vuelo "].value_counts()
print(conteo_vuelos)

# Get the flight with the most entries
numero_mas_vuelos = conteo_vuelos.keys()
mas_vuelos = conteo_vuelos.max()

print(
    f"El vuelo con mayor cantidad de fletes tuvo {mas_vuelos} vuelos y fue el vuelo {numero_mas_vuelos[0]}"
)

registros_vacios = df_hoja["vuelo "].isna().sum()
print(f"El número de registros vacíos en la columna 'vuelo ' es de: {registros_vacios}")

df_hoja_sin = df_hoja.dropna(how="all")

registros_vacios_sin = df_hoja_sin["vuelo "].isna().sum()
print(
    f"El número de registros vacíos en la columna 'vuelo ' es de: {registros_vacios_sin}"
)
