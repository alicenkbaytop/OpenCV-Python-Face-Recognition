# face detection from video haar cascade

import cv2 # importing opencv (it means open source computer vision)

# importing haar cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(frame):
    # converting BGR to RGB ıt means converting ıts normal color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # converting BGR to gray 
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) # common scale
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        # drawing rectangle placement -> image, beginning, finish, color, thickness
        gray_face = gray[y:y + h, x:x + w] # border rectangle
        color_face = frame[y:y + h, x:x + w] # border rectangle
        eyes = eye_cascade.detectMultiScale(gray_face, 1.1, 3) # common scale
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2) # drawing rectangle
            # drawing rectangle placement -> image, beginning, finish, color, thickness
    return frame

video_capture = cv2.VideoCapture("video.mp4") # get a video capture object for the camera
# if ther is address it'll get video

while True:
    ret, frame = video_capture.read() # read what comes from the video
    canvas = detect(frame) # called the function
    cv2.imshow('Video', canvas) # showing each frame
    if cv2.waitKey(25) & 0xFF == ord('q'): # when you press q ıt'll close
        break
    
video_capture.release() # close video capture
cv2.destroyAllWindows() # close all pages