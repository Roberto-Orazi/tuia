import cv2
from matplotlib import pyplot as plt
import numpy as np

# --- Cargo imagen --------------------------------------------------------------------------------
img = cv2.imread('letrasAB.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.show(block=False)

# --- Filtro --------------------------------------------------------------------------------------
img_fil = cv2.medianBlur(img, 5)
plt.figure(), plt.imshow(img_fil), plt.show(block=False)

# --- Paso a escala de grises ---------------------------------------------------------------------
img_fil_gray = cv2.cvtColor(img_fil, cv2.COLOR_RGB2GRAY)
plt.figure(), plt.imshow(img_fil_gray, cmap='gray'), plt.show(block=False)

# --- Binarizo ------------------------------------------------------------------------------------
th, binary_img = cv2.threshold(img_fil_gray, 125, 1, cv2.THRESH_OTSU)
plt.figure(), plt.imshow(binary_img, cmap='gray'), plt.show(block=False)

# --- Operaciones morfológicas para mejorar la segmentación obtenida ------------------------------
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
binary_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, se)   # Apertura para remover elementos pequeños
binary_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, se)  # Clausura para rellenar huecos.
plt.figure(), plt.imshow(binary_img, cmap='gray'), plt.show(block=False)

# --- Obtengo componentes conectados --------------------------------------------------------------
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_img)
plt.figure(), plt.imshow(labels, cmap='gray'), plt.show(block=False)        # Visualizo los objetos con sus labels en ESCALA DE GRISES

# *** OPCIONAL ****************************************************************
# Para visualizar mejor, observo los objetos en COLOR
# im_color = cv2.applyColorMap(labels.astype(np.uint8), cv2.COLORMAP_JET)     # El rango actual de valores es 0 a num_labels-1 (20).
#                                                                             # Como es tan chico el rango comparado al rango total [0 255], los colores son muy parecidos.
#                                                                             # Es conveniente llevar el rango de valores al rango [0 255] para generar colores mas diferentes entre si.
labels_color = np.uint8(255/(num_labels-1)*labels)                  # Llevo el rango de valores a [0 255] para diferenciar mejor los colores
# np.unique(labels_color)                                           # Por si quieren verificar los valores asignados....
im_color = cv2.applyColorMap(labels_color, cv2.COLORMAP_JET)
im_color = cv2.cvtColor(im_color, cv2.COLOR_BGR2RGB)                # El mapa de color que se aplica está en BGR --> convierto a RGB
plt.figure(), plt.imshow(im_color), plt.show(block=False)
# *****************************************************************************

# --- Clasificacion -------------------------------------------------------------------------------
labeled_shapes = np.zeros_like(img)
for i in range(1, num_labels):
    obj = (labels == i).astype(np.uint8)                                            # Genero una imagen que contenga solo el objeto "i"
    contours, _ = cv2.findContours(obj, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)     # Obtengo los contornos del objeto
    if len(contours) == 3:
        labeled_shapes[obj == 1, 2] = 255  # Si tiene 3 contornos --> B 
    else:
        labeled_shapes[obj == 1, 0] = 255  # Caso contrario --> A

plt.figure(), plt.imshow(labeled_shapes), plt.show(block=False)

