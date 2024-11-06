import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

# Defininimos función para mostrar imágenes
def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=False, ticks=False):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:        
        plt.show(block=blocking)

## -----------------------------------------------------------------------------------
## --- Medidas Invariantes de Momentos: Momentos de Hu--------------------------------
## -----------------------------------------------------------------------------------

# ---------------------------------------
# --- Ejemplo 1 ----------------------------------------------------------------
# ---------------------------------------

# --- Cargo imagen ---------------------------------------
image = cv2.imread("avion_01.png")          
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     
imshow(image)

# --- Medidas invariantes de Momentos --------------------
moments = cv2.moments(image)        # https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga556a180f43cab22649c23ada36a8a139
type(moments)
moments
for k, v in moments.items():
    # print(k, v)
    # print(f"{k:4}: {v}")
    # print(f"{k:4}: {v:5.2e}")
    print(f"{k:4}: {v:+5.2e}")

# --- Momentos de Hu ------------------------------------
hu_moments = cv2.HuMoments(moments)
type(hu_moments)
hu_moments.shape
hu_moments

hu_moments = hu_moments.flatten()
for ii,vv in enumerate(hu_moments):
    print(f"{ii:1d}: {vv:5.2e}")

# --- Ejemplo con varias imagenes -------------------------------------------
image = cv2.imread("aviones.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imshow(image, title="Imagen Original")

# --- Obtengo los contornos para separar los objetos ------------
contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
len(contours)

image_cnts = cv2.merge((image, image, image))
cv2.drawContours(image_cnts, contours, contourIdx=-1, color=(0, 0, 255), thickness=2)  # https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html#ga746c0625f1781f1ffc9056259103edbc
imshow(image_cnts)

# --- Visualizo individualmente -----------------------------
c = contours[0]
(x, y, w, h) = cv2.boundingRect(c)
roi = image[y:y + h, x:x + w]
imshow(roi)
hu_moments = cv2.HuMoments(cv2.moments(roi)).flatten()
hu_moments

# --- Obtengo valores para todos los objetos ---------------
result = np.zeros((7, len(contours)))
for ii,c in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)
    roi = image[y:y + h, x:x + w]
    hu_moments = cv2.HuMoments(cv2.moments(roi)).flatten()
    result[:,ii] = hu_moments

print(result)


# ---------------------------------------
# --- Ejemplo 2 ----------------------------------------------------------------
# ---------------------------------------

# --- Cargo imagen ---------------------------------------
img = cv2.imread("pintura.tif", cv2.IMREAD_GRAYSCALE)
img.shape
W,H = img.shape
imshow(img)

# --- Imagen 1 - Original ------------------------------------------------
M = 100
img1 = cv2.copyMakeBorder(img, M, M, M, M, cv2.BORDER_CONSTANT, None, 0)
img1.shape
imshow(img1, title="Imagen Original")

# --- Imagen 2 - Escalada 0.5 ---------------------------------------------
aux = cv2.resize(img, (W//2, H//2))
aux.shape
M = 200
img2 = cv2.copyMakeBorder(aux, M, M, M, M, cv2.BORDER_CONSTANT, None, 0)
img2.shape
imshow(img2, title="Imagen escalada 0.5")

# --- Imagen 3 - Escalada 1/8 ---------------------------------------------
aux = cv2.resize(img, (W//8, H//8))
aux.shape
M = 275
img3 = cv2.copyMakeBorder(aux, M, M, M, M, cv2.BORDER_CONSTANT, None, 0)
img3.shape
imshow(img3, title="Imagen escalada 1/8")

# --- Imagen 4 - Rotada 15 ------------------------------------------------
aux = imutils.rotate_bound(img, 15)
aux.shape
img4 = cv2.copyMakeBorder(aux, 55, 56, 55, 56, cv2.BORDER_CONSTANT, None, 0)
img4.shape
imshow(img4, title="Imagen rotada 15º")

# --- Imagen 5 - Rotada -45 -------------------------------------------
aux = imutils.rotate_bound(img, -45)
aux.shape
img5 = cv2.copyMakeBorder(aux, 17, 18, 17, 18, cv2.BORDER_CONSTANT, None, 0)
img5.shape
imshow(img5, title="Imagen rotada -45º")

# --- Imagen 6 - Rotada 195 ---------------------------------------------
aux = imutils.rotate_bound(img, 195)
aux.shape
img6 = cv2.copyMakeBorder(aux, 55, 56, 55, 56, cv2.BORDER_CONSTANT, None, 0)
img6.shape
imshow(img6, title="Imagen rotada 195º")

# --- Imagen 7 - Escaclada 0.5 y rotada 115 ---------------------------------------------
aux = cv2.resize(img, (W//2, H//2))
aux = imutils.rotate_bound(aux, 115)
aux.shape
img7 = cv2.copyMakeBorder(aux, 167, 168, 167, 168, cv2.BORDER_CONSTANT, None, 0)
img7.shape
imshow(img7, title="Imagen escalada 0.5 + rotada 115º")

# --- Imagen 8 - Escaclada 1/8, rotada -35 y trasladada  ---------------------------------------------
aux = cv2.resize(img, (W//8, H//8))
aux = imutils.rotate_bound(aux, -35)
aux.shape
img8 = cv2.copyMakeBorder(aux, 100, 431, 100, 431, cv2.BORDER_CONSTANT, None, 0)
img8.shape
imshow(img8, title="Imagen escalada 1/8, rotada 15º y trasladada")

# --- Calculo los momentos de Hu ---------------------------------------------------------------------
hu1 = cv2.HuMoments(cv2.moments(img1))
hu2 = cv2.HuMoments(cv2.moments(img2))
hu3 = cv2.HuMoments(cv2.moments(img3))
hu4 = cv2.HuMoments(cv2.moments(img4))
hu5 = cv2.HuMoments(cv2.moments(img5))
hu6 = cv2.HuMoments(cv2.moments(img6))
hu7 = cv2.HuMoments(cv2.moments(img7))
hu8 = cv2.HuMoments(cv2.moments(img8))

x = np.concatenate((hu1, hu2, hu3, hu4, hu5, hu6, hu7, hu8), axis=1)
x.shape
x
print(x)
with np.printoptions(suppress=False, linewidth=100, precision=2):
    print(x)

