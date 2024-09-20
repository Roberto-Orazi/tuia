import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- imadjust --------------------------------------------------------------
def imadjust(x, vin=None, vout=[0,255], gamma=1):
    # x      : Imagen de entrada en escalas de grises (2D), formato uint8.
    # vin    : Límites de los valores de intensidad de la imagen de entrada
    # vout   : Límites de los valores de intensidad de la imagen de salida
    # y      : Imagen de salida
    if vin==None:
        vin = [x.min(), x.max()]
    y = (((x - vin[0]) / (vin[1] - vin[0])) ** gamma) * (vout[1] - vout[0]) + vout[0]
    y[x<vin[0]] = vout[0]   # Valores menores que low_in se mapean a low_out
    y[x>vin[1]] = vout[1]   # Valores mayores que high_in se mapean a high_out
    if x.dtype==np.uint8:
        y = np.uint8(np.clip(np.round(y), 0, 255))   # Numpy underflows/overflows para valores fuera de rango, se debe utilizar clip.
    return y

# img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('xray-chest.png',cv2.IMREAD_GRAYSCALE)
img_adj1 = imadjust(img)
img_adj2 = imadjust(img, vin=[50,80])

img_adj1.min()
img_adj1.max()

img_adj2.min()
img_adj2.max()

ax1 = plt.subplot(221)
h = plt.imshow(img,cmap='gray',vmin=0,vmax=255)
plt.title("Imagen Original - plt.imshow(img,cmap='gray',vmin=0,vmax=255)")
plt.colorbar(h)

plt.subplot(222, sharex=ax1, sharey=ax1) 
h = plt.imshow(img,cmap='gray')
plt.title("Imagen Original - plt.imshow(img,cmap='gray')")
plt.colorbar(h)

plt.subplot(223, sharex=ax1, sharey=ax1)
h = plt.imshow(img_adj1,cmap='gray',vmin=0,vmax=255)
plt.title("imadjust(img)")
plt.colorbar(h)

plt.subplot(224, sharex=ax1, sharey=ax1)
h = plt.imshow(img_adj2,cmap='gray',vmin=0,vmax=255)
plt.title("imadjust(img,vin=[50,80])")
plt.colorbar(h)

plt.show()

# --- imadjust - ejemplo 2 --------------------------------------------------------------
img = cv2.imread('mammogram.tif',cv2.IMREAD_GRAYSCALE)
img_neg = cv2.bitwise_not(img)        # Imagen "negativa"
img_adj = imadjust(img,vin=[128,192])
img_adj2 = imadjust(img, gamma=2)

img.min()
img.max()

img_adj.min()
img_adj.max()

plt.figure()
ax1 = plt.subplot(221) 
plt.imshow(img, cmap="gray",vmin=0,vmax=255), plt.title("Imagen Original")
plt.subplot(222,sharex=ax1, sharey=ax1), plt.imshow(img_neg, cmap="gray",vmin=0,vmax=255), plt.title("Negativo")
plt.subplot(223,sharex=ax1, sharey=ax1), plt.imshow(img_adj, cmap="gray",vmin=0,vmax=255), plt.title("imadjust(img,vin=(128,192))")
plt.subplot(224,sharex=ax1, sharey=ax1), plt.imshow(img_adj2, cmap="gray",vmin=0,vmax=255), plt.title("imadjust(img, gamma=2)")
plt.show()

# --- Transformación logarítmica -----------------------------------------------------------------------
img = cv2.imread('Fourier_Spectrum.tif',cv2.IMREAD_GRAYSCALE)
img_log = 1*np.log(1+img.astype(float))
plt.subplot(121)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(122)
h=plt.imshow(img_log, cmap='gray')
plt.colorbar(h)
plt.title('Transformación logarítmica')
plt.show()

# --- Otra transformación -----------------------------------------------------------------------
img = cv2.imread('bone_scan.tif',cv2.IMREAD_GRAYSCALE)
img2 = 1 / (1 + (np.mean(img)/(img + np.finfo(float).eps ) )**0.9)  # Al sumar un float y al calcular la media, el tipo de dato se transforma en float

plt.subplot(121)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(122)
h=plt.imshow(img2, cmap='gray')
plt.colorbar(h)
plt.title('Otra transformación')
plt.show()


# --- Ecualización de histograma -----------------------------------------
img = cv2.imread('pollen_electron_microscope.tif',cv2.IMREAD_GRAYSCALE)
img.shape
img_fl = img.flatten()
img_fl.shape
hist, bins = np.histogram(img.flatten(), 256, [0, 256]) 
hist2 = cv2.calcHist([img], [0], None, [256], [0, 256]) # Más rápida que np.histogram()
max(abs(hist.flatten() - hist2.flatten()))
img_heq = cv2.equalizeHist(img)  

plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.subplot(122)
# plt.plot(hist)
# plt.plot(bins[:-1], hist)
plt.hist(img.flatten(), 256, [0, 256])
plt.title('Histograma')
plt.show()

ax1=plt.subplot(221)
#plt.imshow(img,cmap='gray')
plt.imshow(img,cmap='gray',vmin=0,vmax=255)
plt.title('Imagen Original')
plt.subplot(222)
plt.hist(img.flatten(), 256, [0, 256])
plt.title('Histograma')
plt.subplot(223,sharex=ax1,sharey=ax1)
#plt.imshow(img_heq,cmap='gray')
plt.imshow(img_heq,cmap='gray',vmin=0,vmax=255)
plt.title('Imagen Ecualizada')
plt.subplot(224)
plt.hist(img_heq.flatten(), 256, [0, 256])
plt.title('Histograma')
plt.show()

histn = hist.astype(np.double) / img.size
cdf = histn.cumsum()
plt.plot(cdf,color='r')
plt.title('cdf')
plt.show()


