# Choosing 3 points on the image and according to that calculating the angle between them.
# add opencv and math library        
import cv2 
import math
 
# test image
path = 'angles.jpg'
img = cv2.imread(path)

# stored points
pointsList = []
 
# left click for point assignment
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        
        if size != 0 and size % 3 != 0:
            # image, start point, end point, color, thickness
            cv2.line(img, tuple(pointsList[size-1]), (x,y), (0,0,255), 2) 
                
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED) 
        pointsList.append([x,y])

# calculation gradient(slope)
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
 
# calculation angle using slope
def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt2,pt3)
    angR = math.atan((m1-m2)/(1+(m1*m2))) # trigonometrical relation
    angD = abs(int(math.degrees(angR)))
 
    cv2.putText(img, str(angD), pt2, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
 
while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        getAngle(pointsList)
 
    cv2.imshow('Angle Finder', img)
    cv2.setMouseCallback('Angle Finder', mousePoints)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        pointsList = []
        img = cv2.imread(path)
    
cv2.destroyAllWindows()        