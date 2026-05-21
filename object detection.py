import cv2
import numpy as np

cat_image = cv2.imread('Images\Real cat.jpg',cv2.IMREAD_COLOR)
cv2.imshow('original image', cat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#converting bgr to gray image
gray=cv2.cvtColor(cat_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blurring out the image #the greater the odd number, the greater the blur 
#                             (horizontal blur, vertical blur)
gray_blurred = cv2.blur(gray, (9,9))#always odd number 
cv2.imshow('Gray blurred image', gray_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detecting circles
detect_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT,
dp = 1,minDist = 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

if detect_circles is not None:
    detect_circles = np.uint16(np.around(detect_circles))
    for pt in detect_circles[0, :]:
        a,b,r = pt[0], pt[1], pt[2]
        cv2.circle(cat_image, (a,b),r,(0,255,0),2)
        cv2.circle(cat_image, (a,b),1,(0,0,255),3)
        cv2.imshow('Detected Circles', cat_image)
        cv2.waitKey(0)
cv2.destroyAllWindows()  
