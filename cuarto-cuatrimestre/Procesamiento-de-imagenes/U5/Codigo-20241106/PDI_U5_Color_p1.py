import cv2
import numpy as np
import matplotlib.pyplot as plt

# =======================================================================================
# UNIDAD 5: Color
# PARTE 1: Imágenes RGB e Imágenes indexadas
# =======================================================================================

# Definimos función para mostrar imágenes
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

# --- Imagen RGB ------------------------------------------------------------------------
img = cv2.imread('peppers.png')
img.shape
img.dtype
imshow(img, title="Imagen Original")    # Acá puede verse que OpenCV, por default, carga las imágenes color en formato BGR, no RGB.

# --- Acomodamos canales ----------------------------------------------------------------
# Por default, openCV  carga las imágenes color en formato BGR, no RGB.
# Por lo tanto, re-acomodamos los planos: pasamos de BGR a RGB.
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imshow(img_RGB, title="Imagen Original con planos re-acomodados (BGR --> RGB)")

# --- Separamos canales -----------------------------------------------------------------
B, G, R = cv2.split(img)    # Separo la imagen en sus respectivos canales.
plt.figure(), plt.imshow(R, cmap='gray'), plt.title("Canal R"), plt.colorbar(), plt.show(block=False)   # Analizamos solo el plano R.

plt.figure()                                                                        # Analizamos todos los planos juntos.
ax1 = plt.subplot(221); imshow(img_RGB, title="Imagen RGB", new_fig=False)      
plt.subplot(222,sharex=ax1,sharey=ax1), imshow(R, title="Canal R", new_fig=False)
plt.subplot(223,sharex=ax1,sharey=ax1), imshow(G, title="Canal G", new_fig=False)
plt.subplot(224,sharex=ax1,sharey=ax1), imshow(B, title="Canal B", new_fig=False)
plt.show(block=False)

# --- Modifico un canal ---------------------------------------------------------------
# Anulamos el canal R, es decir, le asignamos valor 0 en todos los pixels de la imagen.
# img2 = img_RGB    # No! así crea una referencia: si se modifica una, se modifica la otra también.  
img2 = img_RGB.copy()  # Así crea una copia. Otra forma sería "img2 = np.array(img_RGB)"
img2[:,:,0] = 0
imshow(img2, title="Canal R anulado")

# Escalamos el canal R
R2 = R.copy()                   # Creo una copia del canal a modificar
R2 = R2*0.5                     # Multiplico la componente R de todos los pixels por 0.5
print(R2.dtype)
R2 = R2.astype(np.uint8)        # Paso a uint8, ya que en la multiplicación anterior, automáticamente se hizo un casting a float
img3 = cv2.merge((R2,G,B))      # Creo la nueva imagen RGB concatenando los 3 planos.
imshow(img3, title="Canal R escalado")

plt.figure()
ax1 = plt.subplot(221); imshow(img_RGB, title="Imagen RGB", new_fig=False)
plt.subplot(222,sharex=ax1,sharey=ax1), imshow(img2, title="Canal R anulado", new_fig=False)
plt.subplot(223,sharex=ax1,sharey=ax1), imshow(img3, title="Canal R escalado", new_fig=False)
plt.show(block=False)

# --- Paleta de Colores ---------------------------------------------------------------
# Obtengamos los colores únicos de la imagen, es decir, su paleta de colores.
img_pixels = img_RGB.reshape(-1,3)                                  # Re-ordeno los pixels, de manera que cada pixel ocupe una fila.
colours, counts = np.unique(img_pixels, axis=0, return_counts=True) # Obtengo los valores únicos de todos los pixels y su frecuencia de aparición.
# colours = np.unique(img_pixels, axis=0)                           #   Así obtendría solo los valores únicos, no su frecuencia de aparición.
idx = np.argsort(counts)        # Solo para mayor facilidad en el análisis...
counts = counts[idx]            # ... ordeno los colores segun su frecuencia de aparición.
colours = colours[idx]          # El ultimo elemento de counts posee el color con mayor frecuencia de aparición.
N_colours = colours.shape[0]    # Cantidad de colores de la paleta.
N_colours
colours
counts

# Analicemos cuantos colores de la paleta aparecen solo 1 vez
N1 = np.sum(counts==1)                      # Para el caso de peppers: 79482!
N1p = 100*np.sum(counts==1)/N_colours       # Es decir, un 80% de los colores de la paleta aparecen solo 1 vez.
print(f"{N1} colores de la paleta aparecen solo 1 vez en la imagen ({N1p:5.2f}% del total de colores de la paleta).")

# Analicemos cuantos colores de la paleta hay para cada frecuencia de aparación
c_vals, c_counts = np.unique(counts, return_counts=True)
plt.figure() 
plt.stem(c_vals, c_counts)
plt.title("Colores de la paleta para cada frecuencia de aparación")
plt.xlabel("Frecuencia de aparación en la imagen original")
plt.ylabel("Cantidad de colores")
plt.show(block=False)

# Realizamos el mismo análisis pero en porcentajes
c_counts_p = 100*c_counts/N_colours
plt.figure() 
plt.stem(c_vals, c_counts_p)
plt.title("Colores de la paleta para cada frecuencia de aparación")
plt.xlabel("Frecuencia de aparación en la imagen original")
plt.ylabel("Cantidad de colores [%]")
plt.show(block=False)


# --- Imagen Indexada -------------------------------------------------------------------
img = cv2.imread('peppers.png')         # N_colours= 99.059  --> Nbytes_img_idx/Nbytes_img: uint32 = 1.83  
# img = cv2.imread('home.jpg')            # N_colours= 51.711  --> Nbytes_img_idx/Nbytes_img: uint32 = 1.59 | uint16 = 0.93
# img = cv2.imread('flowers.tif')         # N_colours= 120.260 --> Nbytes_img_idx/Nbytes_img: uint32 = 1.667  # Cuidado! puede demorar mucho en correr...
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
imshow(img, title="Imagen Original")

# Obtengamos su paleta de colores
img_pixels = img.reshape(-1,3)                                      # Re-ordeno los pixels, de manera que cada pixel ocupe una fila.
colours, counts = np.unique(img_pixels, axis=0, return_counts=True) # Obtengo los valores únicos de todos los pixels y su frecuencia de aparición.
idx = np.argsort(counts)        # Solo para mayor facilidad en el análisis...
counts = counts[idx]            # ... ordeno los colores segun su frecuencia de aparición.
colours = colours[idx]          # El ultimo elemento de counts posee el color con mayor frecuencia de aparición.
N_colours = colours.shape[0]    # Cantidad de colores de la paleta.
N_colours
colours
counts

# Genero imagen indexada
img_idx = -np.ones(img.shape[:-1])
for ii in range(N_colours):
    # --- Version legible ---------------------------------------------------------------------
    col_sel = colours[ii]
    maskR = img[:,:,0] == col_sel[0]
    maskG = img[:,:,1] == col_sel[1]
    maskB = img[:,:,2] == col_sel[2]
    mask = maskR & maskG & maskB
    img_idx[mask] = ii
    # --- Version compacta -------------------------------------------------------------------
    # img_idx[(img[:,:,0] == colours[ii][0]) & (img[:,:,1] == colours[ii][1]) & (img[:,:,2] == colours[ii][2])] = ii
    # --- Otra version -------------------------------------------------------------------------
    # mask = cv2.inRange(img, colours[ii], colours[ii])  # https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981
    # img_idx[mask>0] = ii

# Analizo la imagen de índices generada
img_idx.max()
img_idx.min()
np.any(img_idx==-1) # Verificamos que ningún pixel quedó sin asignar...

# Visualizo 
imshow(img_idx, title="Imagen de índices")
plt.figure()    # También podemos utilizar otros mapas de colores.
ax1 = plt.subplot(221); plt.xticks([]), plt.yticks([]), plt.imshow(img), plt.title('Imagen Original'), plt.colorbar()
plt.subplot(222,sharex=ax1,sharey=ax1), plt.imshow(img_idx, cmap="gray"), plt.title('Imagen Indexada - Indices'), plt.colorbar()
plt.subplot(223,sharex=ax1,sharey=ax1), plt.imshow(img_idx, cmap="jet"), plt.title('Imagen Indexada - jet'), plt.colorbar()
plt.subplot(224,sharex=ax1,sharey=ax1), plt.imshow(img_idx, cmap="hot"), plt.title('Imagen Indexada - hot'), plt.colorbar()
plt.show(block=False)

# Analisis de los colores con mayor frecuencia de aparación
P = 5   # Probar con: 5 - 20 - 50 - 80
img_idx_topValues_mask = cv2.inRange(img_idx, (N_colours-1)*(100-P)/100, (N_colours-1))   # Filtro el top P% de colores, en los demás pixels asigna 0
img_idx_topValues = cv2.bitwise_and(img, img, mask= img_idx_topValues_mask)                         # Hacemos un AND de la máscara anterior con la imagen original
# img_idx_topValues = img.copy()                                # Lo mismo que antes...   
# img_idx_topValues[img_idx_topValues_mask<255, :] = 0          # pero de manera "manual".
porc = 100* np.sum(img_idx_topValues_mask>0) / np.prod(img_idx_topValues_mask.shape)                # Obtengo el porcentaje del total de pixels que cumplen esta condición

plt.figure()
ax1 = plt.subplot(221); imshow(img, title="Imagen Original", new_fig=False)
plt.subplot(222,sharex=ax1,sharey=ax1), imshow(img_idx_topValues_mask, title=f'Imagen Indexada - {P:5.2f}% top values - mask', new_fig=False)
plt.subplot(223,sharex=ax1,sharey=ax1), imshow(img_idx_topValues, title=f'Imagen Indexada - top values (%{porc:5.2f})', new_fig=False)
plt.show(block=False)

# Veamos si logramos ahorrar espacio (~comprimir) al pasar de imagen RGB a imagen indexada
# Conversion
img_idx = np.uint32(img_idx)        # Rango: [0 2^32-1] --> [0 4.294.967.295]
# img_idx = np.uint16(img_idx)      # Rango: [0 2^16-1] --> [0 65.535]
img_idx.dtype

# Calculo de relación de bytes
Nbytes_img_idx = 4*np.prod(img_idx.shape) + np.prod(colours.shape)  # uint32: 4 bytes
# Nbytes_img_idx = 2*np.prod(img_idx.shape) + np.prod(colours.shape)  # uint16: 2 bytes
Nbytes_img = np.prod(img.shape)
rel = Nbytes_img_idx/Nbytes_img
print(f"Tamaño imagen RGB:      {Nbytes_img:10} bytes")
print(f"Tamaño imagen indexada: {Nbytes_img_idx:10} bytes")
print(f"Relación: {rel}")
