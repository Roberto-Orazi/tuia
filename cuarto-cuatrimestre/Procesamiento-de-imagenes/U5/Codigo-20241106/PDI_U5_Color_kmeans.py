import numpy as np
import cv2
import matplotlib.pyplot as plt

# --- Cargo Imagen ----------------------------------------------------------------------------
img = cv2.imread('home.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(); plt.imshow(img), plt.show(block=False)

# --- Preparo datos ---------------------------------------------------------------------------
Z = img.reshape((-1,3))   # Genero una matriz de Nx3 con todos los valores de los pixels de la imagen (N = ancho x alto)
Z = np.float32(Z)         # Paso a float
Ncolors = len(np.unique(Z, axis=0))

# --- Aplico K-means para obtener la paleta de colores (Cuantización de colores) --------------
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 20
# K = 4
K = 8
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# --- Obtengo la nueva imagen con la nueva paleta de colores ----------------------------------
center = np.uint8(center)
aux = center[label.flatten()]
imgQ = aux.reshape((img.shape))

plt.figure()
ax1 = plt.subplot(121); plt.xticks([]), plt.yticks([]), plt.imshow(img), plt.title(f'Imagen Original. Ncolors = {Ncolors}')
plt.subplot(122, sharex=ax1, sharey=ax1), plt.imshow(imgQ), plt.title(f'Imagen con colores cuantizados --> K = {K}')
plt.show(block=False)

# --- Gráfico de torta ------------------------------------------------------------------------
colours, counts = np.unique(imgQ.reshape(-1,3), axis=0, return_counts=1)    # Obtengo colores y cuentas
idx = np.argsort(-counts)   # Esto es opcional...
counts = counts[idx]        # Ordeno en base a frecuencia de ocurrencias 
colours = colours[idx]      # 
counts_pct = counts/np.sum(counts)*100  # Paso a porcentaje
labels = [f'{counts_pct[ii]:6.2f}%  ({colours[ii,0]:3d},{colours[ii,1]:3d},{colours[ii,2]:3d})' for ii in range(len(counts))]
col = [(c[0]/255., c[1]/255., c[2]/255.) for c in colours]

fig= plt.figure(figsize=(9,5))
ax = fig.add_subplot(111) 
ax.pie(counts_pct, labels=labels, colors=col)
pos1 = ax.get_position()
pos2 = [0.15, pos1.y0, pos1.width, pos1.height] 
ax.set_position(pos2) 
plt.legend(title = f"Colores RGB ({K})", bbox_to_anchor=(1.4, 1), loc='upper left', borderaxespad=0.5, fontsize=10)   # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.title("Proporción de Colores")
plt.show(block=False)


# --- Muestro mascaras --------------------------------------------------------
# !!! Esta hecho para kmeans con k=8 !!!
plt.figure()
ax1 = plt.subplot(331); plt.xticks([]), plt.yticks([]), plt.imshow(img), plt.title('Imagen Original')
for ii in range(8):
    plt.subplot(3,3,ii+2,sharex=ax1,sharey=ax1) 
    col_sel = colours[ii]
    mask_R = img[:,:,0] == col_sel[0]
    mask_G = img[:,:,1] == col_sel[1]
    mask_B = img[:,:,2] == col_sel[2]
    mask = np.uint8(mask_R & mask_B & mask_B)*255
    plt.imshow(mask, cmap='gray')
    plt.title(f'Color ({col_sel[0]},{col_sel[1]},{col_sel[2]}): {counts_pct[ii]:5.2f}% ({counts[ii]}) pixels')
plt.show(block=False)
# Porque no se ven casi puntos para cada color?? Analizar...

# --- Muestro mascaras --------------------------------------------------------
plt.figure()
ax1 = plt.subplot(331); plt.xticks([]), plt.yticks([]), plt.imshow(img), plt.title('Imagen Original')
for ii in range(8):
    plt.subplot(3,3,ii+2,sharex=ax1,sharey=ax1) 
    col_sel = colours[ii]
    mask_R = imgQ[:,:,0] == col_sel[0]
    mask_G = imgQ[:,:,1] == col_sel[1]
    mask_B = imgQ[:,:,2] == col_sel[2]
    plt.title(f'Color ({col_sel[0]},{col_sel[1]},{col_sel[2]}): {counts_pct[ii]:5.2f}% ({counts[ii]}) pixels')    
    # --- Opcion binario -----------------
    # mask = np.uint8(mask_R & mask_B & mask_B)*255
    # plt.imshow(mask, cmap='gray')
    # --- Opcion color --------------------
    mask = mask_R & mask_B & mask_B
    result = img.copy()     # Mascara sobre la imagen Original...
    # result = imgQ.copy()     # Mascara sobre la imagen procesada..
    result[~mask,:] = 0     
    plt.imshow(result)
plt.show(block=False)

