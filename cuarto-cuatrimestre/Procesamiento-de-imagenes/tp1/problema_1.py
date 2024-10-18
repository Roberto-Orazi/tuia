import matplotlib

matplotlib.use("TkAgg")
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error reading the image")
else:
    img_eq = cv2.equalizeHist(img)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img_eq, cmap="gray")
    plt.title("Equalize image")
    plt.axis("off")

    plt.show()


"""
AYUDA: Con la siguiente función, puede agregar una cantidad fija de pixels a una imagen: cv2.copyMakeBorder(img, top,
bottom, left, right, borderType), donde top, bottom, left y right son valores enteros que definen la cantidad de píxeles
a agregar arriba, abajo, a la izquierda y a la derecha, respectivamente, y borderType define el valor a utilizar. Por
ejemplo, borderType = cv2.BORDER_REPLICATE replica el valor de los bordes.
"""
