import pandas as pd


df = pd.read_excel("ejercicio_1.xlsx", sheet_name=None, header=4)


nombre_unica_hoja = list(df.keys())[0]


print(nombre_unica_hoja)

conteo_vuelos = data_hoja["vuelo "].value_counts()

print(conteo_vuelos)
numero_mas_vuelos = conteo_vuelos.keys()
mas_vuelos = conteo_vuelos.max()

print(
    f"El vuelo con mayor cantidad de fletes tuvo {mas_vuelos} vuelos y fue el vuelo {numero_mas_vuelos[0]}"
)
