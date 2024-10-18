import matplotlib

matplotlib.use("TkAgg")
import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Ecualización de histograma -----------------------------------------
img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)
img.shape
img_fl = img.flatten()
img_fl.shape
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
hist2 = cv2.calcHist([img], [0], None, [256], [0, 256])  # Más rápida que np.histogram()
max(abs(hist.flatten() - hist2.flatten()))
img_heq = cv2.equalizeHist(img)

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Imagen Original")
plt.subplot(122)
# plt.plot(hist) plt.plot(bins[:-1], hist)
plt.hist(img.flatten(), 256, [0, 256])
plt.title("Histograma")
plt.show()

ax1 = plt.subplot(221)
# plt.imshow(img,cmap='gray')
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Imagen Original")
plt.subplot(222)
plt.hist(img.flatten(), 256, [0, 256])
plt.title("Histograma")
plt.subplot(223, sharex=ax1, sharey=ax1)
# plt.imshow(img_heq,cmap='gray')
plt.imshow(img_heq, cmap="gray", vmin=0, vmax=255)
plt.title("Imagen Ecualizada")
plt.subplot(224)
plt.hist(img_heq.flatten(), 256, [0, 256])
plt.title("Histograma")
plt.show()

histn = hist.astype(np.double) / img.size
cdf = histn.cumsum()
plt.plot(cdf, color="r")
plt.title("cdf")
plt.show()
