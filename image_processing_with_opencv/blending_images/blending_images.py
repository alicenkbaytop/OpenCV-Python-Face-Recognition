# blending images

import cv2 # importing opencv (it means open source computer vision)
import matplotlib.pyplot as plt # visualization modul

img1 = cv2.imread("eiffel_tower.jpg") # first input 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
# converting BGR to RGB ıt means converting ıts normal color
img2 = cv2.imread("river.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print("First Image Shape: ", img1.shape) # shape of img1
print("Second Image Shape: ", img2.shape) # shape og img2

img1 = cv2.resize(img1, (300,300)) # resizing both images 
img2 = cv2.resize(img2, (300,300))

plt.figure() # border
plt.imshow(img1) # show

plt.figure()
plt.imshow(img2)

# blended image = alpha*img1 + beta*img2
# this function is calculating automatically
blended_img = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended_img)