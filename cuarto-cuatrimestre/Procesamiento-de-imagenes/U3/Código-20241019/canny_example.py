import numpy as np
import cv2
import matplotlib.pyplot as plt

import canny

# --- Imagen ------------------------------------------------------------------
img = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)
plt.figure(), plt.imshow(img, cmap="gray"), plt.show(block=False)

img_blur = cv2.GaussianBlur(img, (3,3), 2)
plt.figure()
ax1 = plt.subplot(121); plt.imshow(img, cmap="gray"), plt.title("Imagen")
plt.subplot(122, sharex=ax1, sharey=ax1), plt.imshow(img_blur, cmap="gray"), plt.title("Imagen + blur")
plt.show(block=False)

# --- Original ----------------------------------------------------------------
# img_canny_CV2 = cv2.Canny(img_blur, 50, 115, apertureSize=3, L2gradient=True)  
img_canny_CV2 = cv2.Canny(img_blur, 150, 255, apertureSize=3, L2gradient=True) 

# --- Implementacion ----------------------------------------------------------
img_canny = canny.canny(img_blur, th1=50, th2=115)

# --- Comparacion -------------------------------------------------------------
plt.figure()
ax1 = plt.subplot(121); plt.imshow(img_canny_CV2, cmap="gray"), plt.title("Canny - openCV")
plt.subplot(122, sharex=ax1, sharey=ax1), plt.imshow(img_canny, cmap="gray"), plt.title("Canny - Manual")
plt.show(block=False)

dif = img_canny.astype(np.int16) - img_canny_CV2.astype(np.int16)
plt.figure()
ax1 = plt.subplot(221); plt.imshow(img, cmap="gray"), plt.title("Imagen")
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(dif, cmap="gray"), plt.title("Diferencia"), plt.colorbar()
plt.subplot(223, sharex=ax1, sharey=ax1); plt.imshow(img_canny_CV2, cmap="gray"), plt.title("Canny - openCV")
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(img_canny, cmap="gray"), plt.title("Canny - Manual")
plt.show(block=False)
