import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny(img, th1=15, th2=100, debug=False):
    G, theta, theta_deg = gradient(img, debug=debug)    # Obtención del gradiente (magnitud y ángulo)
    Z = non_max_suppression(G, theta)                   # Supresión de no-máximos
    Z_th, v_weak, v_strong = threshold(Z, th1, th2)     # Umbralado
    out = hysteresis(Z_th, v_weak, v_strong)            # Conectividad entre bordes débiles y fuertes

    if debug:
        # *** Gradiente & Supresión de no-máximos ***************************************
        theta_deg2 = theta_deg.copy()       # Matriz de direcciones, solo ángulos positivos...
        theta_deg2[theta_deg2<0] += 180     # Ejemplo: ang = -45º --> dir = 135

        plt.figure(), plt.suptitle("Gradiente")
        ax1=plt.subplot(221); plt.imshow(img, cmap="gray"), plt.colorbar(), plt.title("Imagen")
        plt.subplot(222, sharex=ax1, sharey=ax1); plt.imshow(G, cmap="gray"), plt.colorbar(), plt.title("Gradiente")
        plt.subplot(223, sharex=ax1, sharey=ax1); plt.imshow(theta_deg, cmap="gray"), plt.colorbar(), plt.title("Angulo [grados]")
        plt.subplot(224, sharex=ax1, sharey=ax1); plt.imshow(theta_deg2, cmap="gray"), plt.colorbar(), plt.title("Dirección [grados]")
        plt.show(block=False)   
        
        plt.figure()
        ax1 = plt.subplot(221); plt.imshow(img, cmap="gray"), plt.colorbar(), plt.title("Imagen")
        plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(G, cmap="gray"), plt.colorbar(), plt.title("Gradiente")
        plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(theta_deg2, cmap="gray"), plt.colorbar(), plt.title("Dirección [grados]")
        plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(Z, cmap="gray"), plt.colorbar(), plt.title("Supresión de no-máximos")
        plt.show(block=False)
        # *******************************************************************************

        # *** Supresión de no-máximos & Umbralado & Histeresis **************************
        plt.figure()
        ax1 = plt.subplot(221); plt.imshow(img, cmap="gray"), plt.colorbar(), plt.title("Imagen")
        plt.subplot(222, sharex=ax1, sharey=ax1), plt.imshow(Z, cmap="gray"), plt.colorbar(), plt.title("Supresión de no-máximos")
        plt.subplot(223, sharex=ax1, sharey=ax1), plt.imshow(Z_th, cmap="gray"), plt.colorbar(), plt.title("Doble umbralado")
        plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(out, cmap="gray"), plt.colorbar(), plt.title("Resultado Canny")
        plt.show(block=False)
        # *******************************************************************************

    return out


def gradient(img, k=3, debug=False):
    grad_x = cv2.Sobel(img, cv2.CV_16SC1, 1, 0, ksize=k)  # Variaciones en dirección horizontal
    grad_y = cv2.Sobel(img, cv2.CV_16SC1, 0, 1, ksize=k)  # Variaciones en dirección vertical
    G = np.hypot(grad_x, grad_y)            # Magnitud  (idem a: np.sqrt(grad_x**2 + grad_y**2) )
    G = G / G.max() * 255                   # Normalizo rango: [0, max] --> [0, 255]
    theta = np.arctan2(grad_y, grad_x)      # Dirección [radianes]
    theta_deg = theta * 180. / np.pi        # Convierto a grados
    
    if debug:
        # *** Debug *******************************************
        plt.figure(), plt.suptitle("Gradiente")
        ax1=plt.subplot(221); plt.imshow(img, cmap="gray"), plt.colorbar(), plt.title("Imagen")
        plt.subplot(222, sharex=ax1, sharey=ax1); plt.imshow(G, cmap="gray"), plt.colorbar(), plt.title("Gradiente")
        plt.subplot(223, sharex=ax1, sharey=ax1); plt.imshow(cv2.convertScaleAbs(grad_x), cmap="gray"), plt.colorbar(), plt.title("grad_x")
        plt.subplot(224, sharex=ax1, sharey=ax1), plt.imshow(cv2.convertScaleAbs(grad_y), cmap="gray"), plt.colorbar(), plt.title("grad_y")
        plt.show(block=False)
        # *****************************************************
    
    return G, theta, theta_deg


def non_max_suppression(img, D):
    # --- Inicializo imagen de salida ---------------------------------
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.uint8)

    # --- Convierto de radianes a grados ------------------------------
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    # --- Proceso -----------------------------------------------------
    for i in range(1,M-1):
        for j in range(1,N-1):
                # --- Obtengo valores en la dirección del gradiente ---------------------
                # Dirección 1:   0 grados 
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                # Dirección 2:  45 grados 
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]
                # Dirección 3:  90 grados 
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                # Dirección 4: 135 grados 
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]

                # --- Analizo valores en al dirección del gradiente ---------------------
                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]       # Mantengo el valor si es el mayor, sino queda en 0.

    return Z


def threshold(img, th_low=10, th_high=100):
    v_weak, v_strong = 25, 255          # Defino valores para representar bordes debiles y fuertes
    img_th = v_weak*np.ones_like(img)   # Inicializo todos los pixels como debiles
    img_th[img >= th_high] = v_strong   # Pixels con valor mayor/igual a th_high --> borde fuerte
    img_th[img < th_low] = 0            # Pixels con valor menor a th_low        --> borde debil
    
    return img_th, v_weak, v_strong


def hysteresis(img_orig, weak, strong):
    img = img_orig.copy()               # Inicializo la imagen de salida
    M, N = img.shape  
    for i in range(1, M-1):             # Recorro toda...
        for j in range(1, N-1):         # ...la imagen
            if (img[i,j] == weak):      # Si encuentro un pixel que es borde débil, analizo sus vecinos.
                if ((img[i+1, j-1] == strong) or (img[i+1,   j] == strong) or (img[i+1, j+1] == strong) or 
                    (img[  i, j-1] == strong) or (img[  i, j+1] == strong) or 
                    (img[i-1, j-1] == strong) or (img[i-1,   j] == strong) or (img[i-1, j+1] == strong)):
                    img[i, j] = strong  # Si alguno de sus 8 vecinos es un borde fuerte --> Se convierte en borde.
                else:
                    img[i, j] = 0       # Caso contrario, no es borde.
    return img


