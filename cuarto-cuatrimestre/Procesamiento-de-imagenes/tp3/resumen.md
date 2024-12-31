Conceptos Clave

1. Máscaras (Masks):

Una máscara es una matriz binaria (con valores 0 o 255 generalmente) que se utiliza para seleccionar ciertas áreas de
una imagen. Las áreas con valor 255 (blanco) representan las regiones activas que serán procesadas, mientras que las
áreas con valor 0 (negro) no se procesarán.

2. Marcadores (Markers):

Los marcadores son imágenes iniciales utilizadas como semillas para una operación morfológica, como la reconstrucción.
Representan el estado inicial desde donde se va a propagar una operación, como dilatación o erosión.

3. Kernels:

Un kernel es una matriz pequeña, usualmente de tamaños como 3x3 o 5x5, que define la forma y tamaño de la vecindad
utilizada en operaciones morfológicas como dilatación, erosión, o convolución. Por ejemplo:

kernel = np.ones((3, 3), np.uint8)

Este es un kernel cuadrado de 3x3 con todos los valores establecidos en 1.

4. Dilatación:

La dilatación agranda las regiones blancas en una imagen binaria. Utiliza un kernel para “expandir” los píxeles blancos
alrededor de los bordes. Es útil para cerrar huecos pequeños o unir componentes cercanos.

5. Operaciones Bitwise:

Las operaciones bitwise (AND, OR, XOR, NOT) son combinaciones de bits entre dos imágenes o una imagen y una máscara.
Ejemplo:

	•	cv2.bitwise_and(img1, img2): Mantiene solo los píxeles donde ambas imágenes tienen valores distintos de cero.

6. Reconstrucción Morfológica:

Este proceso utiliza un marcador inicial y una máscara para expandir el marcador (generalmente mediante dilatación)
mientras se asegura de que la expansión no exceda los límites definidos por la máscara.

Explicación del Código

1. imfillhole

Rellena los huecos en una imagen binaria.

	•	Pasos:

	    1.	Crear una máscara inicial (mask) con bordes definidos.

	    2.	Calcular el complemento de la imagen y de los bordes (cv2.bitwise_not).

	    3.	Usar la reconstrucción morfológica (imreconstruct) para rellenar los huecos.

	    4.	Calcular el complemento de la reconstrucción para obtener la imagen rellena.

2. Reconstrucción Morfológica (imreconstruct)

	•	Entrada:

	    •	marker: Imagen inicial (marcador).

	    •	mask: Imagen que define los límites de la expansión.

	•	Proceso:

        •	Expandir el marcador con una dilatación (cv2.dilate).

        •	Limitar la expansión con una operación bitwise AND entre la dilatación y la máscara.

        •	Repetir hasta que la imagen no cambie (convergencia).

3. Procesamiento de la Imagen

En el método procesar_imagenes, se realizan varios pasos:

	1.	Preprocesamiento:

	    •	Convertir a escala de grises (cv2.cvtColor).

	    •	Detectar bordes (cv2.Canny).

	    •	Dilatar bordes para engrosarlos (cv2.dilate).

	    •	Rellenar huecos en los bordes (imfillhole).

	    •	Erosionar para reducir pequeños artefactos.

	2.	Cálculo de Bounding Boxes:

	    •	Encontrar componentes conectados (cv2.connectedComponentsWithStats).

	    •	Filtrar componentes por tamaño y proporciones.

	3.	Detección de Círculos en Dados:

	    •	Aplicar Canny para bordes específicos de círculos.

	    •	Usar connectedComponents para detectar posibles círculos.

Agregar Imágenes

Voy a actualizar el código para mostrar imágenes clave:
```python
def procesar_imagenes(num_foto, frame, num_foto_centroides_dados=[]):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Detección de bordes
    canny = cv2.Canny(img_gray, 50, 75)
    imshow(canny, title="Canny: Bordes Detectados")

    # Dilatación
    engrosar_bordes_generales = cv2.dilate(canny, np.ones((17, 17), np.uint8))
    imshow(engrosar_bordes_generales, title="Bordes Engrosados (Dilatación)")

    # Relleno de huecos
    relleno_dados = imfillhole(engrosar_bordes_generales)
    imshow(relleno_dados, title="Huecos Rellenos")

    # Erosión
    erocion_dado = cv2.erode(relleno_dados, np.ones((3, 3), np.uint8))
    imshow(erocion_dado, title="Imagen Erosionada")

    # Componentes Conectados
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(erocion_dado)
    imshow(labels, title="Componentes Conectados", color_img=True)

    # Resultado final
    terminada = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    return terminada, num_foto_centroides_dados
```

Resultados Visuales

Cuando ejecutes el código, se mostrarán imágenes de cada paso:

	1.	Canny: Visualiza bordes detectados.

	2.	Dilatación: Bordes engrosados para unir componentes cercanos.

	3.	Relleno: Imagen con huecos rellenados.

	4.	Erosión: Reducción de artefactos pequeños.

	5.	Componentes Conectados: Visualización de áreas detectadas como dados.

