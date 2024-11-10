"""
Remoción de borrosidad por movimiento Uso:
  python3 PDI_U4_Restauracion_p4_Filtrado_Inverso.py  --img <source_image>
"""

import argparse
import sys
import cv2
import numpy as np


def motion_blur_kernel(length, rotation):
    """
    Genera un kernel de borrosidad lineal.

    Parametros
    ----------
        length : int      --> La longitud del filtro rotation : float  --> El ángulo del desplazamiento, en grados.
    """
    # --- Genero kernel horizontal -----------------------------------
    kernel_motion_blur = np.zeros((length, length))
    kernel_motion_blur[int((length - 1) / 2), :] = np.ones(length)
    kernel_motion_blur = kernel_motion_blur / length

    # --- Roto el kernel de acuerdo al ángulo ------------------------ Aplior una rotación afín. La función
    # cv2.getRotationMatrix2D genera una matriz de rotación dado un pivot y un ángulo.
    M = cv2.getRotationMatrix2D(((length - 1) / 2, (length - 1) / 2), rotation, 1)

    # La funcion cv2.warpAffine aplica una transformación afín dada una matriz de transformación:
    return cv2.warpAffine(kernel_motion_blur, M, kernel_motion_blur.shape)


def weiner_deconvolution(img, psf, snr):
    """
    Aplica una deconvolución Wiener dada la imagen degradada, el kernel o PSF que modela la distorción (Point Spread
    Function) y  un valor de SNR.

    Entradas
    ----------
        img : numpy.ndarray
            La imagen degradada
        psf : numpy.ndarray
            Kernel o PSF (Point Spread Function) que modela la degradación convolucional.
        snr : float
            Relación señal a ruido, en db.
    Salida
    -------
            La imagen restaurada : numpy.ndarray
    """
    # --- Debug ------ print("### PSF ###########################################") print(psf)

    # NSR: relación noise/signal (el inverso del SNR), en escala lineal.
    NSR = 10.0 ** (-0.1 * snr)

    # Expandir el kernel con ceros para igualar el tamaño de la imagen.
    psf_pad = np.zeros_like(img)
    kh, kw = psf.shape
    psf_pad[:kh, :kw] = psf

    # Deconvolución Wiener en el dominio frecuencial.
    IMG = np.fft.fft2(img)
    PSF = np.fft.fft2(psf_pad)
    RES = IMG * (PSF / (np.abs(PSF) ** 2 + NSR))

    # Transformada inversa.
    deconvolved = np.fft.ifft2(RES)

    # Dado que el elemento central del kernel está ubicado en (kw/2,kh/2) y no(0,0), la imagen resultante sufre una
    # traslación de (kw/2,kh/2). Esto se resuelve aplicando un roll (desplazamiento estilo buffer circular) en
    # (-kw/2,-kh/2).
    deconvolved = np.roll(deconvolved, -kh // 2, 0)
    deconvolved = np.roll(deconvolved, -kw // 2, 1)
    return deconvolved


def update(_):
    """
    GUI: Manejo de eventos.
    """
    # --- Obtengo parámetros de la GUI -----------------------------------
    angle = cv2.getTrackbarPos("Angulo", "Filtrado Inverso")
    snr = cv2.getTrackbarPos("SNR (db)", "Filtrado Inverso")
    length = cv2.getTrackbarPos("Longitud", "Filtrado Inverso")

    # --- Proceso parámetros --------------------------------------------- OpenCV no permite setear un mínimo para las
    # trackbars, los valores no válidos se deben manejar explícitamente.
    if length <= 0:
        print(str(length) + " no es una longitud válida para el kernel, usando 1")
        length = 1

    # --- Construyo el kernel según modelo de borrosidad -----------------
    psf = motion_blur_kernel(length, angle)

    # --- Filtrado Inverso: Wienner (deconvolución plano a plano) --------
    restored_img = np.empty_like(source_img)
    for n in range(3):
        result = weiner_deconvolution(source_img[:, :, n], psf, snr)
        restored_img[:, :, n] = np.real(result)

    # --- Muestro Resultado ----------------------------------------------
    cv2.imshow("Filtrado Inverso", restored_img)


# --- Proceso argumentos de entrada --------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--img", required=True)
args = parser.parse_args()
src_path = args.img

# --- Imagen de entrada --------------------------------------------------------
source_img = cv2.imread(src_path, cv2.IMREAD_COLOR)
if source_img is None:
    print("Error al cargar la imagen:", src_path)
    sys.exit(1)

source_img = np.float32(source_img) / 255.0  # Paso a float.
cv2.imshow("Imagen Original", source_img)

# ---  GUI ---------------------------------------------------------------------
cv2.namedWindow("Filtrado Inverso")
cv2.createTrackbar("Angulo", "Filtrado Inverso", 0, 180, update)
cv2.createTrackbar("Longitud", "Filtrado Inverso", 1, 100, update)
cv2.createTrackbar("SNR (db)", "Filtrado Inverso", 0, 50, update)
update(None)

# ---Loop hasta presionar ESC --------------------------------------------------
while True:
    ch = cv2.waitKey()
    if ch == 27:
        break
    if ch == ord(" "):
        defocus = not defocus
        update(None)
