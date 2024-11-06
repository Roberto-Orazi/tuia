import cv2
import numpy as np
import matplotlib.pyplot as plt

# Definimos función para mostrar imágenes
def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=True, ticks=False):
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

# --- Analisis tipo de ruido ----------------------------------------------------------------------
img = cv2.imread('circuit_board_noise.tif', cv2.IMREAD_GRAYSCALE)
img.shape
imshow(img, title="Imagen Original", ticks=True)

r_ini, r_end = 500, 580
c_ini, c_end = 280, 400
roi = img[r_ini:r_end, c_ini:c_end]
imshow(roi, title="ROI", ticks=True)
# plt.figure(), plt.imshow(roi, cmap="gray", vmin=0, vmax=255), plt.show(block=False)

m = np.mean(roi)
std = np.std(roi)
hist, bins = np.histogram(roi.flatten(), 256, [0, 256]) 

plt.figure()
plt.subplot(121), plt.imshow(roi, cmap='gray'), plt.title('ROI')
plt.subplot(122), plt.plot(bins[:-1], hist), plt.title('Histograma')
plt.axvline(m, color='k', linestyle='dashed', linewidth=1)
plt.axvline(m-std, color='r', linestyle='dashed', linewidth=1)
plt.axvline(m+std, color='r', linestyle='dashed', linewidth=1)
plt.show(block=False)

# === Imagen Original =============================================
img_orig = cv2.imread('circuit_board.tif', cv2.IMREAD_GRAYSCALE)
imshow(img_orig, title="Imagen Original", ticks=True)
roi_orig = img_orig[r_ini:r_end, c_ini:c_end]
imshow(roi_orig, title="ROI", ticks=True)

m_orig = np.mean(roi_orig)
std_orig = np.std(roi_orig)
hist_orig, bins_orig = np.histogram(roi_orig.flatten(), 256, [0, 256]) 
plt.figure()
plt.subplot(221), plt.imshow(roi_orig, cmap='gray'), plt.title('ROI original')
plt.subplot(222), plt.imshow(roi, cmap='gray'), plt.title('ROI')
plt.subplot(223), plt.plot(bins_orig[:-1], hist_orig), plt.title('Histograma original')
plt.subplot(224), plt.plot(bins[:-1], hist), plt.title('Histograma')
plt.show(block=False)
# ==================================================================

# --- Otro ejemplo: Ruido uniforme -----------------------------------------------------------------------------
img = cv2.imread('circuit_board.tif', cv2.IMREAD_GRAYSCALE)
img.dtype
img.min()
img.max()

# --- Agrego ruido uniforme ----------------------
noise = np.random.rand(*img.shape)
noise_sc = noise*100
noise_sc.max()
noise_sc.min()
# imshow(noise_sc)

img_f = img.astype(np.float64)
imgn = img_f + noise_sc
imgn.max()
# imgn = np.uint8(255*(imgn/imgn.max()))  # Para analizar... que pasa si escalo y convierto a uint8? Comparar histogramas de ambas ROIs

plt.figure()
ax1=plt.subplot(121); plt.imshow(img, cmap='gray'), plt.title('Imagen Original')
plt.subplot(122,sharex=ax1, sharey=ax1), plt.imshow(imgn, cmap='gray'), plt.title('Imagen Ruidosa')
plt.show(block=False)

# --- Obtengo ROI y analizo ----------------------
r_ini, r_end = 500, 580
c_ini, c_end = 280, 400
roi = imgn[r_ini:r_end, c_ini:c_end]
imshow(roi, title="ROI", ticks=True)

m = np.mean(roi)
hist, bins = np.histogram(roi.flatten(), 256, [0, 256]) 

plt.figure()
plt.subplot(121), plt.imshow(roi, cmap='gray'), plt.title('ROI')
plt.subplot(122), plt.plot(bins[:-1], hist), plt.title('Histograma')
plt.show(block=False)

plt.figure()
plt.subplot(221), plt.imshow(roi_orig, cmap='gray'), plt.title('ROI Original')
plt.subplot(222), plt.imshow(roi, cmap='gray'), plt.title('ROI (ruido)')
plt.subplot(223), plt.plot(bins_orig[:-1], hist_orig), plt.title('Histograma Original')
plt.subplot(224), plt.plot(bins[:-1], hist), plt.title('Histograma (ruido)')
plt.show(block=False)


# -----------------------------------------------------------------------------------------
# --- Ejemplo filtrado espacial: Contrharmonic mean (salt, pepper) ------------------------
# -----------------------------------------------------------------------------------------
def imnoise_pepper(img, p=0.2):
    img_noise = img.copy()
    x = np.random.rand(*img.shape)
    img_noise[x<p] = 0
    return img_noise

def imnoise_salt(img, p=0.2):
    img_noise = img.copy()
    x = np.random.rand(*img.shape)
    img_noise[x<p] = 255
    return img_noise

def charmean(imgn, k=3, Q=1.5):
    imgn_f = imgn.astype(np.float64)
    if Q<0:
        imgn_f += np.finfo(float).eps
    w = np.ones((k,k))
    I_num = cv2.filter2D(imgn_f**(Q+1), cv2.CV_64F, w)
    I_den = cv2.filter2D(imgn_f**Q, cv2.CV_64F, w)
    I = I_num/(I_den + np.finfo(float).eps)
    return I

# --- Ruido pepper ----------------------------------------------
img = cv2.imread('circuit_board.tif', cv2.IMREAD_GRAYSCALE)
imgn = imnoise_pepper(img, 0.3)
# imgn = imnoise_pepper(img, 0.1)
# imgn = imnoise_pepper(img, 0.2)
imshow(imgn, title="Imagen con Ruido Pepper")

# Aplico el filtrado espacial filtrado espacial "Contrharmonic-Mean"
imgn_ch_filt = charmean(imgn, 3, 1.5)
imshow(imgn_ch_filt)

# También aplicamos filtro de mediana para comparar
imgn_median_filt3 = cv2.medianBlur(imgn, 3)
imgn_median_filt5 = cv2.medianBlur(imgn, 5)

# Comparamos
plt.figure()
ax1=plt.subplot(221); imshow(imgn, new_fig=False, colorbar=False, title="Imagen ruidosa")
plt.subplot(222, sharex=ax1, sharey=ax1), imshow(imgn_ch_filt, new_fig=False, colorbar=False, title="charmean")
plt.subplot(223, sharex=ax1, sharey=ax1), imshow(imgn_median_filt3, new_fig=False, colorbar=False, title="Median 3")
plt.subplot(224, sharex=ax1, sharey=ax1), imshow(imgn_median_filt5, new_fig=False, colorbar=False, title="Median 7")
plt.show(block=False)

# --- Ruido salt ----------------------------------------------
img = cv2.imread('circuit_board.tif', cv2.IMREAD_GRAYSCALE)
imgn = imnoise_salt(img, 0.3)
# imgn = imnoise_salt(img, 0.1)
# imgn = imnoise_salt(img, 0.2)
imshow(imgn, title="Imagen con Ruido Salt")

# Aplico el filtrado espacial filtrado espacial "Contrharmonic-Mean"
imgn_ch_filt = charmean(imgn, 3, -1.5)
imshow(imgn_ch_filt)

# También aplicamos filtro de mediana para comparar
imgn_median_filt3 = cv2.medianBlur(imgn, 3)
imgn_median_filt5 = cv2.medianBlur(imgn, 5)

# Comparamos
plt.figure()
ax1=plt.subplot(221); imshow(imgn, new_fig=False, colorbar=False, title="Imagen ruidosa")
plt.subplot(222, sharex=ax1, sharey=ax1), imshow(imgn_ch_filt, new_fig=False, colorbar=False, title="charmean")
plt.subplot(223, sharex=ax1, sharey=ax1), imshow(imgn_median_filt3, new_fig=False, colorbar=False, title="Median 3")
plt.subplot(224, sharex=ax1, sharey=ax1), imshow(imgn_median_filt5, new_fig=False, colorbar=False, title="Median 5")
plt.show(block=False)


