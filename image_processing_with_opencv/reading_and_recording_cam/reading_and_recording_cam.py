# reading and recording camera

import cv2 # importing opencv

cap = cv2.VideoCapture(0) # this'll access your laptop's cam

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height
print("Width: {}, Height: {}".format(width, height)) 

writer = cv2.VideoWriter("video_recording.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))
# DIVX -> decoder, 
# fourcc -> Four character code so We will use FourCC to define or use codecs in OpenCV.

while True: # untill false it'll work
    ret, frame = cap.read() # return and frame
    cv2.imshow("Video", frame) # it'll show each frame
    
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break # when you press q key exit

cap.realese() # stop capture
writer.realese() # stop recording
cv2.destroyAllWindows() # close all pages