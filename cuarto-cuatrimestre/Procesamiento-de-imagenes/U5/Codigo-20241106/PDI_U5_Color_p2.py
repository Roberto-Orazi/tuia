import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Pillow --> https://pillow.readthedocs.io/en/stable/


# Definimos función para mostrar imágenes
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


# --------------------------------------------------------------------------------------
# --- Dithering ------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# --- Imagen en escala de grises - Ejemplo 1 -------------------------------------------
img_cv2 = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)
img_cv2.shape
img_cv2.dtype
imshow(img_cv2, title="Imagen Original")

# Para aplicar Dithering, vamos a utilizar el paquete Pillow
img_PIL = Image.open("cameraman.tif")
img_PIL.mode  # L: Luminance
img_PIL.size  # (256,256)
imshow(img_PIL, title="Imagen Original (Pillow)")

# Aplicamos Dithering sobre la imagen, especificamos que queremos una paleta "binaria", es decir, solo 0s y 1s.
image_dithering = img_PIL.convert(
    mode="1", dither=Image.FLOYDSTEINBERG
)  # https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=convert#PIL.Image.Image.convert
plt.figure()
ax1 = plt.subplot(121)
imshow(img_PIL, title="Imagen original", new_fig=False)
plt.subplot(122, sharex=ax1, sharey=ax1), imshow(
    image_dithering, title="Imagen con dithering", new_fig=False
)
plt.show(block=False)

# -- Análisis Imagen Original ------------------- Cargada con OpenCV
img_cv2.shape
np.unique(img_cv2)
len(np.unique(img_cv2))  # 247 = 253-7+1

# Cargada con Pillow
img_PIL.size
col_and_counts = img_PIL.getcolors()  # [ ( count, index ), ( count, index ), ... ]
len(col_and_counts)
col_and_counts

x = img_PIL.getdata()
list_of_pixels = list(x)
len(list_of_pixels)  # 256*256 = 65.536
list_of_pixels[:5]
list_of_pixels

np.unique(list_of_pixels)
Ncolors = len(np.unique(list_of_pixels))  # 247 = 253-7+1

# -- Análisis Imagen con Dithering ------------------
col_and_counts = (
    image_dithering.getcolors()
)  # [ ( count, index ), ( count, index ), ... ]
len(col_and_counts)
col_and_counts

x = image_dithering.getdata()
list_of_pixels = list(x)
len(list_of_pixels)  # 256*256 = 65.536
list_of_pixels[:5]
np.unique(list_of_pixels)
Ncolors_out = len(np.unique(list_of_pixels))  # 2

# Obtengo matriz de datos
image_dithering_data = np.array(image_dithering.getdata(), dtype=np.uint8).reshape(
    img_PIL.size
)
type(image_dithering_data)
image_dithering_data.dtype
imshow(image_dithering_data, title="Imagen con Dithering - Matriz de datos")

# --- Dithering en colores -------------------------------------------------------------

# --- Imagen Color - Ejemplo 1 ---------------------------------------------------------
img_PIL = Image.open("landscape.jpg")
img_PIL.size
img_PIL.mode
imshow(img_PIL, title="Imagen Original")

# Ahora, reducimos la paleta con y sin Dithering.
img_proc = img_PIL.convert(
    mode="P", dither=Image.NONE, palette=Image.WEB
)  # standard 216-color "web palette"
img_proc_dither = img_PIL.convert(
    mode="P", dither=Image.FLOYDSTEINBERG, palette=Image.WEB
)  # standard 216-color "web palette"
plt.figure()
ax1 = plt.subplot(221)
imshow(img_PIL, title="Imagen Original", new_fig=False)
plt.subplot(222, sharex=ax1, sharey=ax1), imshow(
    img_proc, title="Imagen procesada", new_fig=False
)
plt.subplot(223, sharex=ax1, sharey=ax1), imshow(
    img_proc_dither, title="Imagen procesada + dither", new_fig=False
)
plt.show(block=False)

# -- Análisis Imagen Original -----------------------------------------------
img_PIL.size  # 720 x 480 = 345.600
col_and_counts = img_PIL.getcolors(
    img_PIL.size[0] * img_PIL.size[1]
)  # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getcolors
len(col_and_counts)
col_and_counts[:3]

x = img_PIL.getdata()
list_of_pixels = list(x)
len(list_of_pixels)  # 720 x 480 = 345.600
list_of_pixels[:5]

# -- Análisis de la imagen procesada sin dithering --------------------------
col_and_counts = img_proc.getcolors(img_proc.size[0] * img_proc.size[1])
len(col_and_counts)

x = img_proc.getdata()
list_of_pixels = list(x)
len(list_of_pixels)  # 720 x 480 = 345.600
list_of_pixels[:5]

np.unique(list_of_pixels)
Ncolors_out = len(np.unique(list_of_pixels))

img_proc_idxs = np.array(list_of_pixels, dtype=np.uint8).reshape(
    img_proc.size[::-1]
)  # Tener cuidado con el reshape...
img_proc_idxs.shape
plt.figure()
ax1 = plt.subplot(121)
imshow(img_proc, title="Imagen procesada - RGB", new_fig=False)
plt.subplot(122, sharex=ax1, sharey=ax1), imshow(
    img_proc_idxs, title="Imagen procesada - indices", new_fig=False
)
plt.show(block=False)

# Obtengamos ahora la paleta de nuestra imagen procesada
paleta = (
    img_proc.getpalette()
)  # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getpalette
type(paleta)
len(paleta)
paleta = np.reshape(paleta, (-1, 3))
paleta.max()
paleta.min()
paleta.dtype
paleta = paleta.astype(np.uint8)

# Acá se puede ver que hay 216 colores --> standard 216-color "web palette"
paleta_limpia = np.array(
    [c for c in paleta if c.any()]
)  # Elimino todas las filas que son [0 0 0]
paleta_limpia = np.vstack(
    ([0, 0, 0], paleta_limpia)
)  # Agrego 1 sola correspondiente al [0 0 0]
print(paleta_limpia.shape)  # 216 x 3
print(paleta_limpia)

# Obtengamos ahora la matriz de datos correspondiente a la imagen RGB
img_proc_RGB = np.array(img_proc.convert("RGB"))  # Paso a RGB
imshow(img_proc_RGB, title="Imagen con paleta reducida y sin dithering")
colours = np.unique(img_proc_RGB.reshape(-1, 3), axis=0)
colours.shape

# -- Análisis de la imagen procesada CON dithering --------------------------
dither_col_and_counts = img_proc_dither.getcolors(
    img_proc_dither.size[0] * img_proc_dither.size[1]
)
len(dither_col_and_counts)

x = img_proc_dither.getdata()
list_of_pixels = list(x)
len(list_of_pixels)  # 720 x 480 = 345.600
list_of_pixels[:5]

np.unique(list_of_pixels)
dither_Ncolors_out = len(np.unique(list_of_pixels))
dither_Ncolors_out

dither_img_proc_idxs = np.array(list_of_pixels, dtype=np.uint8).reshape(
    img_proc_dither.size[::-1]
)  # Tener cuidado con el reshape...
dither_img_proc_idxs.shape
plt.figure()
ax1 = plt.subplot(121)
imshow(img_proc_dither, title="Imagen procesada con dithering - RGB", new_fig=False)
plt.subplot(122, sharex=ax1, sharey=ax1), imshow(
    dither_img_proc_idxs,
    title="Imagen procesada con dithering - indices",
    new_fig=False,
)
plt.show(block=False)

# Obtengamos ahora la paleta de nuestra imagen procesada con dithering
dither_paleta = np.reshape(img_proc_dither.getpalette(), (-1, 3)).astype(np.uint8)
dither_paleta.shape
np.all(dither_paleta == paleta)  # Las dos paletas son iguales...

# Obtengamos ahora la matriz de datos correspondiente a la imagen RGB.
img_proc_dither_RGB = np.array(img_proc_dither.convert("RGB"))  # Paso a RGB
imshow(img_proc_dither_RGB, title="Imagen con paleta reducida con dithering")
dither_colours = np.unique(img_proc_dither_RGB.reshape(-1, 3), axis=0)
dither_colours.shape


# --- Imagen Color - Ejemplo 2 ---------------------------------------------------------
img_PIL = Image.open("peppers.png")
print(img_PIL.size)
print(img_PIL.mode)
imshow(img_PIL, title="Imagen Original")

# image_dithering = img_PIL.convert(mode='P', palette=Image.ADAPTIVE, dither=Image.FLOYDSTEINBERG)  #
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering image_dithering = img_PIL.convert(mode='P',
# palette=Image.ADAPTIVE, dither=Image.FLOYDSTEINBERG, colors=3)
image_dithering = img_PIL.convert(
    mode="P", palette=Image.ADAPTIVE, dither=Image.FLOYDSTEINBERG, colors=8
)
plt.figure()
ax1 = plt.subplot(121)
imshow(img_PIL, title="Imagen Original", new_fig=False)
plt.subplot(122, sharex=ax1, sharey=ax1), imshow(
    image_dithering, title="Imagen con dithering", new_fig=False
)
plt.show(block=False)

# -- Análisis Imagen Original ------------------------
col_and_counts = img_PIL.getcolors(img_PIL.size[0] * img_PIL.size[1])
Ncolors = len(col_and_counts)
print(Ncolors)

# -- Análisis Imagen con dithering -------------------
col_and_counts = image_dithering.getcolors(
    image_dithering.size[0] * image_dithering.size[1]
)
Ncolors_out = len(col_and_counts)
print(Ncolors_out)

# Obtengo la paleta de la imagen con dithering
palette = np.array(image_dithering.getpalette(), dtype=np.uint8).reshape((-1, 3))
print(palette.shape)
print(palette)

# Obtenemos la matriz de datos correspondiente a la imagen RGB.
image_dithering_RGB = np.array(image_dithering.convert("RGB"))  # Paso a RGB
# Si bien ya teniamos la paleta de la imagen con dithering, volvamos a obtener los colores y su frecuencia de aparición
# en un formato mas conveniente para analizarlos.
colours, counts = np.unique(
    image_dithering_RGB.reshape(-1, 3), axis=0, return_counts=1
)  # Obtengo colores y cuentas

# De manera ilustrativa, hacemos un gráfico de torta con los colores de la paleta y su frecuencia de aparición. ---
# Preparo datos -----------------------------------------------------------
idx = np.argsort(-counts)  # Ordeno en base a frecuencia de ocurrencias
counts = counts[idx]  #
colours = colours[idx]  #
counts_pct = counts / np.sum(counts) * 100  # Paso a porcentaje

# --- Genero texto a mostrar y normalizo los colores ---------------------------
labels = [
    f"{counts_pct[ii]:6.2f}%  ({colours[ii,0]:3d},{colours[ii,1]:3d},{colours[ii,2]:3d})"
    for ii in range(len(counts))
]
col = [(c[0] / 255.0, c[1] / 255.0, c[2] / 255.0) for c in colours]

# --- Genero gráfico de torta --------------------------------------------------
plt.figure(figsize=(9, 5))
ax = plt.subplot(111)
ax.pie(counts_pct, labels=labels, colors=col)
pos1 = ax.get_position()
pos2 = [0.15, pos1.y0, pos1.width, pos1.height]
ax.set_position(pos2)
plt.legend(
    title="Colores RGB", bbox_to_anchor=(1.4, 1), loc="upper left", fontsize=10
)  # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.title("Proporción de Colores")
plt.show(block=False)


# Obtengo índices
image_dithering_idxs = np.array(
    list(image_dithering.getdata()), dtype=np.uint8
).reshape(
    image_dithering.size[::-1]
)  # Tener cuidado con el reshape...
image_dithering_idxs.shape
np.unique(image_dithering_idxs)
plt.figure()
ax1 = plt.subplot(121)
plt.xticks([]), plt.yticks([]), plt.imshow(image_dithering), plt.title(
    "Imagen procesada - RGB"
)
plt.subplot(122, sharex=ax1, sharey=ax1), plt.imshow(
    image_dithering_idxs, cmap="gray"
), plt.title("Imagen procesada - indices")
plt.show(block=False)
