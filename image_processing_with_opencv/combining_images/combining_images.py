# combining images

import cv2 # importing opencv (it means open source computer vision)
import numpy as np # numerical python

img = cv2.imread("King.jpg") # input image

horizantol = np.hstack((img,img)) # stacking horizantol
cv2.imshow("Horizantol Image", horizantol) # show new image

vertical = np.vstack((img,img)) # stacking vertical
cv2.imshow("Vertical Image", vertical) # show new image

cv2.waitKey(0) & 0xFF # without this line you can get error!