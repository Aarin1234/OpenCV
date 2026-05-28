import cv2
import numpy as np

image = cv2.imread("Images\Circles.jpg", 0,)
params = cv2.SimpleBlobDetector_Params()


#setting area filter parametos
params.filterByArea = True
params.minArea = 160

#setting circularity filter power
params.filterByCircularity=True 
params.minCircularity = 0.9

#setting comwexity.Filter parameter
params.filterByConvexity = True
params.minConvexity = 0.2

#setting the inertia filter parameter
params.filterByInertia = True
params.minInertiaRatio = 0.3

#Creating detector
detector = cv2.SimpleBlobDetector_create(params)
keyPoints = detector.detect(image)
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keyPoints, blank, (0,0,255),
cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keyPoints)
text = 'Number of Circular blobs:'+str(len(keyPoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_SIMPLEX,
1, (0,100,255), 2)
cv2.imshow('Filtering Circular Blobs Only', blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
