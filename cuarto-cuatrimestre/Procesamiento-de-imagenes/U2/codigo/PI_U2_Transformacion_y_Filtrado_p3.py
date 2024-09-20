import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- Ejemplo de la Transformada Discreta de Fourier 2D -------------------------------------------
img = cv2.imread('line_white.tif',0)
F = np.fft.fft2(img)
S = np.abs(F)
Slog = np.log(1.0 + S)

plt.subplot(221), plt.imshow(img, cmap = 'gray'), plt.title('Imagen'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(S, cmap = 'gray'), plt.title('Espectro de amplitud'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(np.fft.fftshift(S), cmap = 'gray'), plt.title('Espectro de amplitud centrado'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(np.fft.fftshift(Slog), cmap = 'gray'), plt.title('Espectro de amplitud centrado + log'), plt.xticks([]), plt.yticks([])
plt.show()

img_ifft = np.real(np.fft.ifft2(F))
plt.imshow(img_ifft,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()


# --- Filtrado en el dominio frecuencial ----------------------------------------------------------
def dftuv(M,N):
    # DFTUV Computes meshgrid frequency matrices.
    #    [U, V] = DFTUV(M, N) computes meshgrid frequency matrices U and
    #    V. U and V are useful for computing frequency-domain filter 
    #    functions that can be used with DFTFILT.  U and V are both M-by-N.

    # Set up range of variables.
    u = np.arange(M)   # u = 0:(M-1);   # Matlab
    v = np.arange(N)   # v = 0:(N-1);   # ...

    # Compute the indices for use in meshgrid
    idx = np.nonzero(u>M/2)             # idx = find(u > M/2);   # Matlab
    u[idx] = u[idx] - M                 # u(idx) = u(idx) - M;   # ...
    idy = np.nonzero(v>N/2)             # idy = find(v > N/2);   # ...
    v[idy] = v[idy] - M                 # v(idy) = v(idy) - N;   # ...

    # Compute the meshgrid arrays
    V,U = np.meshgrid(v,u)              # [V, U] = meshgrid(v, u);  # Matlab  
    
    return U,V


def lpfilter(tipo, M, N, D0=None, n=1.0):
    #    H = lpfilter(TYPE, M, N, D0, n) creates the transfer function of
    #    a lowpass filter, H, of the specified TYPE and size (M-by-N).  To
    #    view the filter as an image or mesh plot, it should be centered
    #    using np.fft.fftshift()
    # 
    #    Valid values for TYPE, D0, and n are:
    # 
    #    'ideal'    Ideal lowpass filter with cutoff frequency D0.  n need
    #               not be supplied.  D0 must be positive
    # 
    #    'btw'      Butterworth lowpass filter of order n, and cutoff D0.
    #               The default value for n is 1.0.  D0 must be positive.
    # 
    #    'gaussian' Gaussian lowpass filter with cutoff (standard deviation)
    #               D0.  n need not be supplied.  D0 must be positive.

    # Use function dftuv to set up the meshgrid arrays needed for 
    # computing the required distances.
    U,V = dftuv(M,N)                        # [U, V] = dftuv(M, N);         # Matlab

    # Compute the distances D(U, V).
    D = np.sqrt(U**2 + V**2)                # D = sqrt(U.^2 + V.^2);        # Matlab

    # % Begin fiter computations.
    if tipo=="ideal":
        H = (D<=D0).astype(np.float64)      # H = double(D <=D0);           # Matlab  
    elif tipo=="btw":
        H = 1 / (1 + (D/D0)**(2*n) )        # H = 1./(1 + (D./D0).^(2*n));   # Matlab  
    elif tipo=="gaussian":
        H = np.exp(-(D**2)/(2*(D0**2)))     # H = exp(-(D.^2)./(2*(D0^2)));  # Matlab  
    else:
        print('Unknown filter type.')
        H=None

    return H


def hpfilter(tipo, M, N, D0=None, n=1.0):
    return 1 - lpfilter(tipo, M, N, D0, n)




# --- Filtro sin padding --------------------------------------------------------------------------
img = cv2.imread('rectangle_bw.tif',0)
M,N = img.shape
F = np.fft.fft2(img)
sig = 10
H = lpfilter('gaussian',M,N,sig)
G = H*F
g = np.real(np.fft.ifft2(G))

plt.subplot(221), plt.imshow(img, cmap = 'gray'), plt.title('Imagen'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(np.abs(F), cmap = 'gray'), plt.title('Espectro de amplitud'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(H, cmap = 'gray'), plt.title('Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(g, cmap = 'gray'), plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
plt.show()

# --- Filtro con padding --------------------------------------------------------------------------
img = cv2.imread('rectangle_bw.tif',0)
M,N = img.shape
P,Q = M*2, N*2
Fp = np.fft.fft2(img,(P,Q))
sig = 10
Hp = lpfilter('gaussian',P,Q,2*sig)
Gp = Hp*Fp
gp = np.real(np.fft.ifft2(Gp))
gpc = gp[:M,:N]

plt.subplot(221), plt.imshow(img, cmap = 'gray'), plt.title('Imagen'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(np.abs(Fp), cmap = 'gray'), plt.title('Espectro de amplitud'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(Hp, cmap = 'gray'), plt.title('Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(gpc, cmap = 'gray'), plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
plt.show()

# --- Comparación ---------------------------------------------------------------------------------
plt.subplot(121) 
h=plt.imshow(g, cmap = 'gray')
plt.title('Imagen filtrada sin padding'), plt.colorbar(h), plt.xticks([]), plt.yticks([])
plt.subplot(122) 
h=plt.imshow(gpc, cmap = 'gray')
plt.title('Imagen filtrada con padding'), plt.colorbar(h), plt.xticks([]), plt.yticks([])
plt.show()


# -- Filtros en el dominio DFT a partir de filtros espaciales -------------------------------------
mean_filter = np.ones((3,3))/9
x = cv2.getGaussianKernel(5,10)
gaussian = x*x.T
sobel_x = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
sobel_y = np.array([[-1,-2,-1],
                   [0, 0, 0],
                   [1, 2, 1]])
laplacian =np.array([[0, 1, 0],
                    [1,-4, 1],
                    [0, 1, 0]])

filtros = [mean_filter, gaussian, laplacian, sobel_x, sobel_y]
filtros_nombres = ['mean_filter', 'gaussian','laplacian', 'sobel_x','sobel_y']
filtros_S = [np.abs(np.fft.fft2(x,(256,256))) for x in filtros]
for i in range(len(filtros)):
    plt.subplot(2,3,i+1) 
    plt.imshow( np.fft.fftshift(filtros_S[i]) ,cmap = 'gray')
    plt.title(filtros_nombres[i]), plt.xticks([]), plt.yticks([])
plt.show()   


# --- Plot 3D -----------------------------------------------
i=3
X,Y = np.meshgrid( range(filtros_S[i].shape[0]) ,range(filtros_S[i].shape[1]))
fig = plt.figure()
ax = fig.gca(projection='3d')        # Si esta linea no funciona, utilizar "ax = fig.add_subplot(projection='3d')"
ax.plot_surface(X, Y, np.fft.fftshift(filtros_S[i]),cmap='jet')
# ax.plot_wireframe(X, Y, np.fft.fftshift(filtros_S[i]), color='g')
# ax.plot_wireframe(X, Y, np.fft.fftshift(filtros_S[i]), rstride=20, cstride=20, color='g')
ax.set_title(filtros_nombres[i])
plt.show()

# --- Ejemplo: Sobel+ Umbralizado ------------------------------------------
f = cv2.imread('building.tif',cv2.IMREAD_GRAYSCALE)
F = np.fft.fft2(f) 
S = np.abs(F)
Slog= np.log(1.0 + S)

fig = plt.figure()
plt.subplot(121)
h=plt.imshow(f,cmap='gray')
plt.title('Imagen original'),plt.xticks([]), plt.yticks([])
plt.subplot(122)
h=plt.imshow(np.fft.fftshift(Slog),cmap='gray')
plt.title('Espectro de amplitud'),plt.xticks([]), plt.yticks([])
plt.show()

# --- Sobel+ Umbralizado ------------
# sobel_x = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]])
sobel_y = np.array([[-1,-2,-1],
                   [0, 0, 0],
                   [1, 2, 1]])
H = np.fft.fft2(sobel_y, img.shape) 
Y = F*H
y = np.real(np.fft.ifft2(Y))
y_abs = np.abs(y)
y_th = np.abs(y) > 0.15*np.max(np.abs(y))

ax1=plt.subplot(221)
h=plt.imshow(f,cmap='gray')
plt.colorbar(h), plt.title('Imagen original'),plt.xticks([]), plt.yticks([])

plt.subplot(222,sharex=ax1,sharey=ax1)
h=plt.imshow(y,cmap='gray')
plt.colorbar(h), plt.title('Imagen filtrada'),plt.xticks([]), plt.yticks([])

plt.subplot(223,sharex=ax1,sharey=ax1)
h=plt.imshow(y_abs, cmap='gray')
plt.colorbar(h), plt.title('Imagen filtrada + abs()'),plt.xticks([]), plt.yticks([])

plt.subplot(224,sharex=ax1,sharey=ax1)
h=plt.imshow(y_th, cmap='gray')
plt.colorbar(h), plt.title('Imagen filtrada + abs() + umbralado'),plt.xticks([]), plt.yticks([])

plt.show()


# --- Comparación de filtrado en dominio espacial vs frecuencial ----------------------------------
def dftfilt(f,H):
    #    G = DFTFILT(F, H) filters F in the frequency domain using the
    #    filter transfer function H. The output, G, is the filtered
    #    image, which has the same size as F.  DFTFILT automatically pads
    #    F to be the same size as H.  Function PADDEDSIZE can be used to
    #    determine an appropriate size for H.
    # 
    #    DFTFILT assumes that F is real and that H is a real, uncentered
    #    circularly-symmetric filter function. 

    # Obtain the FFT of the padded input.           
    F = np.fft.fft2(f, (H.shape[0], H.shape[1]))           # F = fft2(f, size(H, 1), size(H, 2));     # Matlab  

    # Perform filtering. 
    g = np.real(np.fft.ifft2(H*F))                       # g = real(ifft2(H.*F));                   # Matlab  

    # Crop to original size.
    g = g[:f.shape[0], :f.shape[1]]                      # g = g(1:size(f, 1), 1:size(f, 2));       # Matlab  
    
    return g

# --- Ejemplo -------------------------------------------------------------------------------------
img = cv2.imread('building.tif',cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float64)
w = np.array([[-1, 0, 1],
             [-2, 0, 2],
             [-1, 0, 1]], np.float64)
W = np.fft.fft2(w, (img.shape[0]*2, img.shape[1]*2))
gf = dftfilt(img,W)
gs = cv2.filter2D(img, -1, cv2.flip(w,-1), borderType=cv2.BORDER_CONSTANT, anchor=(w.shape[0]-1, w.shape[1]-1)) # Al hacer el flip para lograr la convolución, se debe modificar el anchor, ver docs.... (https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04)
# gs = cv2.filter2D(img, -1, w, borderType=cv2.BORDER_CONSTANT)     # Así hace la correlación, no la convolución.

# # --- Otra opción en vez de cambiar el anchor --> Cropping --------------------
# gs = cv2.filter2D(img, -1, cv2.flip(w,-1), borderType=cv2.BORDER_CONSTANT) 
# gf = gf[int(w.shape[0]/2): , int(w.shape[1]/2):]    
# gs = gs[: -int(w.shape[0]/2) , : -int(w.shape[1]/2)]  
# # -----------------------------------------------------------------------------

dif = gs-gf
abs(dif).max()

plt.figure()
ax1=plt.subplot(121)
h=plt.imshow(gs,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada - Dominio espacial'),plt.xticks([]), plt.yticks([])
plt.subplot(122,sharex=ax1,sharey=ax1)
h=plt.imshow(gf,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada - Dominio frecuencial'),plt.xticks([]), plt.yticks([])
plt.figure()
h=plt.imshow(dif,cmap='gray')
plt.colorbar(h), plt.title('Diferencia'),plt.xticks([]), plt.yticks([])
plt.show()


# --- Ejemplos de filtros ya implementaddos en OpenCV ---------------------------------------------
img = cv2.imread('cameraman.tif',0)
img_blurred = cv2.blur(img,(3,3))               # Idem filtro promedio 
#img_blurred = cv2.GaussianBlur(img,(9,9), 2)       # Idem Filtro Gaussiano  (mas ejemplos/info en https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html)
plt.subplot(121), plt.imshow(img,cmap='gray'), plt.title('Imagen Original')
plt.subplot(122), plt.imshow(img_blurred,cmap='gray'), plt.title('Imagen Filtrada')
plt.show()


# --- Filtro Pasa-alto ------------------------------------------------------------------------------
img = cv2.imread('letter_and_pattern.tif',0)
H = hpfilter('gaussian', img.shape[0]*2, img.shape[1]*2, img.shape[0]*0.15)
g = dftfilt(img,H)
plt.subplot(121)
h=plt.imshow(img,cmap='gray')
plt.colorbar(h), plt.title('Imagen Original')
plt.subplot(122)
h=plt.imshow(g,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada')
plt.show()

# --- Filtros de enfasis de alta frecuencia -------------------------------------------------------
img = cv2.imread('xray-chest.png',0)
HBW = hpfilter('btw', img.shape[0]*2, img.shape[1]*2, img.shape[0]*2*0.05, 1)
H = 0.5 + 2*HBW
g_hp = dftfilt(img, HBW)
g_enfasis = dftfilt(img, H)
g_enfasis_sc = cv2.normalize(g_enfasis, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)  # Paso a uint8 porque equalizeHist() toma uint8, utilizando todo el rango dinámico
g_eq = cv2.equalizeHist(g_enfasis_sc)

ax1=plt.subplot(221) 
h=plt.imshow(img,cmap='gray') 
plt.colorbar(h), plt.title('Imagen Original')
plt.subplot(222,sharex=ax1,sharey=ax1) 
h=plt.imshow(g_hp,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada HP')
plt.subplot(223,sharex=ax1,sharey=ax1) 
h=plt.imshow(g_enfasis,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada enfasis')
plt.subplot(224,sharex=ax1,sharey=ax1) 
h=plt.imshow(g_eq,cmap='gray')
plt.colorbar(h), plt.title('Imagen Filtrada enfasis + eq')
plt.show()


