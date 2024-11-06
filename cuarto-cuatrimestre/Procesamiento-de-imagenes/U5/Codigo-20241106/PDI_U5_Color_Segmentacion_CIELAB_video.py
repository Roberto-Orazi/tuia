# https://docs.opencv.org/4.x/da/d97/tutorial_threshold_inRange.html
import cv2

# Incializo Nombres GUI
win_frame = 'Frame'
win_GUI = 'GUI'
win_mask = 'Mascara'
win_frame_filtrado = 'Frame filtrado'
win_frame_filtrado_neg = 'Frame filtrado negativo'
L_low_name = 'L low'
A_low_name = 'A low'
B_low_name = 'B low'
L_high_name = 'L high'
A_high_name = 'A high'
B_high_name = 'B high'

# Incializo Variables
max_value = 255
L_low = 0
A_low = 0
B_low = 0
L_high = max_value
A_high = max_value
B_high = max_value


def on_L_low_thresh_trackbar(val):
    global L_low
    global L_high
    L_low = val
    L_low = min(L_high-1, L_low)
    cv2.setTrackbarPos(L_low_name, win_GUI, L_low)

def on_L_high_thresh_trackbar(val):
    global L_low
    global L_high
    L_high = val
    L_high = max(L_high, L_low+1)
    cv2.setTrackbarPos(L_high_name, win_GUI, L_high)

def on_A_low_thresh_trackbar(val):
    global A_low
    global A_high
    A_low = val
    A_low = min(A_high-1, A_low)
    cv2.setTrackbarPos(A_low_name, win_GUI, A_low)

def on_A_high_thresh_trackbar(val):
    global A_low
    global A_high
    A_high = val
    A_high = max(A_high, A_low+1)
    cv2.setTrackbarPos(A_high_name, win_GUI, A_high)

def on_B_low_thresh_trackbar(val):
    global B_low
    global B_high
    B_low = val
    B_low = min(B_high-1, B_low)
    cv2.setTrackbarPos(B_low_name, win_GUI, B_low)

def on_B_high_thresh_trackbar(val):
    global B_low
    global B_high
    B_high = val
    B_high = max(B_high, B_low+1)
    cv2.setTrackbarPos(B_high_name, win_GUI, B_high)



cap = cv2.VideoCapture(0)

# --- Creo ventanas ---------------------------------------------------------------------------------------
cv2.namedWindow(win_frame)
cv2.namedWindow(win_GUI)
# cv2.namedWindow(win_GUI,cv2.WINDOW_NORMAL)
# cv2.resizeWindow(win_GUI,450,50)
cv2.namedWindow(win_mask)
cv2.namedWindow(win_frame_filtrado)
cv2.namedWindow(win_frame_filtrado_neg)

# --- Creo GUI --------------------------------------------------------------------------------------------
cv2.createTrackbar(L_low_name, win_GUI , L_low, max_value, on_L_low_thresh_trackbar)
cv2.createTrackbar(L_high_name, win_GUI , L_high, max_value, on_L_high_thresh_trackbar)
cv2.createTrackbar(A_low_name, win_GUI , A_low, max_value, on_A_low_thresh_trackbar)
cv2.createTrackbar(A_high_name, win_GUI , A_high, max_value, on_A_high_thresh_trackbar)
cv2.createTrackbar(B_low_name, win_GUI , B_low, max_value, on_B_low_thresh_trackbar)
cv2.createTrackbar(B_high_name, win_GUI , B_high, max_value, on_B_high_thresh_trackbar)

while True:
    # --- Obtengo frame -----------------------------------------------
    ret, frame = cap.read()
    if frame is None:
        break

    # --- Proceso -----------------------------------------------------
    frame_LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    frame_threshold = cv2.inRange(frame_LAB, (L_low, A_low, B_low), (L_high, A_high, B_high))
    frame_filtrado = cv2.bitwise_and(frame, frame, mask=frame_threshold)
    frame_filtrado_neg = cv2.bitwise_and(frame, frame, mask=~frame_threshold)
    
    # --- Muestro -----------------------------------------------------
    cv2.imshow(win_frame, frame)
    cv2.imshow(win_mask, frame_threshold)
    cv2.imshow(win_frame_filtrado, frame_filtrado)
    cv2.imshow(win_frame_filtrado_neg, frame_filtrado_neg)
    
    # --- Termino? ----------------------------------------------------
    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break
    