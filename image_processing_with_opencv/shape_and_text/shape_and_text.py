# drawing shape and texting

import cv2 # importing opencv library
import numpy as np # importing numpy library and call such as np
import matplotlib.pyplot as plt
img = np.zeros((512,512,3), np.uint8) # first parameter is size and dimention second is type
print("Image Shape: ", img.shape)
cv2.imshow("Ground", img)

cv2.line(img, (0,0), (512,512), (0,255,0), 3)
# in line func. order, image, beginning point, last point, RGB color, thickness
# in OpenCv you should write BGR 
cv2.imshow("Line", img)

cv2.rectangle(img, (0,412), (100,512), (0,0,255), 3) # drawing rectangle
cv2.imshow("Rectangle", img) # showing rectangle

cv2.rectangle(img, (100,200), (300,400), (0,0,255), cv2.FILLED) # drawing rectangle
cv2.imshow("Rectangle", img) # showing filled rectangle

cv2.circle(img, (300,300), 30, (255,0,0), cv2.FILLED) # drawing circle
cv2.imshow("Rectangle", img) # showing circle

cv2.putText(img, "circle", (300,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
# order image, text, position, font, thickness, color
cv2.imshow("Text", img) # showing text

cv2.waitKey(0) & 0xFF # without this line you can get error!



