# 📚 RESUMEN DETALLADO: Fundamentos de Computer Vision
*Explicado desde cero para principiantes*

---

## 🎯 ¿Qué es Computer Vision?

**Computer Vision** (Visión por Computadora) es hacer que las computadoras "vean" y entiendan imágenes como lo hacemos
nosotros. Para lograr esto, necesitamos entender cómo las computadoras representan las imágenes.

---

## 1️⃣ CÓMO FUNCIONA EL COLOR EN LAS PANTALLAS

### 👁️ ¿Por qué usamos RGB?

Imagínate que tus ojos tienen **3 tipos de "sensores"** para ver colores:
- Uno para el **ROJO** 🔴
- Uno para el **VERDE** 🟢
- Uno para el **AZUL** 🔵

**¡Esto es exactamente lo que pasa!** Tienes células en tus ojos llamadas **conos** que detectan estos 3 colores
básicos. Tu cerebro mezcla las señales de estos 3 sensores para crear TODOS los colores que puedes ver.

### 📱 ¿Cómo funciona tu pantalla?

Tu pantalla imita a tus ojos. Cada **píxel** (punto diminuto en la pantalla) está hecho de **3 mini-luces**:

```
UN PÍXEL = 🔴 Luz Roja + 🟢 Luz Verde + 🔵 Luz Azul
```

**Ejemplos prácticos:**
- **Blanco**: Las 3 luces al máximo (100% rojo + 100% verde + 100% azul)
- **Negro**: Las 3 luces apagadas (0% + 0% + 0%)
- **Amarillo**: Rojo + Verde al máximo, Azul apagado
- **Magenta**: Rojo + Azul al máximo, Verde apagado

### 🧮 Los números detrás del color

Las computadoras usan números del **0 al 255** para cada color:
- **0** = Apagado completamente
- **255** = Encendido al máximo

**¿Por qué 255?** Porque las computadoras usan **8 bits** para cada color, y 2^8 = 256 opciones (0-255).

**Ejemplo:**
- Rojo puro = (255, 0, 0)
- Verde puro = (0, 255, 0)
- Azul puro = (0, 0, 255)
- Blanco = (255, 255, 255)
- Negro = (0, 0, 0)

**¡Matemática impresionante!** Con 3 canales de 8 bits cada uno:
```
Total de colores posibles = 256 × 256 × 256 = 16,777,216 colores diferentes
```

---

## 2️⃣ COLORES ADITIVOS vs SUSTRACTIVOS

### 🖥️ Aditivos (RGB) - "Sumamos luz"

**¿Dónde se usa?** Pantallas, proyectores, cualquier cosa que EMITA luz.

**¿Cómo funciona?** Empezamos con NEGRO (sin luz) y AGREGAMOS colores:

```
🔴 Rojo + 🟢 Verde = 🟡 Amarillo
🟢 Verde + 🔵 Azul = 🩵 Cian
🔵 Azul + 🔴 Rojo = 🟣 Magenta
🔴 Rojo + 🟢 Verde + 🔵 Azul = ⚪ Blanco
```

### 🖨️ Sustractivos (CMYK) - "Quitamos luz"

**¿Dónde se usa?** Impresoras, pinturas, cualquier cosa que ABSORBE luz.

**¿Cómo funciona?** Empezamos con BLANCO (papel) y QUITAMOS colores:

```
🩵 Cian + 🟣 Magenta = 🔵 Azul
🟣 Magenta + 🟡 Amarillo = 🔴 Rojo
🟡 Amarillo + 🩵 Cian = 🟢 Verde
🩵 Cian + 🟣 Magenta + 🟡 Amarillo + ⚫ Negro = ⚫ Negro
```

**¿Por qué agregan Negro (K)?** Porque mezclar Cian+Magenta+Amarillo da un marrón feo, no negro puro.

---

## 3️⃣ LAS IMÁGENES EN LA COMPUTADORA

### 🧱 ¿Qué es realmente una imagen digital?

Una imagen digital es como un **rompecabezas gigante** donde cada pieza es un píxel. La computadora guarda esto como una
**tabla de números**.

### 📊 Arrays de NumPy - "Tablas de números"

**NumPy** es una librería de Python que maneja tablas de números súper eficientemente.

#### 🔲 Imagen en Escala de Grises (Blanco y Negro)

```python
# Una imagen simple 3x3 en escala de grises
imagen_gris = [
    [0,   128, 255],
    [64,  192, 32 ],
    [255, 0,   128]
]
```

**¿Qué significa esto?**
- Cada número representa qué tan **brillante** es ese píxel
- **0** = Negro total
- **255** = Blanco total
- **128** = Gris medio

**Forma (Shape):** `(3, 3)` = 3 filas × 3 columnas = **1 canal**

#### 🌈 Imagen a Color (RGB)

```python
# El mismo píxel con color tiene 3 números
pixel_rojo = [255, 0, 0]    # [R, G, B]
pixel_verde = [0, 255, 0]
pixel_azul = [0, 0, 255]
```

Para una imagen 3x3 a color:
```python
# Ahora cada posición tiene 3 números
imagen_color = [
    [[255,0,0], [0,255,0], [0,0,255]],      # Fila 1: rojo, verde, azul
    [[255,255,0], [255,0,255], [0,255,255]], # Fila 2: amarillo, magenta, cian
    [[255,255,255], [128,128,128], [0,0,0]]  # Fila 3: blanco, gris, negro
]
```

**Forma (Shape):** `(3, 3, 3)` = 3 filas × 3 columnas × **3 canales**

### 🔄 BGR vs RGB - ¡Cuidado con OpenCV!

**¡SÚPER IMPORTANTE!** OpenCV (librería popular para imágenes) usa **BGR** en lugar de RGB:

```python
# Lo que TÚ piensas (RGB):
pixel_rojo = [255, 0, 0]  # [Rojo, Verde, Azul]

# Lo que OpenCV guarda (BGR):
pixel_rojo = [0, 0, 255]  # [Azul, Verde, Rojo]
```

**¿Por qué?** Por razones históricas. Siempre hay que **convertir** cuando trabajas con OpenCV:

```python
import cv2

# Leer imagen (OpenCV la carga como BGR)
imagen = cv2.imread('mi_foto.jpg')

# Convertir a RGB para mostrar correctamente
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
```

---

## 4️⃣ TRABAJANDO CON IMÁGENES EN PYTHON

### 📥 Cargar una imagen

#### Método 1: OpenCV
```python
import cv2
import numpy as np

# Cargar imagen desde archivo
imagen = cv2.imread('mi_foto.jpg')
# ¡RECUERDA! OpenCV carga en formato BGR

# Ver información de la imagen
print(f"Forma: {imagen.shape}")  # (altura, ancho, canales)
print(f"Tipo: {imagen.dtype}")   # Tipo de números (uint8)
```

#### Método 2: Desde una URL
```python
import requests
import cv2
import numpy as np

def cargar_imagen_web(url):
    # Descargar la imagen
    respuesta = requests.get(url)

    # Convertir bytes descargados a array
    bytes_imagen = np.array(bytearray(respuesta.content), dtype=np.uint8)

    # Decodificar (de JPG/PNG a array NumPy)
    imagen = cv2.imdecode(bytes_imagen, cv2.IMREAD_COLOR)

    return imagen

# Usar la función
mi_imagen = cargar_imagen_web('https://ejemplo.com/foto.jpg')
```

### 🔍 Inspeccionar una imagen

```python
import matplotlib.pyplot as plt

# Convertir BGR a RGB (para mostrar correctamente)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Información básica
print(f"Dimensiones: {imagen_rgb.shape}")
print(f"Alto: {imagen_rgb.shape[0]} píxeles")
print(f"Ancho: {imagen_rgb.shape[1]} píxeles")
print(f"Canales: {imagen_rgb.shape[2]}")
print(f"Tipo de dato: {imagen_rgb.dtype}")

# Mostrar la imagen
plt.imshow(imagen_rgb)
plt.title("Mi imagen")
plt.show()
```

### 🎨 Separar canales de color

```python
# Separar los 3 canales
canal_rojo = imagen_rgb[:, :, 0]    # Solo el canal rojo
canal_verde = imagen_rgb[:, :, 1]   # Solo el canal verde
canal_azul = imagen_rgb[:, :, 2]    # Solo el canal azul

# Mostrar cada canal por separado
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(canal_rojo, cmap='Reds')
axes[0].set_title('Canal Rojo')

axes[1].imshow(canal_verde, cmap='Greens')
axes[1].set_title('Canal Verde')

axes[2].imshow(canal_azul, cmap='Blues')
axes[2].set_title('Canal Azul')

plt.show()
```

---

## 5️⃣ CONVERSIÓN A ESCALA DE GRISES

### 🤔 ¿Por qué convertir a escala de grises?

1. **Simplicidad:** 3 canales → 1 canal = menos datos
2. **Velocidad:** Procesamiento 3 veces más rápido
3. **Algoritmos:** Muchos algoritmos trabajan mejor sin color
4. **Memoria:** Ocupa menos espacio

### 🧠 ¿Cómo funciona la conversión?

**¡No es un simple promedio!** Nuestros ojos son más sensibles a algunos colores:

```
👁️ Sensibilidad del ojo humano:
🟢 Verde: 58.7% (¡El que más vemos!)
🔴 Rojo: 29.9%
🔵 Azul: 11.4% (¡El que menos vemos!)
```

### 📐 La fórmula mágica

```
Gris = 0.299×Rojo + 0.587×Verde + 0.114×Azul
```

**¿Por qué estos números?** Porque así percibe tu ojo la luminosidad (brillo) de cada color.

### 💻 Implementación práctica

#### Método Fácil (OpenCV):
```python
# Convertir directamente
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Mostrar resultado
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title("Original (Color)")

plt.subplot(1, 2, 2)
plt.imshow(imagen_gris, cmap='gray')
plt.title("Escala de Grises")

plt.show()
```

#### Método Manual (Para entender):
```python
def convertir_a_gris(imagen_rgb):
    # Convertir a números decimales
    imagen_float = imagen_rgb.astype(np.float32)

    # Aplicar la fórmula: 0.299*R + 0.587*G + 0.114*B
    pesos = [0.299, 0.587, 0.114]
    imagen_gris = np.dot(imagen_float, pesos)

    # Asegurar que esté entre 0 y 255
    imagen_gris = np.clip(imagen_gris, 0, 255)

    # Convertir de vuelta a enteros
    return imagen_gris.astype(np.uint8)

# Usar nuestra función
mi_imagen_gris = convertir_a_gris(imagen_rgb)
```

### 🔬 ¿Qué hace np.dot()?

```python
# Ejemplo simple
pixel_color = [100, 150, 50]  # [R, G, B]
pesos = [0.299, 0.587, 0.114]

# np.dot calcula:
resultado = 100*0.299 + 150*0.587 + 50*0.114
resultado = 29.9 + 88.05 + 5.7 = 123.65

# Redondeado = 124 (valor en escala de grises)
```

---

## 6️⃣ DIFERENCIAS ENTRE LIBRERÍAS

### 🔧 OpenCV
```python
import cv2

# ✅ Ventajas:
# - Súper rápido
# - Muchas funciones de procesamiento
# - Ideal para video en tiempo real

# ⚠️ Desventajas:
# - Usa BGR (no RGB)
# - Sintaxis a veces confusa

imagen = cv2.imread('foto.jpg')  # Carga como BGR
```

### 🖼️ Pillow (PIL)
```python
from PIL import Image

# ✅ Ventajas:
# - Fácil de usar
# - Usa RGB (como esperamos)
# - Bueno para operaciones simples

imagen = Image.open('foto.jpg')  # Carga como RGB
imagen_array = np.array(imagen)  # Convertir a NumPy
```

### 📊 Matplotlib
```python
import matplotlib.pyplot as plt

# ✅ Ventajas:
# - Excelente para mostrar imágenes
# - Integrado con NumPy
# - Gráficos científicos

plt.imshow(imagen)  # Espera formato RGB
plt.show()
```

---

## 7️⃣ CONCEPTOS CLAVE PARA RECORDAR

### 🎯 Resumen de Formatos

| Tipo | Dimensiones | Descripción | Ejemplo |
|------|-------------|-------------|---------|
| **Escala de Grises** | `(alto, ancho)` | 2D, 1 canal | `(480, 640)` |
| **Color RGB** | `(alto, ancho, 3)` | 3D, 3 canales | `(480, 640, 3)` |

### 🔄 Conversiones Importantes

```python
# BGR → RGB (OpenCV → Matplotlib)
imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

# Color → Escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Pillow → NumPy
imagen_array = np.array(imagen_pil)
```

### ⚠️ Errores Comunes

1. **Olvidar convertir BGR a RGB**
   ```python
   # ❌ Colores raros
   plt.imshow(imagen_opencv)

   # ✅ Colores correctos
   plt.imshow(cv2.cvtColor(imagen_opencv, cv2.COLOR_BGR2RGB))
   ```

2. **No usar cmap='gray' para imágenes en escala de grises**
   ```python
   # ❌ Se ve raro (con colores falsos)
   plt.imshow(imagen_gris)

   # ✅ Se ve bien (en grises)
   plt.imshow(imagen_gris, cmap='gray')
   ```

3. **Confundir las dimensiones**
   ```python
   # Para una imagen 640x480 en color:
   print(imagen.shape)  # (480, 640, 3)
   #                     ↑     ↑     ↑
   #                   alto ancho canales
   ```

---

## 🚀 PRÓXIMOS PASOS

Una vez que domines estos conceptos básicos, podrás avanzar a:

1. **Filtros y transformaciones**
2. **Detección de bordes**
3. **Reconocimiento de objetos**
4. **Deep Learning para imágenes**

---

## 🔗 RECURSOS ÚTILES

- **Google Colab con ejemplos:**
  [https://colab.research.google.com/drive/1xa35-nCPbyJU0hAx](https://colab.research.google.com/drive/1xa35-nCPbyJU0hAx)
- **Herramienta interactiva RGB:** [http://www.cknuckles.com/rgbsliders.html](http://www.cknuckles.com/rgbsliders.html)

---

**¡Felicidades! 🎉** Ahora entiendes los fundamentos de cómo las computadoras "ven" las imágenes. Estos conceptos son la
base de todo el Computer Vision moderno.