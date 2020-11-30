# perspective warping

import cv2 # importing opencv (it means open source computer vision)
import numpy as np # numerical python 

img = cv2.imread("card.png") # input image
cv2.imshow("Image", img) # show input

width = 450
height = 500

#converting float type
position1 = np.float32([[203,0],[0,475],[540,148],[340,618]])
position2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

# perspective transforming
matrix = cv2.getPerspectiveTransform(position1, position2)
print(matrix) # show matrix

# perspective warping
output_img = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Output Image", output_img) # show output

cv2.waitKey(0) & 0xFF # without this line you can get error!