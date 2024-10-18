import matplotlib

matplotlib.use("TkAgg")
import cv2
import numpy as np
import matplotlib.pyplot as plt


def local_histogram_equalization(img, window_size):
    if len(img.shape) != 2:
        raise ValueError("Input image must be grayscale.")

    rows, cols = img.shape
    M, N = window_size
    half_M, half_N = M // 2, N // 2

    padded_img = cv2.copyMakeBorder(
        img, half_M, half_M, half_N, half_N, cv2.BORDER_REPLICATE
    )

    output_img = np.zeros_like(img)

    for i in range(rows):
        for j in range(cols):
            window = padded_img[i : i + M, j : j + N]

            hist, _ = np.histogram(window.flatten(), bins=256, range=[0, 256])
            cdf = hist.cumsum()

            cdf_min = cdf[cdf > 0].min()
            cdf_range = cdf.max() - cdf_min

            img_val = window[half_M, half_N]
            output_val = (cdf[img_val] - cdf_min) * 255 / cdf_range
            output_img[i, j] = np.clip(output_val, 0, 255)

    return output_img.astype(np.uint8)


img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error reading the image. Check if the file path is correct.")
else:
    window_size_small = (3, 3)
    window_size_small_big = (3, 50)
    window_size_big_small = (50, 3)
    window_size_big = (250, 250)
    window_size_15 = (15, 15)
    window_size_25 = (25, 25)

    img_local_eq = local_histogram_equalization(img, window_size_small_big)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Imagen Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img_local_eq, cmap="gray")
    plt.title("Ecualización Local del Histograma")
    plt.axis("off")

    plt.show()
