# https://docs.opencv.org/4.x/da/d97/tutorial_threshold_inRange.html
import cv2

# Incializo Nombres GUI
win_frame = 'Frame'
win_GUI = 'GUI'
win_mask = 'Mascara'
win_frame_filtrado = 'Frame filtrado'
win_frame_filtrado_neg = 'Frame filtrado negativo'
H_low_name = 'H low'
S_low_name = 'S low'
V_low_name = 'V low'
H_high_name = 'H high'
S_high_name = 'S high'
V_high_name = 'V high'

# Incializo Variables
max_value = 255
max_value_H = 360//2
H_low = 0
S_low = 0
V_low = 0
H_high = max_value_H
S_high = max_value
V_high = max_value


def on_H_low_thresh_trackbar(val):
    global H_low
    global H_high
    H_low = val
    H_low = min(H_high-1, H_low)
    cv2.setTrackbarPos(H_low_name, win_GUI, H_low)

def on_H_high_thresh_trackbar(val):
    global H_low
    global H_high
    H_high = val
    H_high = max(H_high, H_low+1)
    cv2.setTrackbarPos(H_high_name, win_GUI, H_high)

def on_S_low_thresh_trackbar(val):
    global S_low
    global S_high
    S_low = val
    S_low = min(S_high-1, S_low)
    cv2.setTrackbarPos(S_low_name, win_GUI, S_low)

def on_S_high_thresh_trackbar(val):
    global S_low
    global S_high
    S_high = val
    S_high = max(S_high, S_low+1)
    cv2.setTrackbarPos(S_high_name, win_GUI, S_high)

def on_V_low_thresh_trackbar(val):
    global V_low
    global V_high
    V_low = val
    V_low = min(V_high-1, V_low)
    cv2.setTrackbarPos(V_low_name, win_GUI, V_low)

def on_V_high_thresh_trackbar(val):
    global V_low
    global V_high
    V_high = val
    V_high = max(V_high, V_low+1)
    cv2.setTrackbarPos(V_high_name, win_GUI, V_high)



cap = cv2.VideoCapture(0)

# --- Creo ventanas ---------------------------------------------------------------------------------------
cv2.namedWindow(win_frame)
cv2.namedWindow(win_GUI)
cv2.namedWindow(win_mask)
cv2.namedWindow(win_frame_filtrado)
cv2.namedWindow(win_frame_filtrado_neg)

# --- Creo GUI --------------------------------------------------------------------------------------------
cv2.createTrackbar(H_low_name, win_GUI , H_low, max_value_H, on_H_low_thresh_trackbar)
cv2.createTrackbar(H_high_name, win_GUI , H_high, max_value_H, on_H_high_thresh_trackbar)
cv2.createTrackbar(S_low_name, win_GUI , S_low, max_value, on_S_low_thresh_trackbar)
cv2.createTrackbar(S_high_name, win_GUI , S_high, max_value, on_S_high_thresh_trackbar)
cv2.createTrackbar(V_low_name, win_GUI , V_low, max_value, on_V_low_thresh_trackbar)
cv2.createTrackbar(V_high_name, win_GUI , V_high, max_value, on_V_high_thresh_trackbar)

while True:
    # --- Obtengo frame -----------------------------------------------
    ret, frame = cap.read()
    if frame is None:
        break

    # --- Proceso -----------------------------------------------------
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (H_low, S_low, V_low), (H_high, S_high, V_high))
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
    