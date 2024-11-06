import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

# Defininimos función para mostrar imágenes
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

# --- Rotaciones -------------------------------------------------------------------
#  --> Tutorial: https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html
img = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('mammogram.tif', cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
imshow(img, title="Imagen Original")

M = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
M = cv2.getRotationMatrix2D((0,0), 90, 1)  #  Por que todo negro??
M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
img_rot_1 = cv2.warpAffine(img, M, (cols,rows))
img_rot_2 = cv2.warpAffine(img, M, (cols*2,rows*2))

imshow(img_rot_1, title="Imagen Rotada")
imshow(img_rot_2, title="Imagen Rotada - Tamaño duplicado")

# --- Analizar tamaño ejes -----------
plt.figure()
plt.subplot(221), imshow(img, title='Imagen Original', new_fig=False, colorbar=False, ticks=True)
plt.subplot(222), imshow(img_rot_1, title="Imagen Rotada", new_fig=False, colorbar=False, ticks=True)
plt.subplot(223), imshow(img_rot_2, title="Imagen Rotada - Tamaño duplicado", new_fig=False, colorbar=False, ticks=True)
plt.show(block=False)
# ------------------------------------

plt.figure()
ax1 = plt.subplot(221); imshow(img, title='Imagen Original', new_fig=False, colorbar=False, ticks=True)
plt.subplot(222,sharex=ax1,sharey=ax1), imshow(img_rot_1, title="Imagen Rotada", new_fig=False, colorbar=False, ticks=True)
plt.subplot(223,sharex=ax1,sharey=ax1), imshow(img_rot_2, title="Imagen Rotada - Tamaño duplicado", new_fig=False, colorbar=False, ticks=True)
plt.show(block=False)

# Analisis de los distintos tipos de borderMode
M = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
M = cv2.getRotationMatrix2D((0,0), 90, 1)
M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
k=2 # Analizar con 3,4,...
img_rot_3a = cv2.warpAffine(img, M, (cols*k,rows*k), borderMode=cv2.BORDER_CONSTANT, borderValue=127)
img_rot_3b = cv2.warpAffine(img, M, (cols*k,rows*k), borderMode=cv2.BORDER_REPLICATE)
img_rot_3c = cv2.warpAffine(img, M, (cols*k,rows*k), borderMode=cv2.BORDER_REFLECT)
img_rot_3d = cv2.warpAffine(img, M, (cols*k,rows*k), borderMode=cv2.BORDER_WRAP)

plt.figure()
ax1 = plt.subplot(221); imshow(img_rot_3a, title="BORDER_CONSTANT", new_fig=False, colorbar=False)
plt.subplot(222,sharex=ax1,sharey=ax1), imshow(img_rot_3b, title="BORDER_REPLICATE", new_fig=False, colorbar=False)
plt.subplot(223,sharex=ax1,sharey=ax1), imshow(img_rot_3c, title="BORDER_REFLECT", new_fig=False, colorbar=False)
plt.subplot(224,sharex=ax1,sharey=ax1), imshow(img_rot_3d, title="BORDER_WRAP", new_fig=False, colorbar=False)
plt.show(block=False)

# --- Posible solución -----------------------------------------------------------------------
M = cv2.getRotationMatrix2D((0,0), 45, 1)
M = cv2.getRotationMatrix2D((0,0), 90, 1)
M = cv2.getRotationMatrix2D((0,0), 135, 1)
M = cv2.getRotationMatrix2D((0,0), 225, 1)
img_T = cv2.warpAffine(img, M, (cols,rows))
imshow(img_T, title="Imagen Transformada")

# Desplazo y aplico transformación
diag = np.hypot(rows, cols)
M_modif = M.copy()
M_modif[0, 2] += diag
M_modif[1, 2] += diag
img_T_modif = cv2.warpAffine(img, M_modif, (3*cols,3*rows))
imshow(img_T_modif, title="Imagen Transformada con desplazamiento")

# Recorto
cols_nonzero = np.where(np.any(img_T_modif, 0))[0]
ic_ini = cols_nonzero[0]
ic_end = cols_nonzero[-1]
rows_nonzero = np.where(np.any(img_T_modif, 1))[0]
ir_ini = rows_nonzero[0]
ir_end = rows_nonzero[-1]
img_T2 = img_T_modif[ir_ini:ir_end+1, ic_ini:ic_end+1]
imshow(img_T2, title="Imagen Transformada con desplazamiento + recorte")
img_T2.shape

# --- Rotacion sin cortar --------------------------------------------------------------------
img_rot90 = imutils.rotate_bound(img, 90)
img_rot45 = imutils.rotate_bound(img, 45)
# img_rot45 = imutils.rotate(img, 45)
img_rotm33 = imutils.rotate_bound(img, -33)

plt.figure()
plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('Imagen Original')
plt.subplot(222), plt.imshow(img_rot90, cmap='gray'), plt.title('Imagen Rotada 90')
plt.subplot(223), plt.imshow(img_rot45, cmap='gray'), plt.title('Imagen Rotada 45')
plt.subplot(224), plt.imshow(img_rotm33, cmap='gray'), plt.title('Imagen Rotada -33')
plt.show(block=False)


# --- Transformaciones afines ---------------------------------------------------
# ==============================================================================
# En una transformación afín, todas las líneas paralelas de la imagen original 
# seguirán siendo paralelas en la imagen de salida. 
# Para encontrar la matriz de transformación, necesitamos tres puntos de la 
# imagen de entrada y sus correspondientes ubicaciones en la imagen de salida. 
# Entonces cv2.getAffineTransform creará una matriz de 2x3 que se 
# pasará a cv2.warpAffine.
# ==============================================================================

# Cargo Imagen
img = cv2.imread('lines.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols,_ = img.shape
imshow(img, title="Imagen Original", color_img=True, colorbar=False)

# Transformación Afín
pts1 = np.float32([[50,50], [200,50], [50,200]])      # Defino 3 puntos en la imagen de entrada...
pts2 = np.float32([[10,100], [200,50], [100,250]])    # Defino sus correspondientes posiciones en la imagen de salida...
M = cv2.getAffineTransform(pts1, pts2)                # Obtengo la matriz de la transformación afín.
img_warp = cv2.warpAffine(img, M, (cols,rows))
# img_warp = cv2.warpAffine(img, M, (2*cols, 2*rows))

# Agrego los puntos
cv2.circle(img, tuple(np.int32(pts1[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[2])), radius=5, color=(255,0,0), thickness=-1)

# Muestro
plt.figure()
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Scale -------------------------------------------------------
img = cv2.imread('lines.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pts1 = np.float32([[0,0], [cols-1,0], [0,rows-1]])            # Defino 3 puntos en la imagen de entrada...
pts2 = np.float32([[0,0], [2*(cols-1),0], [0,2*(rows-1)]])    # Escalo x2 en ambos ejes 
M = cv2.getAffineTransform(pts1, pts2)                       # Obtengo la matriz de la transformación afín.
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
# Agrego los puntos
cv2.circle(img, tuple(np.int32(pts1[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[2])), radius=5, color=(255,0,0), thickness=-1)
# Muestro
plt.figure()
ax1=plt.subplot(121); plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Traslacion -------------------------------------------------------
img = cv2.imread('lines.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pts1 = np.float32([[0,0], [cols-1,0], [0,rows-1]])            # Defino 3 puntos en la imagen de entrada...
x_desp = 100
y_desp = 200
pts2 = pts1.copy()
pts2[:,0] += x_desp
pts2[:,1] += y_desp
M = cv2.getAffineTransform(pts1, pts2)               # Obtengo la matriz de la transformación afín.
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
# Agrego los puntos
cv2.circle(img, tuple(np.int32(pts1[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img, tuple(np.int32(pts1[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[2])), radius=5, color=(255,0,0), thickness=-1)
# Muestro
plt.figure()
ax1=plt.subplot(121); plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Traslacion 2 -------------------------------------------------------
M = np.array([[1., 0., 100], [0., 1., 200]])
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
plt.figure()
ax1=plt.subplot(121); plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Escalado 2 -------------------------------------------------------
M = np.array([[2., 0., 0], [0., 2., 0]])
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
plt.figure()
ax1=plt.subplot(121); plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Shear Horizontal -------------------------------------------------------
M = np.array([[1., 0.8, 0.],[0., 1., 0.]])
M = np.array([[1., -0.8, 0.],[0., 1., 0.]])
M = np.array([[1., -0.8, 400],[0., 1., 0.]])
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
plt.figure(); ax1=plt.subplot(121)
plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# --- Ejemplo: Shear Vertical -------------------------------------------------------
M = np.array([[1., 0., 0.],[0.4, 1., 0.]])
# M = np.array([[1., 0., 0.],[-0.4, 1., 0.]])
# M = np.array([[1., 0., 0.],[-0.4, 1., 300]])
img_warp = cv2.warpAffine(img, M, (cols*2, rows*2))
plt.figure()
ax1=plt.subplot(121); plt.imshow(img), plt.title('Input')
plt.subplot(122,sharex=ax1,sharey=ax1), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)


# --- Otro ejemplo: Espejado ----------------------------------
img = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
pts1 = np.float32([[0,0], [cols-1,0], [0,rows-1]])     
pts2 = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
M = cv2.getAffineTransform(pts1, pts2)               
img_warp = cv2.warpAffine(img, M, (rows, cols))
plt.figure()
plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title('Input')
plt.subplot(122), plt.imshow(img_warp, cmap="gray"), plt.title('Output')
plt.show(block=False)

# ---------------------------------------------------------------------------------
# --- Homography ------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# ---------------------------------------------------
# --- Ejemplo 1 -------------------------------------------------------------------
# ---------------------------------------------------
img = cv2.imread('libro.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols,_ = img.shape
imshow(img, title="Imagen Original", colorbar=False)

# Obtengo puntos de los extremos del libro
pts_src = np.array([[333,82], [771,166], [665,775], [183,669]])  # sup-izq | sup-der | inf-der | inf-izq
img_points = img.copy()
cv2.circle(img_points, tuple(np.int32(pts_src[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(img_points, title="Imagen Original + puntos seleccionados", colorbar=False)

# Obtengo puntos destino
ancho = int(np.sqrt(np.sum(np.power(pts_src[0]-pts_src[1],2))))
alto = int(np.sqrt(np.sum(np.power(pts_src[1]-pts_src[2],2))))
pts_dst = np.array([[0,0], [ancho-1,0], [ancho-1,alto-1], [0,alto-1]])  # sup-izq | sup-der | inf-der | inf-izq

# Aplico Homography
h, status = cv2.findHomography(pts_src, pts_dst)
im_dst = cv2.warpPerspective(img, h, (ancho,alto))
im_dst.shape
cv2.circle(im_dst, tuple(np.int32(pts_dst[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(im_dst, title="Imagen Transformada", colorbar=False)

# Muestro 
plt.figure()
plt.subplot(121), plt.imshow(img_points), plt.title("Imagen Original")
plt.subplot(122), plt.imshow(im_dst), plt.title("Imagen Transformada")
plt.show(block=False)

plt.figure()
ax1=plt.subplot(122); plt.imshow(im_dst), plt.title("Imagen Transformada")
plt.subplot(121, sharex=ax1, sharey=ax1), plt.imshow(img_points), plt.title("Imagen Original")
plt.show(block=False)

# --- Visualizo toda la imagen ----------------
pts_dst2 = pts_dst.copy()
# pts_dst2 += 500             # Desplazo todo en (500,500)
pts_dst2 += [400, 500]      # Desplazo todo en (400,500)
h, status = cv2.findHomography(pts_src, pts_dst2)
im_dst2 = cv2.warpPerspective(img, h, (ancho*3,alto*3))
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(im_dst2, colorbar=False)

# --- Intento con transformación afin ------------------------------
pts1 = np.float32(pts_src[0:3])
pts2 = np.float32(pts_dst[0:3])
M = cv2.getAffineTransform(pts1, pts2) 
img_warp = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
# Agrego los puntos
cv2.circle(img_warp, tuple(np.int32(pts2[0])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[1])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[2])), radius=10, color=(255,0,0), thickness=-1)
# Muestro
plt.figure()
plt.subplot(121), plt.imshow(img_points), plt.title('Input')
plt.subplot(122), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# ---------------------------------------------------
# --- Ejemplo 2 -------------------------------------------------------------------
# ---------------------------------------------------
img = cv2.imread('lane.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols,_ = img.shape
imshow(img, title="Imagen Original", colorbar=False)

# Obtengo puntos de los extremos del libro
pts_src = np.array([[433,438], [542,438], [910,608], [80, 608]])  # sup-izq | sup-der | inf-der | inf-izq
img_points = img.copy()
cv2.circle(img_points, tuple(np.int32(pts_src[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(img_points, tuple(np.int32(pts_src[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(img_points, title="Imagen Original + puntos seleccionados", colorbar=False)

# Obtengo puntos destino
alto = int(np.sqrt(np.sum(np.power(pts_src[0]-pts_src[3],2))))
ancho = int(np.sqrt(np.sum(np.power(pts_src[2]-pts_src[3],2))))
pts_dst = np.array([[0,0], [ancho-1,0], [ancho-1,alto-1], [0,alto-1]])  # sup-izq | sup-der | inf-der | inf-izq

# Aplico Homography
h, status = cv2.findHomography(pts_src, pts_dst)
im_dst = cv2.warpPerspective(img, h, (ancho,alto))
im_dst.shape
cv2.circle(im_dst, tuple(np.int32(pts_dst[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst, tuple(np.int32(pts_dst[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(im_dst, title="Imagen Transformada", colorbar=False)

# --- Visualizo toda la imagen ----------------
pts_dst2 = pts_dst.copy()
pts_dst2 += [1600, 1600]      # Desplazo todo en (400,500)
h, status = cv2.findHomography(pts_src, pts_dst2)
im_dst2 = cv2.warpPerspective(img, h, (ancho*8,alto*8))
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[0])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[1])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[2])), radius=5, color=(255,0,0), thickness=-1)
cv2.circle(im_dst2, tuple(np.int32(pts_dst2[3])), radius=5, color=(255,0,0), thickness=-1)
imshow(im_dst2, colorbar=False)

# --- Intento con transformación afin ------------------------------
pts1 = np.float32(pts_src[0:3])
pts2 = np.float32(pts_dst[0:3])
M = cv2.getAffineTransform(pts1, pts2) 
img_warp = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
# Agrego los puntos
cv2.circle(img_warp, tuple(np.int32(pts2[0])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[1])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp, tuple(np.int32(pts2[2])), radius=10, color=(255,0,0), thickness=-1)
# Muestro
plt.figure()
plt.subplot(121), plt.imshow(img_points), plt.title('Input')
plt.subplot(122), plt.imshow(img_warp), plt.title('Output')
plt.show(block=False)

# Desplazo para ver la imagen completa...
pts3 = pts2.copy()
pts3+=1000
M2 = cv2.getAffineTransform(pts1, pts3) 
img_warp2 = cv2.warpAffine(img, M2, (img.shape[1]*4, img.shape[0]*4))
# Agrego los puntos
cv2.circle(img_warp2, tuple(np.int32(pts3[0])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp2, tuple(np.int32(pts3[1])), radius=10, color=(255,0,0), thickness=-1)
cv2.circle(img_warp2, tuple(np.int32(pts3[2])), radius=10, color=(255,0,0), thickness=-1)
# Muestro
plt.figure()
plt.subplot(121), plt.imshow(img_points), plt.title('Input')
plt.subplot(122), plt.imshow(img_warp2), plt.title('Output')
plt.show(block=False)
