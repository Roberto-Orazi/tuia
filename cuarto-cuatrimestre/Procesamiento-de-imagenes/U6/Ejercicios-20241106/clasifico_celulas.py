import cv2
from matplotlib import pyplot as plt
import numpy as np

# --- Cargo imagen ----------------------------------------------------------------------
source_img = np.float32(cv2.imread('celulas.tiff', cv2.IMREAD_GRAYSCALE))
np.unique(source_img)
H, W = source_img.shape[:2]
plt.figure(); plt.imshow(source_img, cmap='gray'); plt.show(block=False)

# --- Binarizo --------------------------------------------------------------------------
_, binary_img = cv2.threshold(source_img, 127, 1, cv2.THRESH_BINARY)
print(binary_img.shape)
binary_img = binary_img.astype(np.uint8)
plt.figure(), plt.imshow(binary_img, cmap='gray'), plt.show(block=False)

# --- Componentes conectadas ------------------------------------------------------------
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_img)
plt.figure(), plt.imshow(labels, cmap='gray'), plt.show(block=False)

labels_color = np.uint8(255/(num_labels-1)*labels)                  # Llevo el rango de valores a [0 255] para diferenciar mejor los colores
# np.unique(labels_color)                                           # Por si quieren verificar los valores asignados....
im_color = cv2.applyColorMap(labels_color, cv2.COLORMAP_JET)
im_color = cv2.cvtColor(im_color, cv2.COLOR_BGR2RGB)                # El mapa de color que se aplica está en BGR --> convierto a RGB
plt.figure(), plt.imshow(im_color), plt.show(block=False)

# --- Defino parametros para la clasificación -------------------------------------------
RHO_TH = 0.8    # Factor de forma (rho)
AREA_TH = 500   # Umbral de area
aux = np.zeros_like(labels)
labeled_image = cv2.merge([aux, aux, aux])

# --- Clasificación ---------------------------------------------------------------------
# Clasifico en base al factor de forma
for i in range(1, num_labels):

    # --- Remuevo las celulas que tocan el borde de la imagen -----------------
    if (stats[i, cv2.CC_STAT_LEFT] == 0 or 
        stats[i, cv2.CC_STAT_TOP] == 0 or 
        stats[i, cv2.CC_STAT_HEIGHT] + stats[i, cv2.CC_STAT_TOP] == H or 
        stats[i, cv2.CC_STAT_WIDTH] + stats[i, cv2.CC_STAT_LEFT] == W):
        continue

    # --- Remuevo celulas con area chica --------------------------------------
    if (stats[i, cv2.CC_STAT_AREA] < AREA_TH):
        continue

    # --- Selecciono el objeto actual -----------------------------------------
    obj = (labels == i).astype(np.uint8)

    # --- Calculo Rho ---------------------------------------------------------
    ext_contours, _ = cv2.findContours(obj, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = cv2.contourArea(ext_contours[0])
    perimeter = cv2.arcLength(ext_contours[0], True)
    rho = 4 * np.pi * area/(perimeter**2)
    flag_circular = rho > RHO_TH

    # --- Calculo cantidad de huecos ------------------------------------------
    all_contours, _ = cv2.findContours(obj, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    holes = len(all_contours) - 1

    # --- Muestro por pantalla el resultado -----------------------------------
    print(f"Objeto {i:2d} --> Circular: {flag_circular}  /  Huecos: {holes}")

    # --- Clasifico -----------------------------------------------------------
    if flag_circular:
        if holes == 1:
            labeled_image[obj == 1, 0] = 255    # Circular con 1 hueco
        else:
            labeled_image[obj == 1, 1] = 255    # Circular con mas de 1 hueco
    else:
        labeled_image[obj == 1, 2] = 255        # No circular

plt.figure(); plt.imshow(labeled_image); plt.show(block=False)
