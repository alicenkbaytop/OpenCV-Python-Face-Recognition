# corner detection

import cv2 # importing opencv (it means open source computer vision)
import numpy as np # numerical python 
import matplotlib.pyplot as plt # visualization library

img = cv2.imread("sudoku.jpg",0) # input image
img = np.float32(img) # converting type
print("Image Shape: ", img.shape) # showing shape
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original")

# harris corner detection
corner1 = cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
plt.figure(), plt.imshow(corner1, cmap="gray"), plt.axis("off"), plt.title("Corner 1")
# block size = size of neighbourhood, kernel size, k = Harris detector free parameter in the equation.

# shi tomsai detection
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img) # converting type
corner2 = cv2.goodFeaturesToTrack(img, 120, 0.01, 10) 
# 120 = number of corner, 0.01 = quality level, 10 = min distance
corner2 = np.int64(corner2) # converting type

for i in corner2:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, (125,125,125), cv2.FILLED)
    # image, center, radius, color, fill
plt.imshow(img), plt.axis("off"), plt.title("Corner 2")