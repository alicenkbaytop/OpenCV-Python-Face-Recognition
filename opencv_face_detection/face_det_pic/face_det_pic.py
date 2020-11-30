# face detection from picture haar cascade

import cv2 # importing opencv (it means open source computer vision)

# importing haar cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(frame):
    # converting BGR to RGB ıt means converting ıts normal color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # converting BGR to gray 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # common scale  
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # drawing rectangle placement -> image, beginning, finish, color, thickness
        roi_gray = gray[y:y+h, x:x+w] # border rectangle
        roi_color = frame[y:y+h, x:x+w] # border rectangle
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # common scale
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) # drawing rectangle
            
    return frame

image = cv2.imread("lebron_james.jpg") # reading image
image = detect(frame=image) # called the function
cv2.imwrite('lebron_output.jpg', image) # save new image