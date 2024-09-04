import cv2
import numpy as np

def update(_):
    # --- Obtengo parámetros de la GUI -----------------------------------
    val = cv2.getTrackbarPos("Slider_1", "Imagen")

    # --- Actualizo ------------------------------------------------------ img_modif = img+val   # Por que así da mal?
    img_modif = img.astype(np.double) + val
    img_modif = cv2.convertScaleAbs(img_modif, None, alpha=1, beta=0)
    cv2.imshow("Imagen", img_modif)

# --- Cargo imagen -------------------------------------------------------
src_path = "cameraman.tif"
img = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Imagen Original", img)

# --- GUI ----------------------------------------------------------------
cv2.imshow("Imagen", img)
cv2.createTrackbar("Slider_1", "Imagen", 0, 50, update)

# --- Loop hasta presionar ESC -------------------------------------------
while True:
    ch = cv2.waitKey()
    if ch == 27:
        break
