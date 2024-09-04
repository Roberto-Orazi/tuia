import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Leo imagen --------------------------------------------------
img = cv2.imread('xray-chest.png',cv2.IMREAD_GRAYSCALE)  # https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
# img = cv2.imread('xray-chest.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Info
type(img)
img.dtype
img.shape
w,h = img.shape

# Stats
img.min()
img.max()
pix_vals = np.unique(img)
N_pix_vals = len(np.unique(img))

# --- Muestro imagen -----------------------------------------------
plt.imshow(img, cmap='gray')  # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow
plt.show()                    # https://matplotlib.org/stable/gallery/color/colormap_reference.html

h = plt.imshow(img, cmap='gray', vmin=0, vmax=255) # Cualquier valor fuera del rango se satura.
plt.colorbar(h)
plt.title('Imagen')
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks([])
plt.yticks([])
plt.show()

h = plt.imshow(img, cmap='gray', vmin=0, vmax=10)
plt.colorbar(h)
plt.show()

plt.subplot(121)
h = plt.imshow(img, cmap='gray')
plt.colorbar(h)
plt.title('Imagen - normalizada')
plt.subplot(122)
h = plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.colorbar(h)
plt.title('Imagen - sin normalizar')
plt.show()


# --- Generar imagenes jpeg variando calidad  --------------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
h = plt.imshow(img, cmap='gray')
plt.colorbar(h)
plt.show()

cv2.imwrite("cameraman90.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite("cameraman50.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite("cameraman25.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 25])
cv2.imwrite("cameraman10.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 10])
cv2.imwrite("cameraman05.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 5])

# --- Metricas de error ----------------------------------------------------------------------------
img90 = cv2.imread('cameraman90.jpeg',cv2.IMREAD_GRAYSCALE)
img05 = cv2.imread('cameraman05.jpeg',cv2.IMREAD_GRAYSCALE)
img90_RMSE = np.sqrt(np.sum(np.power(img.astype(float)-img90.astype(float),2))) / np.sqrt(np.size(img))
img05_RMSE = np.sqrt(np.sum(np.power(img.astype(float)-img05.astype(float),2))) / np.sqrt(np.size(img))
img05_RMSE_v2 = np.sqrt(np.mean((img.astype(float) - img05.astype(float)) ** 2))   # Otra forma...
print(f"q =  5 --> RMSE = {img05_RMSE}")
print(f"q = 90 --> RMSE = {img90_RMSE}")

# --- Obtengo info de una imagen ------------------------------------------------------------------
from PIL import Image
from PIL.ExifTags import TAGS
image= Image.open('cameraman.tif')
exifdata= image.getexif()
for tag_id in exifdata:
    tag= TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    print(f"{tag:25}: {data}")

# Cambio valor de dpi 
image.save('cameraman_dpi100.tif', dpi=(100,100))
image = Image.open('cameraman_dpi100.tif')  # Check dpi value:
exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    print(f"{tag:25}: {data}")



# --- Conversion de tipo de dato -----------------------------------------------------------------
# Numpy
x = np.array([1,2,3],dtype="uint8")
x.dtype
x16 = x.astype("int16")
x16.dtype

# Numpy
img.dtype
img.max()
img.min()

img_converted = img.astype("float")
img_converted.dtype
img_converted.min()
img_converted.max()

# OpenCV
print(f"{img.dtype} - max = {img.max()} - min = {img.min()}")

img2 = cv2.convertScaleAbs(img,None,alpha=1,beta=0)
img2 = cv2.convertScaleAbs(img,None,alpha=2,beta=2)
img2 = cv2.convertScaleAbs(img,None,alpha=2,beta=-2)
img2 = cv2.convertScaleAbs(img_converted,None,alpha=2,beta=-2)
print(f"{img2.dtype} - max = {img2.max()} - min = {img2.min()}")


# --- Im2double -------------------------------------------------------------------------------------
def im2double(im):
    info = np.iinfo(im.dtype) 
    return im.astype(np.double) / info.max 

imgd = im2double(img)
imgd.max()
imgd.min()
h = plt.imshow(imgd,cmap='gray')
plt.colorbar(h)
plt.show()

img = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX) # Así no, porque lleva los valores min/max a 0/1
img.min()
img.max()
h = plt.imshow(imgd,cmap='gray')
plt.colorbar(h)
plt.show()

# --- Creo imagen en base a una función ------------------------------
nx, ny = (100, 100)
x = np.linspace(0, 8*np.pi, nx)
y = np.linspace(0, 8*np.pi, ny)
xv, yv = np.meshgrid(x, y)
z = np.sin(1*xv + 1*yv)
# z = np.sin(1*xv + 2*yv)
z.shape

plt.figure()
plt.imshow(z, cmap='gray')
plt.show()