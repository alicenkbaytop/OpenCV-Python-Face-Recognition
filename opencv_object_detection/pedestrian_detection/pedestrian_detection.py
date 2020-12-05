# pedestrian detection

import cv2 # importing opencv (it means open source computer vision)
import os # operating system

# files storage 
files = os.listdir()
img_path_list = []

# getting files
for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
print(img_path_list)

# hog descriptor
hog = cv2.HOGDescriptor()

# adding SVM detector
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# for each images
for imagePath in img_path_list:
    print(imagePath)

    image = cv2.imread(imagePath)

    (rects, weights) = hog.detectMultiScale(image, padding=(8,8), scale=1.05)        
    
    for (x,y,w,h) in rects:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255), 2)
        
    cv2.imshow("Pedestrian", image)
    if cv2.waitKey(0) & 0xFF == ord("q"): continue    