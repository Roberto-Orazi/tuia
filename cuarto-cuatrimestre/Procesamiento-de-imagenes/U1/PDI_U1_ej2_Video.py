import cv2

vid = cv2.VideoCapture(0)            # Si aparece warning, cambiar por "cv2.VideoCapture(0, cv2.CAP_DSHOW)". Info: https://stackoverflow.com/questions/60007427/cv2-warn0-global-cap-msmf-cpp-674-sourcereadercbsourcereadercb-termina
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):   # waitKey(): https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
        break                        # ord(): Devuelve el código Unicode de un caracter dado. 

vid.release()
cv2.destroyAllWindows()