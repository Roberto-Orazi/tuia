import cv2
import matplotlib.pyplot as plt
import numpy as np

# --- Rotaciones a +/-90º y 180º -----------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
img.shape
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False)

img_T = img.T
plt.figure(), plt.imshow(img_T, cmap='gray'), plt.show(block=False)

img_espejada =  img[::-1,]
plt.figure(), plt.imshow(img_espejada, cmap='gray'), plt.show(block=False)

img_espejada_T =  img[::-1,].T
plt.figure(), plt.imshow(img_espejada_T, cmap='gray'), plt.show(block=False)

# --- Recorte (crop) ----------------------------------------------------------------
img_crop = img[35:90,90:170]
plt.figure(), plt.imshow(img_crop, cmap='gray'), plt.show(block=False)

# img_crop = 0  # Así no...
img_crop *= 0
img_crop += 30
plt.figure(), plt.imshow(img_crop, cmap='gray'), plt.show(block=False)
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False)

# Otra forma...
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
img[35:90,90:170] = 255
img[35:90,90:170] = 0
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False)

# Crop and replace...
H = 55
W = 60
crop = img[120:120+H, 120:120+W,]
img_replaced = img.copy()
img_replaced[35:35+crop.shape[0], 90:90+crop.shape[1]] = crop
plt.figure(), plt.imshow(img_replaced, cmap='gray'), plt.show(block=False)

# --- Resize -------------------------------------------------------
img_resized = cv2.resize(img  , (128 , 128))
img_resized.shape
plt.figure(), plt.imshow(img_resized, cmap='gray'), plt.show(block=False)

img_resized = cv2.resize(img  , (50 , 128))
img_resized = cv2.resize(img  , (128 , 50))
img_resized.shape
plt.figure(), plt.imshow(img_resized, cmap='gray'), plt.show(block=False)


# --- Observo columnas/filas ---------------------------------------------------
img = cv2.imread('letras.png',cv2.IMREAD_GRAYSCALE)
img.shape

plt.imshow(img, cmap='gray')
plt.show(block=False)

linea_hor = img[50,:]
plt.figure()
plt.plot(linea_hor)
plt.show(block=False)