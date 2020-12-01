# edge detection

import cv2 # importing opencv (it means open source computer vision)
import numpy as np # numerical python
import matplotlib.pyplot as plt # visulization library

img = cv2.imread("king.jpg",0) # input image
# show input
plt.figure(), plt.imshow(img, cmap="gray"), plt.title("Original Image")

# simple paramters
edged_img = cv2.Canny(image=img, threshold1=0, threshold2=255)
plt.figure(), plt.imshow(edged_img, cmap="gray"), plt.title("Edge Image")

#blured img
blurred_img = cv2.blur(img, ksize=(7,7)) # ksize = kernel size

med_val = np.median(blurred_img) 

low = int(max(0, (1 - 0.33) * med_val)) # common formula
high = int(min(255, (1 + 0.33) * med_val))

blurred_img1 = cv2.Canny(image=img, threshold1=low, threshold2=high)
plt.figure(), plt.imshow(blurred_img1, cmap="gray"), plt.title("Blured Image")