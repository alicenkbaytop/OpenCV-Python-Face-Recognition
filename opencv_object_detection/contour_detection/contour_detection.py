# contour detection

import cv2 # importing opencv (it means open source computer vision)
import numpy as np # numerical python 
import matplotlib.pyplot as plt # visualization library

img = cv2.imread("contour.jpg",0) # input image
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original")

contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# external, internal extraction

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    # external
    if hierarch[0][i][3] == -1: 
        cv2.drawContours(external_contour, contours, i, 255, thickness=-1)
    else: # internal
        cv2.drawContours(internal_contour, contours, i, 255, thickness=-1)
        
plt.figure(), plt.imshow(internal_contour, cmap="gray"), plt.axis("off"), plt.title("Internal")      
plt.figure(), plt.imshow(external_contour, cmap="gray"), plt.axis("off"), plt.title("External")  