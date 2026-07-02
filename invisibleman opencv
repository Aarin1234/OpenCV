import cv2
import numpy as np
import  time

raw_video = cv2.VideoCapture('C:\Users\gaura\
                             Documents\pygame one\Open Cv\\video.mp4')
time.sleep(1)
count = 0
background = 0
for i in range(60):
    return_val, background = raw_video.read()
    if return_val == False:
        continue
    background = np.flip(background,axis = 1)
    while(raw_video.isOpened()):
        return_val, img = raw_video.read()
    if not return_val:
        break
    count += 1
    image = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #define red ranges in HSV
    lower_red1 = np.array([100,40,40])
    upper_red1 = np.array([100,255,255])

    #detect red
    lower_red2 = np.array([155,40,40])
    upper_red2 = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1+mask2
    red-mask = cv2.bitwise_or(mask1,mask2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),
                             np.uint8), iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)
    #now invert the mask
