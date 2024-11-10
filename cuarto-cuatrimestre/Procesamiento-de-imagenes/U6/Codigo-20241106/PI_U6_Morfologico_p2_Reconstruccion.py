import cv2
import numpy as np
import matplotlib.pyplot as plt


# Defininimos funcion para mostrar imágenes
def imshow(
    img,
    new_fig=True,
    title=None,
    color_img=False,
    blocking=False,
    colorbar=False,
    ticks=False,
):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap="gray")
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:
        plt.show(block=blocking)


# ---------------------------------------------------------------------------------------
# --- Reconstrucción Morgológica --------------------------------------------------------
# ---------------------------------------------------------------------------------------
def imreconstruct(marker, mask, kernel=None):
    if kernel == None:
        kernel = np.ones((3, 3), np.uint8)
    while True:
        expanded = cv2.dilate(marker, kernel)  # Dilatacion
        expanded_intersection = cv2.bitwise_and(
            src1=expanded, src2=mask
        )  # Interseccion
        if (marker == expanded_intersection).all():  # Finalizacion?
            break  #
        marker = expanded_intersection
    return expanded_intersection


# ------------------------------------------
# --- Apertura por Reconstruccion ---------------------------------------------
# ------------------------------------------
# Se pretende detectar los caracteres que tienen una linea vertical larga (h, l, n, p, etc.).
f = cv2.imread("book_text_bw.tif", cv2.IMREAD_GRAYSCALE)
print(f.dtype)
print(np.unique(f))
imshow(f, title="Imagen Original")

# Primero, intentamos utilizando solamente la apertura morfolófica.
kernel = np.ones((51, 1))
fo = cv2.morphologyEx(f, cv2.MORPH_OPEN, kernel)

plt.figure()
ax1 = plt.subplot(121)
imshow(f, new_fig=False, title="Original")
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(fo, new_fig=False, title="Apertura")
plt.show(block=False)

# Ahora intentamos con el método de Apertura por Reconstrucción
fe = cv2.erode(f, kernel, iterations=1)
fobr = imreconstruct(fe, f)
imshow(fobr, title="Apertura por Reconstrucción")


fe = cv2.erode(f, kernel, iterations=1)
plt.figure()
ax1 = plt.subplot(221)
imshow(f, new_fig=False, title="Original")
plt.subplot(222, sharex=ax1, sharey=ax1)
imshow(fe, new_fig=False, title="Erosion")
plt.subplot(223, sharex=ax1, sharey=ax1)
imshow(fo, new_fig=False, title="Apertura")
plt.show(block=False)

# Ahora visualizamos las diferentes imágenes involucradas en el cálculo.
plt.figure()
ax1 = plt.subplot(221)
imshow(f, new_fig=False, title="Original")
plt.subplot(222, sharex=ax1, sharey=ax1)
imshow(fe, new_fig=False, title="Erosion")
plt.subplot(223, sharex=ax1, sharey=ax1)
imshow(fo, new_fig=False, title="Apertura")
plt.subplot(224, sharex=ax1, sharey=ax1)
imshow(fobr, new_fig=False, title="Apertura por Reconstruccion")
plt.show(block=False)

# ------------------------------------------
# --- Rellenado de huecos -----------------------------------------------------
# ------------------------------------------
img = cv2.imread("book_text_bw.tif", cv2.IMREAD_GRAYSCALE)
imshow(img)
np.unique(img)


# --- Version 1 ------------------------------------------------ Utilizando reconstrucción morfológica NO rellena los
# huecos que tocan los bordes
def imfillhole(img):
    # img: Imagen binaria de entrada. Valores permitidos: 0 (False), 255 (True).
    mask = np.zeros_like(img)  # Genero mascara para...
    mask = cv2.copyMakeBorder(
        mask[1:-1, 1:-1], 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=int(255)
    )  # ... seleccionar los bordes.
    marker = cv2.bitwise_not(
        img, mask=mask
    )  # El marcador lo defino como el complemento de los bordes.
    img_c = cv2.bitwise_not(
        img
    )  # La mascara la defino como el complemento de la imagen.
    img_r = imreconstruct(
        marker=marker, mask=img_c
    )  # Calculo la reconstrucción R_{f^c}(f_m)
    img_fh = cv2.bitwise_not(
        img_r
    )  # La imagen con sus huecos rellenos es igual al complemento de la reconstruccion.
    return img_fh


img_fh = imfillhole(img)
plt.figure()
ax1 = plt.subplot(121)
imshow(img, new_fig=False, title="Original", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(img_fh, new_fig=False, title="Rellenado de Huecos")
plt.show(block=False)

# --- Analisis de cada etapa ------------------------------------
img = cv2.imread("book_text_bw.tif", cv2.IMREAD_GRAYSCALE)
mask = np.zeros_like(img)  # Genero mascara para...
mask = cv2.copyMakeBorder(
    mask[1:-1, 1:-1], 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=int(255)
)  # ... seleccionar los bordes.
marker = cv2.bitwise_not(
    img, mask=mask
)  # El marcador lo defino como el complemento de los bordes.
img_c = cv2.bitwise_not(img)  # La mascara la defino como el complemento de la imagen.
img_r = imreconstruct(
    marker=marker, mask=img_c
)  # Calculo la reconstrucción R_{f^c}(f_m)
img_fh = cv2.bitwise_not(
    img_r
)  # La imagen con sus huecos rellenos es igual al complemento de la reconstruccion.

plt.figure()
ax1 = plt.subplot(221)
imshow(marker, new_fig=False, title="Marker", ticks=True)
plt.subplot(222, sharex=ax1, sharey=ax1)
imshow(img_c, new_fig=False, title="Mascara")
plt.subplot(223, sharex=ax1, sharey=ax1)
imshow(img_r, new_fig=False, title="Reconstruccion")
plt.subplot(224, sharex=ax1, sharey=ax1)
imshow(img_fh, new_fig=False, title="Reconstruccion + Complemento")
plt.show(block=False)

# Como se puede observar en la figura anterior, hay pequeños detalles que impiden que ciertos "huecos" se llenen.
# Planteamos algunas posibles soluciones.

# --- Mejoras sobre la imagen original ----------
img_modif = cv2.dilate(
    img, np.ones((3, 3), np.uint8)
)  # Con esto logro rellenar casi todos, algunas que quedan son: 1 "b", 1 "o" y 1 "e" abajo)
# img_modif = cv2.dilate(img, np.ones((5,5),np.uint8))  # Soluciono solo la "e" img_modif = cv2.morphologyEx(img,
# cv2.MORPH_CLOSE, np.ones((5,5),np.uint8)) # Notar la mejora en el grosor... img_modif = cv2.morphologyEx(img,
# cv2.MORPH_CLOSE, np.ones((6,6),np.uint8)) # Acá ya hay problemas: se unen caracteres.
# -----------------------------------------------
img_fh_modif = imfillhole(img_modif)

plt.figure()
ax1 = plt.subplot(221)
imshow(img, new_fig=False, title="Original", ticks=True)
plt.subplot(222, sharex=ax1, sharey=ax1)
imshow(img_fh, new_fig=False, title="Rellenado de Huecos (Original)")
plt.subplot(223, sharex=ax1, sharey=ax1)
imshow(img_fh_modif, new_fig=False, title="Rellenado de Huecos con Mejoras")
plt.show(block=False)


# --- Version 2 ------------------------------------------------ Utilizando cv2.floodFill() SI rellena los huecos que
# tocan los bordes
def imfillhole_v2(img):
    img_flood_fill = img.copy().astype("uint8")  # Genero la imagen de salida
    h, w = img.shape[:2]  # Genero una máscara necesaria para cv2.floodFill()
    mask = np.zeros(
        (h + 2, w + 2), np.uint8
    )  # https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#floodfill
    cv2.floodFill(img_flood_fill, mask, (0, 0), 255)  # Relleno o inundo la imagen.
    img_flood_fill_inv = cv2.bitwise_not(
        img_flood_fill
    )  # Tomo el complemento de la imagen inundada --> Obtenog SOLO los huecos rellenos.
    img_fh = (
        img | img_flood_fill_inv
    )  # La salida es un OR entre la imagen original y los huecos rellenos.
    return img_fh


img_fh_v2 = imfillhole_v2(img)
plt.figure()
ax1 = plt.subplot(121)
imshow(img, new_fig=False, title="Original", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(img_fh_v2, new_fig=False, title="Rellenado de Huecos (v2)")
plt.show(block=False)

# --- Comparacion ----------------------------------------------
(img_fh == img_fh_v2).all()  # No dan lo mismo....
imshow(img_fh == img_fh_v2)

plt.figure()
ax1 = plt.subplot(121)
imshow(img_fh, new_fig=False, title="Rellenado de Huecos (reconstruccion)", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(img_fh_v2, new_fig=False, title="Rellenado de Huecos (floodFill)")
plt.show(block=False)


# ------------------------------------------
# --- Elimino objetos que tocan el borde --------------------------------------
# ------------------------------------------
img = cv2.imread("book_text_bw.tif", cv2.IMREAD_GRAYSCALE)
imshow(img)


def imclearborder(img):
    # img: Imagen binaria de entrada. Valores permitidos: 0 (False), 255 (True).
    marker = img.copy()  # El marcador lo defino...
    marker[1:-1, 1:-1] = 0  # ... seleccionando solo los bordes.
    border_elements = imreconstruct(
        marker=marker, mask=img
    )  # Calculo la reconstrucción R_{f}(f_m) --> Obtengo solo los elementos que tocan el borde.
    img_cb = cv2.subtract(
        img, border_elements
    )  # Resto dichos elementos de la imagen original.
    return img_cb


img_cb = imclearborder(img)
plt.figure()
ax1 = plt.subplot(121)
imshow(img, new_fig=False, title="Original", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(img_cb, new_fig=False, title="Elimino objetos que tocan el borde")
plt.show(block=False)

# ------------------------------------------
# --- Ejemplo de aplicacion --------------------------------------------
# ------------------------------------------
img = cv2.imread("5R0Zs.jpg", cv2.IMREAD_GRAYSCALE)
img.shape
np.unique(img)
imshow(img, title="Imagen Original")

# Binarizo
_, img = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
np.unique(img)
imshow(img, title="Imagen Binarizada")

# Procesamos la imagen para mejorarla y luego visualizamos y comparamos.
img_cb = imclearborder(img)  # Elimino objetos que tocan el borde
img_cb_fh = imfillhole(img_cb)  # Relleno huecos
k = 15  # Probar con 8, 15, 25, ...
img_cb_fh_op = cv2.morphologyEx(
    img_cb_fh, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
)  # Suavizo bordes

# Visualizo y comparo
plt.figure()
ax1 = plt.subplot(221)
imshow(img, new_fig=False, title="Imagen Original", ticks=True)
plt.subplot(222, sharex=ax1, sharey=ax1)
imshow(img_cb, new_fig=False, title="Elimino objetos que tocan el borde")
plt.subplot(223, sharex=ax1, sharey=ax1)
imshow(img_cb_fh, new_fig=False, title="Relleno huecos")
plt.subplot(224, sharex=ax1, sharey=ax1)
imshow(img_cb_fh_op, new_fig=False, title="Apertura")
plt.show(block=False)
