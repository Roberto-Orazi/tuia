import cv2
import numpy as np
import matplotlib.pyplot as plt


# --- Filtro Promediación (Pasa bajos) - Efectos de borde -----------------------------------
# https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04
img = cv2.imread('squares_bw.tif',cv2.IMREAD_GRAYSCALE)
w = np.ones((31, 31), np.float32) / (31*31)

# /*
#  Various border types, image boundaries are denoted with '|'

#  * BORDER_REPLICATE:     aaaaaa|abcdefgh|hhhhhhh
#  * BORDER_REFLECT:       fedcba|abcdefgh|hgfedcb
#  * BORDER_REFLECT_101:   gfedcb|abcdefgh|gfedcba
#  * BORDER_WRAP:          cdefgh|abcdefgh|abcdefg
#  * BORDER_CONSTANT:      iiiiii|abcdefgh|iiiiiii  with some specified 'i'
#  */

plt.subplot(231)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

plt.subplot(232)
img_fil = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_DEFAULT)  # cv2.BORDER_DEFAULT = 4  --> Idem a cv2.BORDER_REFLECT_101
plt.imshow(img_fil,cmap='gray')
plt.title('Filtrada - BORDER_DEFAULT')
plt.xticks([]), plt.yticks([])

plt.subplot(233)
img_fil = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_REPLICATE)
plt.imshow(img_fil,cmap='gray')
plt.title('Filtrada - BORDER_REPLICATE')
plt.xticks([]), plt.yticks([])

plt.subplot(234)
img_fil = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_WRAP)
plt.imshow(img_fil,cmap='gray')
plt.title('Filtrada - BORDER_WRAP')
plt.xticks([]), plt.yticks([])

plt.subplot(235)
img_fil = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_REFLECT)
plt.imshow(img_fil,cmap='gray')
plt.title('Filtrada - BORDER_REFLECT')
plt.xticks([]), plt.yticks([])

plt.subplot(236)
img_fil = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_CONSTANT)  # 0  --> Idem a cv2.BORDER_REFLECT_101
plt.imshow(img_fil,cmap='gray')
plt.title('Filtrada - BORDER_CONSTANT (idem zero padding)')
plt.xticks([]), plt.yticks([])

plt.show(block=False)


# --- Filtro promediacion - Ejemplo ------------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
w1 = np.ones((3,3))/(3*3)  # Casting a float automático...
w2 = np.ones((15,15))/(15*15)  
w3 = np.ones((31,31))/(31*31)  
img1 = cv2.filter2D(img,-1,w1)
img2 = cv2.filter2D(img,-1,w2)
img3 = cv2.filter2D(img,-1,w3)

ax1 = plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
plt.imshow(img1,cmap='gray')
plt.title('Filtro promediación 3 x 3')
plt.subplot(223,sharex=ax1,sharey=ax1)
plt.imshow(img2,cmap='gray')
plt.title('Filtro promediación 15 x 15')
plt.subplot(224,sharex=ax1,sharey=ax1)
plt.imshow(img3,cmap='gray')
plt.title('Filtro promediación 31 x 31')
plt.show(block=False)


# --- Filtro pasa  altos - Ejemplo ------------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
w1 = -np.ones((3,3))/(3*3)
w1[1,1]=8/9
w2 = -np.ones((5,5))/(5*5)  
w2[2,2]=24/25
img1 = cv2.filter2D(img,-1,w1)
img2 = cv2.filter2D(img,-1,w2)

ax1 = plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
plt.imshow(img1,cmap='gray')
plt.title('Filtro pasa altos 3 x 3')
plt.subplot(223,sharex=ax1,sharey=ax1)
plt.imshow(img2,cmap='gray')
plt.title('Filtro pasa altos 5 x 5')
plt.show(block=False)



# --- Filtro High Boost - Ejemplo ------------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
A = 1.8
w1 = -np.ones((3,3))/(3*3)
w1[1,1] = (9*A-1)/9
w2 = -np.ones((5,5))/(5*5)  
w2[2,2] = (25*A-1)/25
img1 = cv2.filter2D(img,-1,w1)
img2 = cv2.filter2D(img,-1,w2)

ax1 = plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
plt.imshow(img1,cmap='gray')
plt.title('Filtro High Boost 3 x 3')
plt.subplot(223,sharex=ax1,sharey=ax1)
plt.imshow(img2,cmap='gray')
plt.title('Filtro High Boost 5 x 5')
plt.show(block=False)


# --- Filtro Sobel -------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
wy = np.array([(1,2,1),(0,0,0),(-1,-2,-1)])
wx = wy.transpose() # Idem a wx.T
img1 = cv2.filter2D(img,-1,wx)
img2 = cv2.filter2D(img,-1,wy)

plt.figure(1)
ax1 = plt.subplot(221)
plt.imshow(img,cmap='gray')
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
plt.imshow(img1,cmap='gray')
plt.title('Filtro Sobel horizontal')
plt.subplot(223,sharex=ax1,sharey=ax1)
plt.imshow(img2,cmap='gray')
plt.title('Filtro Sobel vertical')
plt.show(block=False)


# --- Filtro Laplaciano ------------------------------------------
img = cv2.imread('moon.tif',cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img, cv2.CV_64F) # El tamaño del kernel por defecto es 3x3 (ksize=3)
# laplacian = cv2.Laplacian(img.astype(float), -1) 
img_res = img - laplacian
img_res_8 = cv2.convertScaleAbs(img_res)   # Toma valor absoluto - Satura - pasa a uint8 

ax1 = plt.subplot(221)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(laplacian,cmap='gray')
plt.colorbar(h)
plt.title('Filtro Laplaciano')
plt.subplot(223,sharex=ax1,sharey=ax1)
h=plt.imshow(img_res,cmap='gray')
plt.colorbar(h)
plt.title('Imagen resaltada')
plt.subplot(224,sharex=ax1,sharey=ax1)
h=plt.imshow(img_res_8,cmap='gray')
plt.colorbar(h)
plt.title('Imagen resaltada - uint8')
plt.show(block=False)


# --- Filtro Laplaciano - Comparación de diferentes implementaciones -----------------------------
img = cv2.imread('moon.tif',cv2.IMREAD_GRAYSCALE)
w4 = np.array([[0,1,0],[1,-4,1],[0,1,0]], np.float32)
w8 = np.array([[1,1,1],[1,-8,1],[1,1,1]], np.float32)
img_w4 = img.astype(np.float32) - cv2.filter2D(img, -1, w4) 
img_w8 = img.astype(np.float32) - cv2.filter2D(img, -1, w8) 
img_w4 = cv2.convertScaleAbs(img_w4)
img_w8 = cv2.convertScaleAbs(img_w8)

ax1 = plt.subplot(221)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(img_w4,cmap='gray')
plt.colorbar(h)
plt.title('Filtro Laplaciano -4')
plt.subplot(223,sharex=ax1,sharey=ax1)
h=plt.imshow(img_w8,cmap='gray')
plt.colorbar(h)
plt.title('Filtro Laplaciano -8')
plt.show(block=False)


# --- Filtro de Mediana ---------------------------------------------------------------------------
def imnoise_salt_pepper(img, p=0.2):
    #   imnoise_salt_pepper(img, p=0.2)
    # img: Imagen 2D de entrada.
    # p: porcentaje de píxeles afectados por el ruido (debe ser un valor entre 0 y 1)
    # Salida: imagen + ruido salt (255) and pepper (0).
    img_noise = img.copy()
    x = np.random.rand(*img.shape)
    img_noise[ x <p/2 ] = 0
    img_noise[ (x > p/2)  & (x<p) ] = 255
    return img_noise

img = cv2.imread('circuit_board.tif',cv2.IMREAD_GRAYSCALE)
img_noise1 = imnoise_salt_pepper(img,0.1)
img_noise2 = imnoise_salt_pepper(img,0.2)
img_noise3 = imnoise_salt_pepper(img,0.5)

ax1 = plt.subplot(221)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise1,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.1')
plt.subplot(223,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise2,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.2')
plt.subplot(224,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise3,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5')
plt.show(block=False)


img_noise1_filt = cv2.medianBlur(img_noise1,3)
img_noise2_filt = cv2.medianBlur(img_noise2,3)
img_noise3_filt3 = cv2.medianBlur(img_noise3,3)
img_noise3_filt5 = cv2.medianBlur(img_noise3,5)

ax1 = plt.subplot(221)
h=plt.imshow(img_noise1,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.1')
plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise1_filt,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.1 - Filtrada')
ax1 = plt.subplot(223)
h=plt.imshow(img_noise3,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5')
plt.subplot(224,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise3_filt5,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5 - Filtrada')

plt.show(block=False)


ax1 = plt.subplot(221)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h)
plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise3, cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5')
ax1 = plt.subplot(223)
h=plt.imshow(img_noise3_filt3,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5 - Filtrada (k=3)')
plt.subplot(224,sharex=ax1,sharey=ax1)
h=plt.imshow(img_noise3_filt5,cmap='gray')
plt.colorbar(h)
plt.title('Imagen con ruido salt & pepper - 0.5 - Filtrada (k=5)')

plt.show(block=False)
