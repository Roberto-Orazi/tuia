import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('xray-chest.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)

# --- Matplotlib -------------------------------------------------
plt.figure(1)
h = plt.imshow(img1, cmap='gray')
plt.colorbar(h)

plt.figure(2)
h = plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.colorbar(h)

plt.show()
# plt.show(block=False)

# --- Open CV -----------------------------------------------------
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
