import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
Problema "Letras" 

Dada la imagen 'letras.png', la cual contiene letras en diferentes renglones, se pretende generar una imagen de salida
que resalte cada letra mediante un rectángulo de color (Caja contenedora o Bounding Box).
"""

# --- Cargo imagen ------------------------------------------------------------
img = cv2.imread('letras.png',cv2.IMREAD_GRAYSCALE) 
img.shape
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False)                    

"""
Para lograr lo pedido, se deben encontrar las filas y columnas donde empieza y termina cada letra. Para ello,
dividiremos el problema en 2 partes:
    1) Detectaremos cada renglón del texto.  
       Debemos encontrar las filas donde empieza y termina cada renglón.
    2) Analizaremos cada renglón por separado, detectando donde empieza y termina cada letra. Debemos encontrar las
       columnas donde empieza y termina cada letra.
"""

# -----------------------------------------------------------------------------
# --- PARTE 1: Detección de renglones -----------------------------------------
# -----------------------------------------------------------------------------
"""
Para encontrar donde empieza y termina cada renglón, analizaremos las filas de la imagen. Crearemoms un vector de la
misma longitud que la cantidad de filas de la imagen. La idea consiste en analizar cada fila y asignar un valor TRUE a
la posición correspondiente de dicho vector si en dicha fila existe aunque sea un pixel perteneciente a una letra. Caso
contrario, se le asigna FALSE.

Dado que el fondo es blanco (~255) y las letras son negras (~0), se asignará TRUE si aunque sea un pixel de la misma es
negro.
"""

# ****************************************************************************************************
# *** EJEMPLO: Búsqueda de columnas y filas con elementos != 0 ***************************************
# ****************************************************************************************************
a = np.array([[0,1,0],
              [0,0,0],
              [0,1,1],
              [0,1,0]])

# Busco columnas que poseen algún valor distinto de cero --> ic = [1 2]
a.any(axis=0)               # any() devuelve TRUE si aunque sea un elemento es != 0. 
np.argwhere(a.any(axis=0))  # argwhere() devuelve los índices del vector de entrada donde el valor es TRUE.
                            # --> Prestar especial atención al tamañao (.shape) del valor de salida de argwhere(): 2x1.

# Busco filas que poseen algún valor distinto de cero   --> ir = [0 2 3]
a.any(axis=1)               
np.argwhere(a.any(axis=1))

# Mismos ejemplos que antes, pero buscando algún valor particular
VAL = 0                         # Busco filas y columnas que tengan algún valor igual a VAL
b = a==VAL                      # Genero matriz booleana con TRUE donde se encuentre el valor VAL y FALSE donde no.

# Analizo Filas --> ir = [0 1 2 3]
b.any(axis=1)                                 
np.argwhere(b.any(axis=1))

# Analizo Columnas  --> ic = [0 1 2]
b.any(axis=0)                                 
np.argwhere(b.any(axis=0))
# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************

# Acondicionamiento de la imagen
img_zeros = img==0                              # Por simplicidad, genero una matriz booleana con TRUE donde supongo que hay letras (pixel = 0)
plt.figure(), plt.imshow(img_zeros, cmap='gray'), plt.show()

# Analizo filas
img_row_zeros = img_zeros.any(axis=1)
img_row_zeros_idxs = np.argwhere(img_zeros.any(axis=1))
plt.figure(), plt.plot(img_row_zeros), plt.show()   # Visualizamos el vector booleano que indica con TRUE (1) donde "está" el regnlón.

# Generamos una figura donde se muestra la imagen original superponiendo la gráfica anterior pero rotada y escalada.
xr = img_row_zeros*(img.shape[1]-1)     # Generamos valores en el eje x (el eje que apunta hacia la derecha) --> dos posibles valores: 0 o el ancho de la imagen (cantidad de columnas de la imagen -1).
yr = np.arange(img.shape[0])            # Generamos valores en el eje y (el eje que apunta hacia abajo) --> Vector que arranca en 0, aumenta de a 1 y llega hasta la cantidad de filas de la imagen [0, 1, ..., N_filas-1]
plt.figure(), plt.imshow(img, cmap='gray'), plt.plot(xr, yr, c='r'), plt.title("Renglones"), plt.show(block=False)                    

"""
Hasta aquí, generamos un vector (img_row_zeros) que posee valores TRUE donde se encuentra el renglón. Es decir, tenemos
una señal del tipo "pulsos", donde los pulsos son los renglones:

================================================================
F F F F F T T T T F F F F F F T T T T F F F F F F  ...
         --------             -------             
--------|        |-----------|       |-----------  ...
            R1                   R2
        <        >           <       > i1       f1          i2      f2
================================================================
        
F: False T: True 

R1: Renglón 1 i1: Inicio del renglón 1 f1: Fin del renglón 1

R2: Renglón 2 i2: Inicio del renglón 2 f2: Fin del renglón 2

Ahora quisieramos obtener cuales son las filas donde EMPIEZA y TERMINA dicho renglón: i1, f1, i2, f2, etc. Veamos un
ejemplo simple y luego lo aplicamos al problema de los renglones...
"""

# ****************************************************************************************************
# *** EJEMPLO: Encontrar inicio/fin de pulsos ********************************************************
# ****************************************************************************************************
a = np.array([False,False,True,True,True,False,False])  # El resultado debería ser [2, 4]
ad = np.diff(a)         # Calcula la diferencia entre los elementos contiguos del vector de entrada:
                        #  ad[0] = a[1] - a[0]  
                        #  ad[1] = a[2] - a[1] ... En este caso, el resultado es: [False, True, False, False, True,
                        #   False]
ind = np.argwhere(ad)   # Luego encuentro los índices donde se da TRUE. En este caso: [1,4]  
                        #   --> Puede verse que el inicio no coincide (vale 1 menos), por lo cual lo ajustamos
                        #       manualmente (sumamos 1).
ind[0] += 1             # Modifico el indice inicial para que coincida con el resultado esperado --> [2 4]
# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************

# Encontramos inicio y final de cada renglón
"""
Utilizando el ejemplo anterior, encontramos el inicio y final de cada renglón
"""
x = np.diff(img_row_zeros)          
renglones_indxs = np.argwhere(x)    # Esta variable contendrá todos los inicios y finales de los renglones
len(renglones_indxs)                # Como son 4 renglones, tendrá 8 elementos: 4 renglones x 2 (ini/fin)

# Modifico índices de inicio
"""
Ahora debo modificar todos los inicios (ver ejemplo). El vector renglones_indxs esta formado de la siguiente manera:
[ini_R1  fin_R1  ini_R2  fin_R2  ...] Como puede observarse, los inicios están en los índices: 0, 2, 4, etc. Por lo
tanto, genero un vector con dichos valores para indexar renglones_indxs y sumar 1.
"""
ii = np.arange(0,len(renglones_indxs),2)    # 0 2 4 ... X --> X es el último nro par antes de len(renglones_indxs)
renglones_indxs[ii]+=1

# Visualizo
xri = np.zeros(img.shape[0])
xri[renglones_indxs] = (img.shape[1]-1)
yri = np.arange(img.shape[0])            
plt.figure(), plt.imshow(img, cmap='gray'), plt.plot(xri, yri, 'r'), plt.title("Renglones - Inicio y Fin"), plt.show(block=False)                    

# Recortamos cada renglón y guardamos información del mismo
"""
Generamos una estructura de datos para los renglones. Definiremos un diccionario para cada renglón, el cual contendrá la
siguiente información:
    * índice del renglón.
    * índices de las filas del inicio y final.
    * sub-imagen que contiene solo el renglón.
Guardamos todos los diccionarios en una lista.
"""

# Acondicionamiento de los índices de inicio/fin.
r_idxs = np.reshape(renglones_indxs, (-1,2))  # Re-ordeno los índices en grupos de a 2 (inicio-final)
                                              # De esta manera, cada fila de r_idxs contiene el inicio y final de cada
                                              # renglón.

# Genero estructura de datos
renglones = []
for ir, idxs in enumerate(r_idxs):
    renglones.append({
        "ir": ir+1,
        "cord": idxs,
        "img": img[idxs[0]:idxs[1], :]
    })

# Visualizo
"""
Generamos una figura con un subplot por cada renglón.
"""
plt.figure()
for renglon in renglones:
    plt.subplot(2, 2, renglon["ir"])
    plt.imshow(renglon["img"], cmap='gray')
    plt.title(f"Renglón {renglon['ir']}")
plt.suptitle("RENGLONES")
plt.show(block=False)      


# -----------------------------------------------------------------------------
# --- PARTE 2: Detección de letras en cada renglón ----------------------------
# -----------------------------------------------------------------------------
"""
Ahora, analizaremos cada renglón por separado, es decir, como si fueran imágenes independientes. Generamos un bucle for
que itere sobre la estructura de datos de los renglones, y para cada sub-imagen del renglón bajo análisis, realizamos lo
siguiente:

    a) ACONDICIONAMIENTO
        Al igual que para el paso anterior, por simplicidad, genero una matriz booleana con TRUE donde supongo que hay
        letras (pixel = 0)

    b) DETECCIÓN INICIO-FIN DE LETRA
        Utilizando la misma metodología que para el caso de detección de renglones, ahora detectaremos el inicio y fin
        de cada letra. Para ello, como sabemos que cada sub-imagen contiene 1 solo renglón, analizamos las columnas.
        Crearemoms un vector de la misma longitud que la cantidad de columnas de la sub-imagen. La idea consiste en
        analizar cada columna y asignar un valor TRUE a la posición correspondiente de dicho vector si en dicha columna
        existe aunque sea un pixel perteneciente a una letra. Caso contrario, se le asigna FALSE.
    
    c) ESRTRUCTURA DE DATOS 
        Generamos una estructura de datos para las letras. Definiremos un diccionario para cada letra, el cual contendrá
        la siguiente información:
            * índice del renglón (ir).
            * índice de la letra dentro del renglón (irl).
            * índice de la letra en toda la imagen (il).
            * índices de las filas y columnas del inicio y fin de la letra en la imagen original.
            * sub-imagen que contiene solo la letra.
        Guardamos todos los diccionarios en una lista.
        
"""

# --- Analizo en renglones -----------------------------------------------------
letras = []
il = -1
for ir, renglon in enumerate(renglones):
    # --- a) ACONDICIONAMIENTO --------------------------------------
    renglon_zeros = renglon["img"]==0  # Acondiciono imagen...

    # --- b) DETECCIÓN INICIO-FIN DE LETRA -------------------------- Analizo columnas del renglón 
    ren_col_zeros = renglon_zeros.any(axis=0)
    ren_col_zeros_idxs = np.argwhere(renglon_zeros.any(axis=0))
    # Visualizo
    xc = np.arange(renglon_zeros.shape[1])
    yc = ren_col_zeros*(renglon_zeros.shape[0]-1)
    plt.figure(), plt.imshow(renglon_zeros, cmap='gray'), plt.plot(xc, yc, c='b'), plt.title(f"Renglón {ir+1}"), plt.show()        
        
    # Encontramos inicio y final de cada letra
    x = np.diff(ren_col_zeros)
    letras_indxs = np.argwhere(x) 
    # *** Modifico índices ***********
    ii = np.arange(0,len(letras_indxs),2)
    letras_indxs[ii]+=1
    # ********************************

    # Re-ordeno los índices en grupos de a 2 (inicio-final)
    letras_indxs = letras_indxs.reshape((-1,2))     # De esta manera, cada fila de letras_indxs contiene el inicio y final de cada letra.
   
    # Visualizo
    Nrows = letras_indxs.shape[0]
    plt.figure(), plt.suptitle(f"Renglón {ir+1}")
    for ii, idxs in enumerate(letras_indxs):
        letra = renglon["img"][: , idxs[0]:idxs[1]]
        plt.subplot(Nrows, 4, ii+1), plt.imshow(letra, cmap='gray'), plt.title(f"letra {ii+1}")
    plt.show()
    
    # --- c) ESRTRUCTURA DE DATOS ---------------------------------------------
    for irl, idxs in enumerate(letras_indxs):
        il+=1
        letras.append({
            "ir":ir+1,
            "irl":irl+1,
            "il": il,
            "cord": [renglon["cord"][0], idxs[0], renglon["cord"][1], idxs[1]],
            "img": renglon["img"][:, idxs[0]:idxs[1]]
        })

# --- Imagen final -----------------------------------------------------------
"""
Genero una figura con la imagen original y un recuadro (bounding-box) para cada letra.
"""
from matplotlib.patches import Rectangle        # Matplotlib posee un módulo para dibujar rectángulos (https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html)
plt.figure(), plt.imshow(img, cmap='gray')
for il, letra in enumerate(letras):
    yi = letra["cord"][0]                       # Rectangle() toma como entrada
    xi = letra["cord"][1]                       # las coordenadas (x,y) de la esquina superior izquierda, 
    W = letra["cord"][2] -letra["cord"][0]      # el ancho y el alto.
    H = letra["cord"][3] -letra["cord"][1]      #
    rect = Rectangle((xi,yi), H, W, linewidth=1, edgecolor='r', facecolor='none')    # Creamos el objeto rectángulo.
    ax = plt.gca()          # Obtengo el identificador de los ejes de la figura (handle)...
    ax.add_patch(rect)      # ... Agrego el objeto (patch) a los ejes.

plt.show()

# --- ANÁLISIS --------------------------------------------------------------
print(len(letras))
"""
Como pueden observar, se encontraron 27 letras en vez de 26:
    ¿Donde está el error? ¿Como pueden solucionarlo?

Hacer esto como tarea... AYUDA: Hay muchas formas de solucionarlo, cambiando un única linea ya se puede solucionar.

Se propone además, realizar las siguientes mejoras:

1) Como puede observarse, el alto del bounding-box de cada letra no siempre coincide con el alto real de cada letra.
   Generar/modificar el código para lograr que el alto del bounding-box coincida con el alto de la letra.

2) Generar una carpeta de salida "letras" y guardar en la misma, una imagen por cada letra, cuyo nombre sea el índice de
   la letra en toda la imagen (il). Todas los nombres de archivos deberán tener la misma cantidad de caracteres, es
   decir: 01.png, 02.png, ..., 26.png.

3) Normalizar el tamaño de todas las letras, de manera tal que todas sean del mismo tamaño. Adoptar como tamaño de
   normalización, el tamaño de la letra más grande. Para lograr dicha normalización, generar una matriz de ceros de
   dicho tamaño y luego insertar la letra en la misma de manera centrada. Por último, generar otra carpeta de salida
   "letras_norm" y guardar en la misma un archivo por cada letra, con el siguiente formato de nombre: 01n.png, 02n.png,
   ... , 26n.png, 
"""
