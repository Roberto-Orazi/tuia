import cv2

face_cascade = cv2.CascadeClassifier()  
face_cascade.load(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")    
vid = cv2.VideoCapture(0)
  
while(True):
    ret, frame = vid.read()
    
    # --- Proceso ----------------------------------------------
    grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(grayimg)   
    image_faces = frame.copy()
    image_faces_blurred = frame.copy()
    if len(faces) != 0:        
        for (x, y, w, h) in faces:        
            cv2.rectangle(image_faces, (x,y), (x+w,y+h), (255,0,0), 2)                      # Agrego un rectángulo en cada cara
            cv2.arrowedLine(image_faces, (round(x+w/2), round(y-40)), (round(x+w/2), y), (0,0,255), 2, tipLength=0.5) 
            cv2.putText(image_faces, "Face!!", (x, round(y-45)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
            sub_face = frame[y:y+h, x:x+w]
            sub_face = cv2.GaussianBlur(sub_face, (23,23), 30)                              # Aplico borrosidad a cada cara...
            image_faces_blurred[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face    # ... y reemplazo en la imagen
    
    # --- Muestro figuras ----------------------------------------
    cv2.imshow('frame', frame)
    cv2.imshow('Faces', image_faces)
    cv2.imshow('Blurred Faces', image_faces_blurred)

    # --- Check exit ---------------------------------------------      
    if cv2.waitKey(1) == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()

