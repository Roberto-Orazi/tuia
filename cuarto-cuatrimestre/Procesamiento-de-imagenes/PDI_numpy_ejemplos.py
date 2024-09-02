import numpy as np

# --- Vectores y Matrices -----------------------------------------------------
# Vectores
x = np.array([1,2,3])
type(x)
x.dtype
x.shape
len(x)

x = np.array([1,2,3], dtype=np.uint8)
x.dtype

# Matrices
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], dtype=np.uint8)
type(x)
x.dtype
x.shape
w, h = x.shape
len(x)
x
x.T

# --- Operaciones sobre vectores ----------------------------------------------
x = np.array([1,2,3,0,6,9,7], dtype=np.uint8)
x
x.min()
x.max()
x.argmin()
x.argmax()
np.unique(x)

# x.sort()    # Modifica el vector!
x2 = x.copy()
x2.sort()

ix = x.argsort()
x3 = x[ix]

x==2
np.where(x==2)


# --- Operaciones sobre matrices --------------------------------
x = np.array([[2,0,4],[1,6,9],[3,8,5],[12,7,11]], dtype=np.uint8)
x
x.min()
x.max()
x.argmin()
x.argmax()

# x[x.argmax()]     # Por que da error?
r,c = np.unravel_index(x.argmax(), x.shape)
x[r, c]

np.unique(x)

# Analisis en una sola dimensión
x
x.min(axis=0)
x.max(axis=0)
x.argmin(axis=0)
x.argmax(axis=0)


# --- Otros metodos -------------------------------------------
x = np.arange(10)
x = np.arange(4, 9)
x = np.arange(4, 9, 2)

