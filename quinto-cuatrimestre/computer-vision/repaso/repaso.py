import numpy as np
import matplotlib.pyplot as plt
import requests
import cv2

# Ejercicio 1
imagen = np.zeros((150, 150, 3), dtype=np.uint8)

centro = 150 // 2
tamaño_cuadrado = 50

inicio = centro - tamaño_cuadrado // 2
fin = centro + tamaño_cuadrado // 2

imagen[inicio:fin, inicio:fin] = [255, 0, 0]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 2)
plt.imshow(imagen)
plt.title(f"Cuadrado {tamaño_cuadrado}x{tamaño_cuadrado} en imagen 150x150")
plt.grid(True, alpha=0.3)
plt.show()

imagen_con_verde = imagen

imagen_con_verde[0:30, 0:60] = [0, 255, 0]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 2)
plt.imshow(imagen_con_verde)
plt.title(f"Cuadrado {tamaño_cuadrado}x{tamaño_cuadrado} en imagen 150x150")
plt.grid(True, alpha=0.3)
plt.show()


canal_rojo = imagen_con_verde[:, :, 0]
canal_verde = imagen_con_verde[:, :, 1]
canal_azul = imagen_con_verde[:, :, 2]

# Crear una figura con 4 subplots
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(imagen_con_verde)
plt.title("Imagen Original (RGB)")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(canal_rojo, cmap="Reds")

plt.title("Canal Rojo")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(canal_verde, cmap="Greens")

plt.title("Canal Verde")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(canal_azul, cmap="Blues")

plt.title("Canal Azul")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"Forma: {imagen_con_verde.shape}")
print(f"Tipo: {imagen_con_verde.dtype}")

# Ejercicio 2
url = (
    "https://raw.githubusercontent.com/jpmanson/tuia-unr/main/images/big_buck_bunny.jpg"
)

respuesta = requests.get(url)
bytes_imagen = np.array(bytearray(respuesta.content), dtype=np.uint8)
imagen_github = cv2.imdecode(bytes_imagen, cv2.IMREAD_COLOR)

canal_rojo = imagen_github[:, :, 0]
canal_verde = imagen_github[:, :, 1]
canal_azul = imagen_github[:, :, 2]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(imagen_github)
plt.title("Imagen Original (RGB)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(canal_rojo, cmap="Reds")

plt.title("Canal Rojo")
plt.axis("off")

plt.tight_layout()
plt.show()

promedio_rojo = np.mean(canal_rojo)
promedio_verde = np.mean(canal_verde)
promedio_azul = np.mean(canal_azul)

print("INTENSIDADES PROMEDIO")
print(f"Canal Rojo:  {promedio_rojo:.2f}")
print(f"Canal Verde: {promedio_verde:.2f}")
print(f"Canal Azul:  {promedio_azul:.2f}")
print(f"Promedio general: {(promedio_rojo + promedio_verde + promedio_azul)/3:.2f}")

# Ejercicio 3 3.a
gris_ponderado = (canal_rojo * 0.299) + (canal_verde * 0.587) + (canal_azul * 0.114)

# 3.b
gris_promedio = (canal_rojo + canal_verde + canal_azul) / 3

# 3.c
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagen_github, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gris_ponderado, cmap="gray")
plt.title("Escala de Grises (Ponderada)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(gris_promedio, cmap="gray")
plt.title("Escala de Grises (Promedio)")
plt.axis("off")

# 3.d - Calcular diferencia absoluta promedio
diferencia = np.abs(gris_ponderado - gris_promedio)

plt.subplot(2, 2, 4)
plt.imshow(diferencia, cmap="hot")
plt.title("Diferencia entre Métodos")
plt.axis("off")

plt.tight_layout()
plt.show()

# 3.d - Estadísticas
diferencia_promedio = np.mean(diferencia)
print(f"\nEJERCICIO 3 - RESULTADOS:")
print(f"Diferencia absoluta promedio: {diferencia_promedio:.2f}")
print(f"Diferencia máxima: {np.max(diferencia):.2f}")
print(f"Promedio ponderado: {np.mean(gris_ponderado):.2f}")
print(f"Promedio simple: {np.mean(gris_promedio):.2f}")

# Ejercicio 4
imagen_copia = imagen_github.copy()
rojo_ej4 = imagen_copia[:, :, 0]
verde_ej4 = imagen_copia[:, :, 1]
azul_ej4 = imagen_copia[:, :, 2]

# 4.a
rojo_ej4 = 255 - rojo_ej4
verde_ej4 = 255 - verde_ej4
azul_ej4 = 255 - azul_ej4
imagen_negativo = 255 - imagen_copia

# 4.b
imagen_brillo = np.clip(imagen_copia.astype(np.int16) + 50, 0, 255).astype(np.uint8)

# 4.c
imagen_rotada = imagen_copia.copy()
imagen_rotada[:, :, 0] = imagen_copia[:, :, 2]
imagen_rotada[:, :, 2] = imagen_copia[:, :, 0]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagen_copia, cv2.COLOR_BGR2RGB))
plt.title("4. Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(imagen_negativo, cv2.COLOR_BGR2RGB))
plt.title("4a. Negativo")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(imagen_brillo, cv2.COLOR_BGR2RGB))
plt.title("4b. Brillo +50")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(imagen_rotada, cv2.COLOR_BGR2RGB))
plt.title("4c. R-B Intercambiados")
plt.axis("off")

plt.tight_layout()
plt.show()

# Ejercicio 5

# 5.a
url_berenjenas = (
    "https://raw.githubusercontent.com/jpmanson/tuia-unr/main/images/berenjenas.jpg"
)

respuesta_ber = requests.get(url_berenjenas)
bytes_ber = np.array(bytearray(respuesta_ber.content), dtype=np.uint8)
imagen_berenjenas = cv2.imdecode(bytes_ber, cv2.IMREAD_COLOR)

h1, w1 = imagen_github.shape[:2]
h2, w2 = imagen_berenjenas.shape[:2]

nuevo_h = min(h1, h2)
nuevo_w = min(w1, w2)

img1 = cv2.resize(imagen_github, (nuevo_w, nuevo_h))
img2 = cv2.resize(imagen_berenjenas, (nuevo_w, nuevo_h))

# 5.b
blend = 0.5 * img1.astype(np.float64) + 0.5 * img2.astype(np.float64)
blend = np.clip(blend, 0, 255).astype(np.uint8)

# 5.c
resta = img1.astype(np.int16) - img2.astype(np.int16)
resta = np.clip(resta, 0, 255).astype(np.uint8)

# 5.d
img1_verde_mult = img1.copy()
img1_verde_mult[:, :, 1] = np.clip(
    img1_verde_mult[:, :, 1].astype(np.float64) * 1.5, 0, 255
)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("5a. Imagen 1 (Big Buck Bunny)")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("5a. Imagen 2 (Berenjenas)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(blend, cv2.COLOR_BGR2RGB))
plt.title("5b. Blend (α=0.5)")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(resta, cv2.COLOR_BGR2RGB))
plt.title("5c. Resta (img1 - img2)")
plt.axis("off")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1_verde_mult, cv2.COLOR_BGR2RGB))
plt.title("5d. Canal Verde x1.5")
plt.axis("off")

plt.subplot(1, 2, 2)
verde_orig = img1[:, :, 1]
verde_mult = img1_verde_mult[:, :, 1]
plt.imshow(verde_mult - verde_orig, cmap="Greens")
plt.title("Diferencia Canal Verde")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"\nEJERCICIO 5 - RESULTADOS:")
print(f"Tamaño final de imágenes: {nuevo_w}x{nuevo_h}")
print(f"Blend promedio: {np.mean(blend):.2f}")
print(f"Resta promedio: {np.mean(resta):.2f}")
print(f"Canal verde original promedio: {np.mean(img1[:,:,1]):.2f}")
print(f"Canal verde multiplicado promedio: {np.mean(img1_verde_mult[:,:,1]):.2f}")
