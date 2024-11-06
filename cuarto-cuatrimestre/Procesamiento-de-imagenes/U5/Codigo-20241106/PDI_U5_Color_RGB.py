import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Ejemplo: Puntos en el espacio RGB -----------------------------------------------------------------
N = 10000 # Probar 1000 - 10000 - ...
RGBlist = np.random.randint(0,255,(N,3))
colors = [(RGBlist[ii,0] / 255., RGBlist[ii,1] / 255., RGBlist[ii,2] / 255.) for ii in range(N)]

fig = plt.figure()
fig.suptitle(f"Espacio de Colores RGB: {N} colores")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(RGBlist[:,0], RGBlist[:,1], RGBlist[:,2], c=colors)
ax.grid(False)
ax.set_xlabel("R")
ax.set_ylabel("G")
ax.set_zlabel("B")
ax.set_xlim((0, 255))
ax.set_ylim((0, 255))
ax.set_zlim3d((0, 255))
plt.show(block=False)

# ---- Ejemplo: Graficar todos los colores que aparecen en una imagen ---------------------
img = cv2.imread("peppers.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.show(block=False)

img_all_rgb_codes = img.reshape(-1, img.shape[-1])
img_unique_rgbs = np.unique(img_all_rgb_codes, axis=0)
colors = [(img_unique_rgbs[ii,0] / 255., img_unique_rgbs[ii,1] / 255., img_unique_rgbs[ii,2] / 255.) for ii in range(img_unique_rgbs.shape[0])]

# Cuidado al realizar esta gráfica, puede ser muy pesada y tildar el host....
fig = plt.figure()
fig.suptitle(f"Cantidad de colores que aparecen: {len(colors)}")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(img_unique_rgbs[:,0], img_unique_rgbs[:,1], img_unique_rgbs[:,2], c=colors)
# ax.grid(False)
ax.set_xlabel("R")
ax.set_ylabel("G")
ax.set_zlabel("B")
ax.set_xlim((0, 255))
ax.set_ylim((0, 255))
ax.set_zlim3d((0, 255))
plt.show(block=False)

# --- Grafico de torta -----------------------------------------------------------------------------
colours, counts = np.unique(img_all_rgb_codes, axis=0, return_counts=1)    # Obtengo colores y cuentas
idx = np.argsort(-counts)       # Esto es opcional...
N = 8                           #
counts = counts[idx[:N]]        # Ordeno en base a frecuencia de ocurrencias 
colours = colours[idx[:N]]      # 
counts_pct = counts/np.sum(counts)*100  # Paso a porcentaje
labels = [f'{counts_pct[ii]:6.2f}%  ({colours[ii,0]:3d},{colours[ii,1]:3d},{colours[ii,2]:3d})' for ii in range(len(counts))]
col = [(c[0]/255., c[1]/255., c[2]/255.) for c in colours]

fig= plt.figure(figsize=(9,5))
ax = fig.add_subplot(111) 
ax.pie(counts_pct, labels=labels, colors=col)
pos1 = ax.get_position()
pos2 = [0.15, pos1.y0, pos1.width, pos1.height] 
ax.set_position(pos2) 
plt.legend(title = "Colores RGB:", bbox_to_anchor=(1.4, 1), loc='upper left', borderaxespad=0.5, fontsize=10)   # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.title("Proporción de Colores")
plt.show(block=False)

# --- Muestro mascaras --------------------------------------------------------
plt.figure()
ax1 = plt.subplot(331); plt.xticks([]), plt.yticks([]), plt.imshow(img), plt.title('Imagen Original')
for ii in range(N):
    plt.subplot(3,3,ii+2,sharex=ax1,sharey=ax1) 
    col_sel = colours[ii]
    mask_R = img[:,:,0] == col_sel[0]
    mask_G = img[:,:,1] == col_sel[1]
    mask_B = img[:,:,2] == col_sel[2]
    mask = np.uint8(mask_R & mask_B & mask_B)*255
    plt.imshow(mask, cmap='gray')
    plt.title(f'Color ({col_sel[0]},{col_sel[1]},{col_sel[2]}): {counts_pct[ii]:5.2f}% ({counts[ii]}) pixels')
plt.show(block=False)

