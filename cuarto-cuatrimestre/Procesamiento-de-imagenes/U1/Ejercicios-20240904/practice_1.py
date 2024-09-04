import cv2
import numpy as np
import matplotlib.pyplot as plt

#1 Cargar la imagen
img = cv2.imread('cuarto-cuatrimestre/Procesamiento-de-imagenes/U1/Ejercicios-20240904/img_calculadora.tif', cv2.IMREAD_GRAYSCALE)
#2 Dimensiones de la imagen
img.shape
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False)
#3 Minimo y maximo de nivel de gris
min=np.min(img)
max=np.max(img)
print(min,max)
#4 Valores de nivel de gris
unique=np.unique(img)
unique_count=len(unique)
print(unique)
print(unique_count)
#5 mayor y menos repetitividad de nivel
unique_counter, counts = np.unique(img, return_counts=True)
min_count=counts.min()
max_count=counts.max()
print('Veces de repeticion min y max',min_count,max_count)

min_value = unique[np.where(counts == min_count)] # Esto toma todos por si se repiten
max_value = unique[np.where(counts == max_count)]
print('valores que se repiten min y max pero solo el primero que encuentra',min_value, max_value)

min_value_unique = unique[np.where(counts == min_count)[0][0]]
max_value_unique = unique[np.where(counts == max_count)[0][0]]
print('valores que se repiten min y max pero solo el primero que encuentra',min_value_unique, max_value_unique)

#6 Recortar teclas sin, cos y tan y mostrarlos usando subplots para cada tecla
sin = img[332:433, 729:882]
cos = img[332:433, 963:1109]
tan = img[332:433, 1186:1336]


plt.figure()

plt.subplot(131)
plt.imshow(sin, cmap='gray')
plt.title('Sin')

plt.subplot(132)
plt.imshow(cos, cmap='gray')
plt.title('Cos')

plt.subplot(133)
plt.imshow(tan, cmap='gray')
plt.title('Tan')

plt.tight_layout()
plt.show()