# resizing and cropping

import cv2 # importing opencv library

img = cv2.imread("King.jpg") # reading image
print("Image Shape: ", img.shape) # shape of image
cv2.imshow("King", img) # show image

resized_img = cv2.resize(img, (400,400)) # resizing image first parameter
# is image and second is new image size
print("Resized Image Shape: ", resized_img.shape) # new shape
cv2.imshow("Resized King", resized_img) # new resized image show

cropped_img = img[100:200,200:400] # row 100:200 and column 200:400
print("Cropped Image Shape: ", cropped_img.shape) # new cropped image shape
cv2.imshow("Cropped King", cropped_img) # new cropped image show