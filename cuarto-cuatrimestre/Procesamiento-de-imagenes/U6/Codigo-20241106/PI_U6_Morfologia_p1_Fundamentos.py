import cv2
import numpy as np
import matplotlib.pyplot as plt


# Defininimos función para mostrar imágenes
def imshow(
    img,
    new_fig=True,
    title=None,
    color_img=False,
    blocking=False,
    colorbar=False,
    ticks=False,
):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap="gray")
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:
        plt.show(block=blocking)


# -----------------------------------------------------------------------------
# --- Operaciones básicas de conjuntos ----------------------------------------
# -----------------------------------------------------------------------------
A = cv2.imread("UTK.tif", cv2.IMREAD_GRAYSCALE)
B = cv2.imread("GT.tif", cv2.IMREAD_GRAYSCALE)
print(A.dtype)
print(np.unique(A))
print(B.dtype)
print(np.unique(B))

imshow(A, "A")
imshow(B, "B")

# --- Complemento -------------------------------
Ac = 255 - A
Ac = cv2.bitwise_not(A)
imshow(Ac, "Ac", title="Complemento de A")

# --- Union -------------------------------------
AuB = np.zeros_like(A)
AuB[np.logical_or(A, B)] = 255
# AuB = np.uint8(255*np.logical_or(A,B))  # Otra opción (ojo con el tipo de dato).
print(AuB.dtype)
imshow(AuB, "AuB", title="Union")

# --- Interseccion ------------------------------
AiB = np.zeros_like(A)
AiB[np.logical_and(A, B)] = 255
# AiB = 255*np.logical_and(A,B)  # Otra opción (ojo con el tipo de dato).
print(AiB.dtype)
imshow(AiB, "AiB", title="Interseccion")

# --- Resta -------------------------------------
AmB = A.copy()
AmB[B > 0] = 0

# AmB = np.zeros_like(A)                # Otra Opcion AmB[np.logical_and(A, 255-B)] = 255   #

# AmB = 255*np.logical_and(A, 255-B)   # Otra opción (ojo con el tipo de dato).

print(AmB.dtype)
imshow(AmB, "AmB", "Resta (A - B)")

plt.close("all")

# -----------------------------------------------------------------------------
# --- Operaciones morfológicas ------------------------------------------------
# -----------------------------------------------------------------------------
# --- Dilatacion (Dilate) -----------------------
F = cv2.imread("broken_text.tif", cv2.IMREAD_GRAYSCALE)
imshow(F, title="Imagen Original")

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
Fd = cv2.dilate(F, kernel, iterations=1)

plt.figure()
ax1 = plt.subplot(121)
imshow(F, new_fig=False, title="Original")
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(Fd, new_fig=False, title="Dilatacion")
plt.show(block=False)

# --- Erosion (Erode) ---------------------------
F = cv2.imread("wirebond_mask.tif", cv2.IMREAD_GRAYSCALE)
imshow(F, title="Imagen Original")

L = 10  # Probar con 10 - 30 - 70
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (L, L))
Fe = cv2.erode(F, kernel, iterations=1)

plt.figure()
ax1 = plt.subplot(121)
imshow(F, new_fig=False, title="Original")
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(Fe, new_fig=False, title="Erosion")
plt.show(block=False)

# --- Apertura (Opening) ------------------------
A = cv2.imread("shapes.tif", cv2.IMREAD_GRAYSCALE)
imshow(A, title="Imagen Original")

B = cv2.getStructuringElement(cv2.MORPH_RECT, (37, 37))
# B = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
Aop = cv2.morphologyEx(
    A, cv2.MORPH_OPEN, B
)  # https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html

plt.figure()
ax1 = plt.subplot(121)
imshow(A, new_fig=False, title="Original")
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(Aop, new_fig=False, title="Apertura")
plt.show(block=False)

# ---- Clausura (Closing) -----------------------
A = cv2.imread("shapes.tif")
imshow(A, title="Imagen Original")

B = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
Aclau = cv2.morphologyEx(A, cv2.MORPH_CLOSE, B)

plt.figure()
ax1 = plt.subplot(121)
imshow(A, new_fig=False, title="Original")
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(Aclau, new_fig=False, title="Clausura")
plt.show(block=False)

# --- Apertura + Clausura -----------------------
f = cv2.imread("fingerprint.tif", cv2.IMREAD_GRAYSCALE)
imshow(f, title="Imagen Original")

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
fop = cv2.morphologyEx(f, cv2.MORPH_OPEN, se)
fop_cl = cv2.morphologyEx(fop, cv2.MORPH_CLOSE, se)

plt.figure()
ax1 = plt.subplot(131)
imshow(f, new_fig=False, title="Original")
plt.subplot(132, sharex=ax1, sharey=ax1)
imshow(fop, new_fig=False, title="Apertura")
plt.subplot(133, sharex=ax1, sharey=ax1)
imshow(fop_cl, new_fig=False, title="Apertura + Clausura")
plt.show(block=False)


# --- Gradiente Morfológico (Morphological Gradient) ------
f = cv2.imread("UTK.tif", cv2.IMREAD_GRAYSCALE)
# f = cv2.bitwise_not(f)        # Para analizar...
imshow(f, title="Imagen Original")

L = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (L, L))
f_mg = cv2.morphologyEx(f, cv2.MORPH_GRADIENT, kernel)

plt.figure()
ax1 = plt.subplot(121)
imshow(f, new_fig=False, title="Original", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(f_mg, new_fig=False, title="Gradiente Morfologico", ticks=True)
plt.show(block=False)


# --- Hit or Miss -------------------------------
# ----------------------------------------------
# B1 = strel([0 0 0;0 1 1;0 0 0]); B2 = strel([1 0 0;1 0 0;1 0 0]); g = HIT-or-MISS( f , B1 , B2 );
# ----------------------------------------------
f = cv2.imread("squares.tif", cv2.IMREAD_GRAYSCALE)
imshow(f, title="Imagen Original")

# Elemento estructural: "1": lugares donde debe haber hit / "-1":lugares donde debe haber miss /  "0": Da igual
B = np.array(
    [[-1, -1, -1], [-1, 1, 1], [-1, 1, 0]]
)  # Detección de esquina superior izquierda
# B = np.array([[-1, 0, 0], [-1, 1, 1], [-1, 0, 0]])    # Detección de "lado" izquierdo
print(B)
f_hom = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B)

plt.figure()
ax1 = plt.subplot(121)
imshow(f, new_fig=False, title="Original", ticks=True)
plt.subplot(122, sharex=ax1, sharey=ax1)
imshow(f_hom, new_fig=False, title="Hit or Miss")
plt.show(block=False)
