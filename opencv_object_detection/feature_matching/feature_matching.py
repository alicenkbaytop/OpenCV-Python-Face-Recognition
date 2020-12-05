# feature matching

import cv2
import matplotlib.pyplot as plt

# main input
chos = cv2.imread("chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap = "gray"),plt.axis("off")

# second input
cho = cv2.imread("nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap = "gray"),plt.axis("off")

# orb detector 
# ORB is a fusion of FAST keypoint detector and BRIEF descriptor with some 
# added features to improve the performance.
# corner-edge etc.
orb = cv2.ORB_create()

# keypoint detection
#des - description
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# bf matcher
# Brute-Force matcher is simple. It takes the descriptor of one feature in first set 
# and is matched with all other features in second set using some distance calculation. And the closest one is returned.
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
# matching points
matches = bf.match(des1, des2)

# order by distance
matches = sorted(matches, key = lambda x: x.distance)

# matched images
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match), plt.axis("off"),plt.title("orb")

# improvement the method
# sift
sift = cv2.xfeatures2d.SIFT_create()

# bf
bf = cv2.BFMatcher()

# keypoint detection with sift
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k = 2)

good_match = []

for match1, match2 in matches:
    
    if match1.distance < 0.75*match2.distance:
        good_match.append([match1])
    
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho,kp1,chos,kp2,good_match,None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("sift")