import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Imagen Original ---------------------------------------
img = cv2.imread("MonaLisa.jpg")
print(img.dtype)

plt.figure()
plt.imshow(img)
plt.show(block=False)  # Acá puede observarse que la imagen está en BGR....

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Re-acomodo los planos: BGR --> RGBS
plt.figure(), plt.imshow(img), plt.show(block=False)

# --- Determino ROI ----------------------------------------
img2 = img.copy()  # Creo una copia de la imagen
xi, H = 100, 100  # Defino las coordenadas...
yi, W = 480, 75  # ... de la ROI
cv2.rectangle(
    img2, (yi, xi), (yi + W, xi + H), (255, 0, 0), 2
)  # Agrego un rectángulo  (https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html?highlight=rectangle)
plt.figure(), plt.imshow(img2), plt.show(block=False)

# ---- Agrego borrosidad -----------------------------------
img3 = img.copy()  # Creo una copia de la imagen
sub_face = img[xi : xi + H, yi : yi + W]  # Obtengo la ROI
# -- Agrego Borrosidad ----
K = 23
sub_face = cv2.filter2D(
    sub_face, -1, np.ones((K, K)) / (K**2)
)  # Filtrado espacial --> Filtro promedio
# sub_face = cv2.blur(sub_face, (K,K))                          # Idem anterior... sub_face = cv2.GaussianBlur(sub_face,
# (K,K), 10)              # Kernel Gaussiano (mas ejemplos/info en
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html) -- Reemplazo  -----------
img3[xi : xi + H, yi : yi + W] = sub_face  # Reemplazo en la imagen
plt.figure(), plt.imshow(img3), plt.show(block=False)


# --------------------------------------------------------------
# --- Version con máscaras -------------------------------------
# --------------------------------------------------------------
mask = np.full(img.shape, False)
# mask = np.zeros(img.shape, dtype=bool)    # Otra forma....
mask[xi : xi + H, yi : yi + W] = True
maskneg = ~mask

# *** Otra forma de generar la máscara: 0s y 1s ****** mask = np.zeros(img.shape, np.uint8) mask[xi:xi+H, yi:yi+W] = 1
# maskneg = mask.copy() maskneg[maskneg==1] = 255 maskneg[maskneg==0] = 1 maskneg[maskneg==255] = 0
# ****************************************************

plt.figure()
plt.subplot(121), plt.imshow(mask[:, :, 0], cmap="gray"),
plt.subplot(122), plt.imshow(maskneg[:, :, 0], cmap="gray")
plt.show(block=False)

img_blurred = cv2.GaussianBlur(img, (K, K), 20)
img_face = img_blurred * mask
img_back = img * maskneg

plt.figure()
plt.subplot(121), plt.imshow(img_face)
plt.subplot(122), plt.imshow(img_back)
plt.show(block=False)

img_out = img_face + img_back
plt.figure(), plt.imshow(img_out), plt.show(block=False)
