import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- Cargo imagen --------------------------------------------------
img = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE) 
ir, ic = 0, 0
row = img[ir,:]
col = img[:,ic]

# --- Genero plot ---------------------------------------------------
fig=plt.figure()
plt.subplot(2,2,1), plt.imshow(img, cmap="gray")
ha_row = plt.subplot(2,2,2) 
hp_row, = plt.plot(row)
ha_row.set_ylim([0, img.shape[0]-1])
plt.title("Row")
ha_col = plt.subplot(2,2,3) 
hp_col, = plt.plot(col)
ha_col.set_ylim([0, img.shape[1]-1])
plt.title("Columna")
fig.subplots_adjust(bottom=0.25)

# --- GUI -----------------------------------------------------------
ax_slider_row = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_slider_col = fig.add_axes([0.25, 0.05, 0.65, 0.03])

slider_row = Slider(
    ax=ax_slider_row,
    label='row',
    valmin=0,
    valmax=img.shape[0]-1,
    valinit=10,
)

slider_col = Slider(
    ax=ax_slider_col,
    label='column',
    valmin=0,
    valmax=img.shape[1]-1,
    valinit=10,
)

def update_slider_row(val):
    line = img[int(val),:]
    hp_row.set_ydata(line)

def update_slider_col(val):
    line = img[:, int(val)]
    hp_col.set_ydata(line)

slider_row.on_changed(update_slider_row)
slider_col.on_changed(update_slider_col)

# --- Muestro imagen ------------------------------------------------
plt.show()
