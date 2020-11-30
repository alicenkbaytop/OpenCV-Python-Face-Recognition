# reading video part

import cv2 # importing opencv
import time # time modul

video = "video.mp4" # video path

cap = cv2.VideoCapture(video) # importing video

if cap.isOpened() == False: # checking video
    print("Error!!!") # if there is error it'll show this output
    
print("Width: ", cap.get(3)) # get function's 3rd parameter equal to width
print("Height: ", cap.get(4)) # get function's 4th parameter equal to height

while True: # untill false it'll work
    ret, frame = cap.read() # return and frame
    
    if ret == True: # if there is return
        #time.sleep(0.01) # it'll make slower
        cv2.imshow("Street Video", frame) # it'll show each frame
    
    else: 
        break # if video finished exit
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # when you press q key exit
        break
    
cap.realese() # stop capture
cv2.destrowAllWindows() # close all pages