import cv2
import numpy as np
import matplotlib.pyplot as plt
from roipoly import RoiPoly     # https://pypi.org/project/roipoly/

# --- Cargo imagen y selecciono ROI --------------------------------------
img = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap="gray")
my_roi = RoiPoly(color='r') 

# --- Muestra la ROI sobre la imagen -------------------------------------
plt.imshow(img, cmap="gray")
my_roi.display_roi()
plt.show()

# --- Muestra la ROI + info ----------------------------------------------
plt.imshow(img, cmap="gray")
my_roi.display_roi()
my_roi.display_mean(img)
plt.show()

# --- Obtengo máscara ----------------------------------------------------
mask = my_roi.get_mask(img)
mask
type(mask)
mask.dtype
plt.imshow(mask, cmap="gray")
plt.show()

# --- ROI info -----------------------------------------------------------
my_roi.x
my_roi.y
mean = np.mean(img[mask])
std = np.std(img[mask])