import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Generamos datos a clasificar ------------------------------------------------------
X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
# X = np.random.randint(15,40,(25,2))
# Y = np.random.randint(50,75,(25,2))
Z = np.vstack((X,Y))
Z = np.float32(Z)
plt.scatter(Z[:,0], Z[:,1])
plt.show()

# --- K-means ---------------------------------------------------------------------------
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)  # criteria --> ( type, max_iter, epsilon )
ret, label, center = cv2.kmeans(Z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)  #  https://docs.opencv.org/master/d5/d38/group__core__cluster.html#ga9a34dc06c6ec9460e90860f15bcd2f88
                                                                                      
# Separo ambos clusters
A = Z[label.flatten()==0]
B = Z[label.flatten()==1]

# Plot
plt.scatter(A[:,0], A[:,1])
plt.scatter(B[:,0], B[:,1], c='r')
plt.scatter(center[:,0], center[:,1], s=80, c='y', marker='s')
plt.xlabel('dim1'), plt.ylabel('dim2')
plt.show()
