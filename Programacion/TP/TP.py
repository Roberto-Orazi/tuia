import matplotlib.pyplot as plt

datos = openFile2()
estructura_datos = estructura(datos)

# Get available editions
ediciones = estructura_datos["edicion"]
ediciones_disponibles = list(set(ediciones))

# Prompt user to select an edition
print("Ediciones disponibles:")
for i, edicion in enumerate(ediciones_disponibles):
    print(f"{i+1}. {edicion}")
selected_edicion_index = int(input("Ingrese el número de la edición seleccionada: ")) - 1
selected_edicion = ediciones_disponibles[selected_edicion_index]

# Calculate total travelers per province in the selected edition
viajeros_por_provincia = {}
for i, edicion in enumerate(ediciones):
    if edicion == selected_edicion:
        provincia_destino = estructura_datos["provincia_destino"][i]
        viajeros = int(estructura_datos["viajeros"][i])
        if provincia_destino in viajeros_por_provincia:
            viajeros_por_provincia[provincia_destino] += viajeros
        else:
            viajeros_por_provincia[provincia_destino] = viajeros

# Create bar chart
provincias = list(viajeros_por_provincia.keys())
viajeros_totales = list(viajeros_por_provincia.values())

plt.bar(provincias, viajeros_totales)
plt.xlabel("Provincia")
plt.ylabel("Total de Viajeros")
plt.title(f"Total de Viajeros por Provincia en la Edición {selected_edicion}")
plt.xticks(rotation=45)
plt.show()
