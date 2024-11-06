import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Espacio de color HSV ----------------------------------------------
img = cv2.imread('flowers.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # Rangos --> H: 0-179  / S: 0-255  / V: 0-255
h, s, v = cv2.split(img_hsv)
plt.figure()
ax1=plt.subplot(221); plt.imshow(img)
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(h, cmap='gray'), plt.title('Canal H')
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(s, cmap='gray'), plt.title('Canal S')
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(v, cmap='gray'), plt.title('Canal V')
plt.show(block=False)

# --- Espacio de color HSI ----------------------------------------------
img = cv2.imread('flowers.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS) 
h, l, s = cv2.split(img_hls)
plt.figure()
ax1=plt.subplot(221); plt.imshow(img)
plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(h, cmap='gray'), plt.title('Canal H')
plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(l, cmap='gray'), plt.title('Canal L')
plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(s, cmap='gray'), plt.title('Canal S')
plt.show(block=False)

h_smooth = cv2.blur(h, (9, 9))
l_smooth = cv2.blur(l, (9, 9))
s_smooth = cv2.blur(s, (9, 9))
img_smooth_all = cv2.cvtColor(cv2.merge((h_smooth, l_smooth, s_smooth)), cv2.COLOR_HLS2RGB)
img_smooth_l = cv2.cvtColor(cv2.merge((h, l_smooth, s)), cv2.COLOR_HLS2RGB)

plt.figure()
ax1=plt.subplot(221) 
plt.imshow(img), plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(img_smooth_l, cmap='gray'), plt.title('Blur en canal L')
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(img_smooth_all, cmap='gray'), plt.title('Blur en los 3 canales')
plt.show(block=False)


# --- Espacio de color HSV - Ejemplo ----------------------------------------------
img = cv2.imread('peppers.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # Rangos --> H: 0-179  / S: 0-255  / V: 0-255
h, s, v = cv2.split(img_hsv)
plt.figure()
ax1=plt.subplot(221); plt.imshow(img)
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(h, cmap='gray'), plt.title('Canal H')
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(s, cmap='gray'), plt.title('Canal S')
plt.subplot(224,sharex=ax1,sharey=ax1), plt.imshow(v, cmap='gray'), plt.title('Canal V')
plt.show(block=False)

# Segmentacion en color - Detectar solo el rojo
ix_h1 = np.logical_and(h > 180 * .9, h < 180)
ix_h2 = h < 180 * 0.04
ix_s = np.logical_and(s > 256 * 0.3, s < 256)
ix = np.logical_and(np.logical_or(ix_h1, ix_h2), ix_s)
# ix2 = (ix_h1 | ix_h2) & ix_s   # Otra opcion que da igual...

r, g, b = cv2.split(img)
r[ix != True] = 0
g[ix != True] = 0
b[ix != True] = 0
rojo_img = cv2.merge((r, g, b))
plt.figure(), plt.imshow(rojo_img), plt.show(block=False)


# --- Filtrado espacial ----------------------------------------------------------------
img = cv2.imread('peppers.png')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Usando kernel y filter 2D
kernel = np.ones((5, 5), np.float32)/25
img_filt = cv2.filter2D(img_RGB, -1, kernel)
plt.figure(), plt.imshow(img_filt), plt.show(block=False)

# Funciones filtrado
gblur = cv2.GaussianBlur(img_RGB, (55, 55), 0)
median = cv2.medianBlur(img_RGB, 21)
blur = cv2.blur(img_RGB, (55, 55))
plt.figure()
plt.subplot(221), plt.imshow(img_RGB), plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title('Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(gblur), plt.title('Gaussian blur'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(median), plt.title('Median blur'), plt.xticks([]), plt.yticks([])
plt.show(block=False)

# Filtrado Espacial - High Boost
img = cv2.imread('flowers.tif')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
w1 = np.ones((3, 3), np.float32)/9
w2 = np.ones((3, 3), np.float32)  # Laplaciano  
w2[1,1] = -8                      #
# -----------------
def im2double(im):
    info = np.iinfo(im.dtype) 
    return im.astype(np.float64) / info.max 

img_RGB = im2double(img_RGB)
# ------------------
img_pb = cv2.filter2D(img_RGB, -1, w1)
img_en = img_pb - cv2.filter2D(img_pb, -1, w2)
plt.figure()
ax1 = plt.subplot(221); plt.imshow(img_RGB), plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(img_pb), plt.title('Filtro Pasa-Bajos en todos los canales'), plt.xticks([]), plt.yticks([])
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(img_en), plt.title('Mejorada utilizando Laplaciano'), plt.xticks([]), plt.yticks([])
plt.show(block=False)


img_en2 = cv2.convertScaleAbs(img_en*255)
img_en2.dtype
plt.figure()
ax1 = plt.subplot(221); plt.imshow(img_RGB), plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(img_pb), plt.title('Filtro Pasa-Bajos en todos los canales'), plt.xticks([]), plt.yticks([])
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(img_en), plt.title('Mejorada utilizando Laplaciano'), plt.xticks([]), plt.yticks([])
plt.subplot(224,sharex=ax1,sharey=ax1), plt.imshow(img_en2), plt.title('Mejorada utilizando Laplaciano + cast'), plt.xticks([]), plt.yticks([])
plt.show(block=False)

img_en3 = cv2.normalize(img_en,None,0,255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
img_en3.min()
img_en3.max()
img_en3.dtype
plt.figure()
ax1 = plt.subplot(221); plt.imshow(img_RGB), plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(img_en3), plt.title('Mejorada utilizando Laplaciano - norminmax'), plt.xticks([]), plt.yticks([])
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(img_en), plt.title('Mejorada utilizando Laplaciano'), plt.xticks([]), plt.yticks([])
plt.subplot(224,sharex=ax1,sharey=ax1), plt.imshow(img_en2), plt.title('Mejorada utilizando Laplaciano + cast'), plt.xticks([]), plt.yticks([])
plt.show(block=False)
