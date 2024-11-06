import cv2
import numpy as np
import matplotlib.pyplot as plt

# Defininimos función para mostrar imágenes
def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=False, ticks=False):
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

# -------------------------------------------------------------------------------------------------------------
# --- Thining -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
G123_LUT = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
       1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1,
       0, 0, 0], dtype=np.bool_)

G123P_LUT = np.array([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0,
       0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1,
       0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0], dtype=np.bool_)

def imthin(image, n_iter=None):
    """
    imthin: Realiza el adelgazamiento (thinning) morfológico de una imagen binaria.

    Parametros
    ----------
    image   : Imagen binaria (M,N) ndarray, valores permitidos: 0 y 1.
    n_iter  : int, numero de iteraciones (opcional).

    Salida
    ------
    out     : Imagen binaria (M,N) ndarray. Imagen adelgazada (thinned).

    Referencias
    ----------
    [1] Z. Guo and R. W. Hall, "Parallel thinning with two-subiteration algorithms," Comm. ACM, vol. 32, no. 3, pp. 359-373, 1989.
    [2] Lam, L., Seong-Whan Lee, and Ching Y. Suen, "Thinning Methodologies-A Comprehensive Survey," IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol 14, No. 9, 1992, p. 879
    """
    # --- Check n_iter -----------------------------------------
    if n_iter is None:
        n = -1
    elif n_iter <= 0:
        raise ValueError('n_iter must be > 0')
    else:
        n = n_iter
    
    # --- Check image ------------------------------------------
    skel = np.array(image).astype(np.uint8)
    if skel.ndim != 2:
        raise ValueError('"image" debe ser un array 2D.')
    if not np.all(np.in1d(image.flat,(0,1))):
        raise ValueError('"image" debe contener valores 0s y 1s solamente.')

    # --- Definiciones iniciales -------------------------------
    mask = np.array([[ 8,  4,  2],
                     [16,  0,  1],
                     [32, 64,128]],dtype=np.uint8)

    # --- Procesamiento ----------------------------------------
    while n != 0:
        before = np.sum(skel)                                                   # Cuento la cantidad de pixels True antes de esta iteración...
        # ----------------------------------
        for lut in [G123_LUT, G123P_LUT]:                                       # sub-itero para cada LUT
            N = cv2.filter2D(skel, -1, mask, borderType=cv2.BORDER_CONSTANT)    # Correlación entre la imagen y la máscara 
            D = np.take(lut, N)                                                 # Decido que pixels eliminar en base al resultado de la correlación y la LUT.
            skel[D] = 0                                                         # Elimino pixels (adelgazo)            
        # ----------------------------------
        after = np.sum(skel)                                                    # Cuento la cantidad de pixels True al final de esta iteración.
        if before == after:                                                     # Si no hay cambios, no itero mas, termine el adelgazamiento...
            break   
        n -= 1                                                                  # Caso contrario, decremento n
    return skel.astype(np.bool_)                                                
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# --- Cargo imagen ---------------------------------------
img = cv2.imread("cromosoma.tif", cv2.IMREAD_GRAYSCALE)
img.shape
W,H = img.shape
imshow(img, title="Imagen Original")

# --- Filtro ruido ---------------------------------------
img_b = cv2.GaussianBlur(img, (25,25), 15.0)
imshow(img_b, title="Imagen Filtrada (PB)")

# --- Umbralado ------------------------------------------
th, img_bin = cv2.threshold(img_b, 127, 255, cv2.THRESH_OTSU)
th
imshow(img_bin, title="Imagen umbralada")

# # ---- Suavizado -----------------------------------------
# st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (60,60))
# img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, st)
# imshow(img_bin, title="Imagen umbralada")

# --- Contorno Exterior ----------------------------------
ext_contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_out = cv2.merge((img_bin,img_bin,img_bin))
cv2.drawContours(img_out, ext_contours, -1, (255,0,0), 2)
imshow(img_out, title="Contorno exterior")

# --- Esqueleto --------------------------------------------------
th, thin_input= cv2.threshold(img_bin,127, 1, cv2.THRESH_OTSU)
np.unique(thin_input)
img_skel = imthin(thin_input)
np.unique(img_skel)
imshow(img_skel, "Esqueleto")

# --- Imagen con contorno y esqueleto resaltado -------------------
img_out[img_skel] = (0,0,255)
imshow(img_out, title="Contorno exterior + Esqueleto")

# --- Cuento los extremos (endpoints) -----------------------------
f = img_skel.copy()
f = f.astype(np.uint8)*255
np.unique(f)

def endpoints(f):
    B1 = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, -1]])
    B2 = np.array([[-1, 1, -1], [-1, 1, -1], [-1, -1, -1]])
    B3 = np.array([[-1, -1, 1], [-1, 1, -1], [-1, -1, -1]])
    B4 = np.array([[-1, -1, -1], [1, 1, -1], [-1, -1, -1]])
    B5 = np.array([[-1, -1, -1], [-1, 1, 1], [-1, -1, -1]])
    B6 = np.array([[-1, -1, -1], [-1, 1, -1], [1, -1, -1]])
    B7 = np.array([[-1, -1, -1], [-1, 1, -1], [-1, 1, -1]])
    B8 = np.array([[-1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
    f1 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B1)
    f2 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B2)
    f3 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B3)
    f4 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B4)
    f5 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B5)
    f6 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B6)
    f7 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B7)
    f8 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B8)

    fend = f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8
    
    return fend

f_endpoints = endpoints(f)
(f_endpoints>0).sum()
f_endpoints_cord = np.argwhere(f_endpoints)
f_endpoints_cord

xx = img_out.copy()
for p in f_endpoints_cord:
    cv2.circle(xx, tuple((p[1],p[0])), 5, (0,255,0), -1)
imshow(xx)