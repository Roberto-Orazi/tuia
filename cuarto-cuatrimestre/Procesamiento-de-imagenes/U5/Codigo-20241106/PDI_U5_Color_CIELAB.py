import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Cargo Imagenes --------------------------------------------
bright = cv2.imread('cube_1_outdoor.png')
dark = cv2.imread('cube_1_indoor.png')
bright = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)
dark = cv2.cvtColor(dark, cv2.COLOR_BGR2RGB)

# --- CIELAB -----------------------------------------------------
brightLAB = cv2.cvtColor(bright, cv2.COLOR_RGB2LAB)
darkLAB = cv2.cvtColor(dark, cv2.COLOR_RGB2LAB)

plt.figure()
ax1 = plt.subplot(241); plt.xticks([]), plt.yticks([]), plt.imshow(bright), plt.title('BRIGHT')
plt.subplot(242,sharex=ax1,sharey=ax1), plt.imshow(brightLAB[:,:,0], cmap="gray"), plt.title('L')
plt.subplot(243,sharex=ax1,sharey=ax1), plt.imshow(brightLAB[:,:,1], cmap="gray"), plt.title('A')
plt.subplot(244,sharex=ax1,sharey=ax1), plt.imshow(brightLAB[:,:,2], cmap="gray"), plt.title('B')
plt.subplot(245,sharex=ax1,sharey=ax1), plt.imshow(dark), plt.title('DARK')
plt.subplot(246,sharex=ax1,sharey=ax1), plt.imshow(darkLAB[:,:,0], cmap="gray"), plt.title('L')
plt.subplot(247,sharex=ax1,sharey=ax1), plt.imshow(darkLAB[:,:,1], cmap="gray"), plt.title('A')
plt.subplot(248,sharex=ax1,sharey=ax1), plt.imshow(darkLAB[:,:,2], cmap="gray"), plt.title('B')
plt.show(block=False)

# --- HSV ---------------------------------------------------------------
bright_HSV = cv2.cvtColor(bright, cv2.COLOR_RGB2HSV)
dark_HSV = cv2.cvtColor(dark, cv2.COLOR_RGB2HSV)

plt.figure()
ax1 = plt.subplot(241); plt.xticks([]), plt.yticks([]), plt.imshow(bright), plt.title('BRIGHT')
plt.subplot(242,sharex=ax1,sharey=ax1), plt.imshow(bright_HSV[:,:,0], cmap="gray"), plt.title('H')
plt.subplot(243,sharex=ax1,sharey=ax1), plt.imshow(bright_HSV[:,:,1], cmap="gray"), plt.title('S')
plt.subplot(244,sharex=ax1,sharey=ax1), plt.imshow(bright_HSV[:,:,2], cmap="gray"), plt.title('V')
plt.subplot(245,sharex=ax1,sharey=ax1), plt.imshow(dark), plt.title('DARK')
plt.subplot(246,sharex=ax1,sharey=ax1), plt.imshow(dark_HSV[:,:,0], cmap="gray"), plt.title('H')
plt.subplot(247,sharex=ax1,sharey=ax1), plt.imshow(dark_HSV[:,:,1], cmap="gray"), plt.title('S')
plt.subplot(248,sharex=ax1,sharey=ax1), plt.imshow(dark_HSV[:,:,2], cmap="gray"), plt.title('V')
plt.show(block=False)

