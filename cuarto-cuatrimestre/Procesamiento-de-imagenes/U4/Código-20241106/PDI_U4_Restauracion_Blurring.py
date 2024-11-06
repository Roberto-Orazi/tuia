import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Imagen de entrada --------------------------------------
f = cv2.imread("patente_2_blur.jpg")
f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)

plt.figure(), plt.imshow(f), plt.show(block=False)

# --- Observo borrosidad -------------------------------------
# P1= (203,247) # Ojo! ...
# P2= (187,277) # Así queda al revés...
P1= (247,203)
P2= (277,187)

f2 = f.copy()
cv2.circle(f2,P1,2,(255,0,0),-1)
cv2.circle(f2,P2,2,(255,0,0),-1)
plt.figure(), plt.imshow(f2), plt.show(block=False)

dx = P2[0] - P1[0]
dy = np.abs(P2[1] - P1[1])
angle = np.arctan(dy/dx)
angle_grad = 180*angle/np.pi
d = (dx**2 + dy**2)**0.5
print(f"Angulo: {angle_grad:5.2f}  -  Desplazamiento: {d:5.2f}")

