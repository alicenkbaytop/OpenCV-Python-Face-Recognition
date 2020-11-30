# Reading image part

import cv2 # importing opencv (it means open source computer vision)

img = cv2.imread("king.jpg", 0) # reading image and convert gray 

cv2.imshow("King", img) # show our image

k = cv2.waitKey(0) & 0xFF # define to k for accessing keyboard 
#and if waitkey 0 it'll wait forever 

if k == 27: # 27 equal to esc key
    cv2.destroyAllWindows() # close image page
elif k == ord("s"): # when you press s firsly it'll take gray image then close
    cv2.imwrite("king_gray.jpg", img)
    cv2.destroyAllWindows()