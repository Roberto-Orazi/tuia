import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------
# --- Filtro Sobel - Diferentes implentaciones -------------------------------------------------
# ----------------------------------------------------------------------------------------------
# --- Cargo Imagen --------------------------------------------------------------
img = cv2.imread(
    "cameraman.tif",
    cv2.IMREAD_GRAYSCALE,
)
print(img.dtype)


plt.figure()
plt.imshow(img, cmap="gray")
plt.show(block=False)

# --- Filtro Sobel --------------------------------------------------------------
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
grad_x = cv2.filter2D(img, -1, sobel_x)
grad_y = cv2.filter2D(img, -1, sobel_y)

grad_x2 = cv2.Sobel(
    img, -1, 1, 0, ksize=3
)  # https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#gacea54f142e81b6758cb6f375ce782c8d
grad_y2 = cv2.Sobel(
    img, -1, 0, 1, ksize=3
)  # Tutorial: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html

abs((grad_x - grad_x2)).max()  # son idénticos....
abs((grad_y - grad_y2)).max()  # son idénticos....

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(grad_x, cmap="gray"), plt.title("Sobel x - filter2D()")
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(grad_y, cmap="gray"), plt.title(
    "Sobel y - filter2D()"
)
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(grad_x2, cmap="gray"), plt.title(
    "Sobel x - Sobel()"
)
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(grad_y2, cmap="gray"), plt.title(
    "Sobel y - Sobel()"
)
plt.show()

# ----------------------------------------------------------------------------------------------
# --- Filtro Sobel - Tipo de dato --------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# --- Imagen de entrada -----------------------------------------
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
plt.figure(), plt.imshow(img, cmap="gray"), plt.show(block=False)

# --- Filtro Sobel ----------------------------------------------
sobel_x_8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)  # Filtrado utilizando uint8
sobel_x_64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Filtrado utilizando float 64
np.unique(sobel_x_8u)
np.unique(sobel_x_64f)

# --- Figuras ---------------------------------------------------
plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(
    sobel_x_8u, cmap="gray"
), plt.title("Sobel x - uint8"), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(
    sobel_x_64f, cmap="gray"
), plt.title("Sobel x - float 64"), plt.colorbar()
plt.show(block=False)

# --- Analizo valores ------------------------------------------- Transiciones de "negro"  (  0) a "blanco" (255) -->
# Generan valores positivos Transiciones de "blanco" (255) a "negro"  (  0) --> Generan valores negativos sobel_x =
# np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Transición de "negro"  (  0) a "blanco" (255) --> Generan valores positivos
img[48:53, 48:53]
sobel_x_8u[48:53, 48:53]
sobel_x_64f[48:53, 48:53]

# Transición de "blanco" (255) a "negro"  (  0) --> Generan valores negativos
img[48:53, 147:152]
sobel_x_8u[48:53, 147:152]
sobel_x_64f[48:53, 147:152]

# --- Conversión ------------------------------------------------
sobel_x_64f_to_8u = cv2.convertScaleAbs(
    sobel_x_64f
)  # convertScaleAbs(src,dst,alpha,beta) --> saturate_cast<uchar>(|src*alpha+ beta|)
np.unique(sobel_x_64f_to_8u)
sobel_x_64f_to_8u[48:53, 147:152]

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(
    sobel_x_8u, cmap="gray"
), plt.title("Sobel x - uint8"), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(
    sobel_x_64f, cmap="gray"
), plt.title("Sobel x - float 64"), plt.colorbar()
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(
    sobel_x_64f_to_8u, cmap="gray"
), plt.title("Sobel x - float 64 --> convertScaleAbs"), plt.colorbar()
plt.show(block=False)

# ----------------------------------------------------------------------------------------------
# --- Filtro Sobel - Combinacion  --------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# --- Imagen de entrada -----------------------------------------
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
plt.figure(), plt.imshow(img, cmap="gray"), plt.show(block=False)

# --- Sobel x e y -----------------------------------------------
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# --- Combino ---------------------------------------------------
sobel_xy = sobel_x + sobel_y
np.unique(sobel_xy)

sobel_xy[48:53, 48:53]  # Transición de "negro"  (  0) a "blanco" (255)
sobel_x[48:53, 48:53]  # Para analizar en la esquina superior-derecha...
sobel_y[48:53, 48:53]  # ...

sobel_xy[48:53, 147:152]  # Transición de "blanco" (255) a "negro"  (  0)
sobel_x[48:53, 147:152]  # Para analizar en la esquina superior-derecha...
sobel_y[48:53, 147:152]  # ...

# --- Casting ---------------------------------------------------
sobel = cv2.convertScaleAbs(sobel_xy)
np.unique(sobel)
sobel[48:53, 48:53]  # Transición de "negro"  (  0) a "blanco" (255)
sobel[48:53, 147:152]  # Transición de "blanco" (255) a "negro"  (  0)

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(sobel_xy, cmap="gray"), plt.title(
    "Sobel xy"
), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(sobel, cmap="gray"), plt.title(
    "Sobel"
), plt.colorbar()
plt.show(block=False)

# --- Mejoras en la combinación: Casting y luego combino (la mas utilizada) -----------------------
sobel_x2 = cv2.convertScaleAbs(sobel_x)
sobel_y2 = cv2.convertScaleAbs(sobel_y)
np.unique(sobel_x2)
np.unique(sobel_y2)
sobel_2 = cv2.addWeighted(sobel_x2, 0.5, sobel_y2, 0.5, 0)
np.unique(sobel_2)

# *** Por qué así no? *********************************************************** sobel_3 = sobel_x2 + sobel_y2
# np.unique(sobel_3) sobel_3[48:53, 48:53]     # Transición de "negro"  (  0) a "blanco" (255) sobel_3[48:53, 147:152]
# # Transición de "blanco" (255) a "negro"  (  0)
# *******************************************************************************

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(sobel_xy, cmap="gray"), plt.title(
    'float - "+"'
), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(sobel, cmap="gray"), plt.title(
    'float - "+" - convertScaleAbs'
), plt.colorbar()
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(sobel_2, cmap="gray"), plt.title(
    "convertScaleAbs - addWeighted(0.5)"
), plt.colorbar()
plt.suptitle("Sobel")
plt.show(block=False)

# --- Otra opción de combinación (menos frecuente) -------------------------------------------
sobel_3 = cv2.addWeighted(sobel_x2, 1, sobel_y2, 1, 0)
np.unique(sobel_3)

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(sobel, cmap="gray"), plt.title(
    'float - "+" - convertScaleAbs'
), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(sobel_2, cmap="gray"), plt.title(
    "convertScaleAbs - addWeighted(0.5)"
), plt.colorbar()
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(sobel_3, cmap="gray"), plt.title(
    "convertScaleAbs - addWeighted(1.0)"
), plt.colorbar()
plt.suptitle("Sobel")
plt.show(block=False)


# ----------------------------------------------------------------------------------------------
# --- Filtro Sobel - Combinacion - Ejemplo sobre imagen real -----------------------------------
# ----------------------------------------------------------------------------------------------
# --- Cargo Imagen --------------------------------------------------------------
img = cv2.imread(
    "cuarto-cuatrimestre/Procesamiento-de-imagenes/U2/codigo/cameraman.tif",
    cv2.IMREAD_GRAYSCALE,
)
plt.figure(), plt.imshow(img, cmap="gray"), plt.show(block=False)

# --- Sobel ---------------------------------------------------------------------
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_xy = sobel_x + sobel_y
sobel = cv2.convertScaleAbs(sobel_xy)

sobel_x2 = cv2.convertScaleAbs(sobel_x)
sobel_y2 = cv2.convertScaleAbs(sobel_y)
sobel_2 = cv2.addWeighted(sobel_x2, 0.5, sobel_y2, 0.5, 0)
sobel_3 = cv2.addWeighted(sobel_x2, 1, sobel_y2, 1, 0)

plt.figure()
ax1 = plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.title("Imagen"), plt.colorbar()
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(sobel, cmap="gray"), plt.title(
    'float - "+" - convertScaleAbs'
), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(sobel_2, cmap="gray"), plt.title(
    "convertScaleAbs - addWeighted(0.5)"
), plt.colorbar()
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(sobel_3, cmap="gray"), plt.title(
    "convertScaleAbs - addWeighted(1.0)"
), plt.colorbar()
plt.suptitle("Sobel")
plt.show(block=False)
