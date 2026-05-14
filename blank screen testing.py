import cv2
import numpy as np
blank_scrn = np.zeros((300,400,3), dtype = 'uint8')
cv2.imshow('blank_scrn ',  blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Activity 1. To paint the output screen green
blank_scrn[:] =(0,255,0)
cv2.imshow('green screen', blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Activity 2. To paint the output screen red
blank_scrn[:] = (0,0,255)
cv2.imshow('red screen', blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Activity 3. To paint the output screen blue
blank_scrn[:] = (255,0,0)
cv2.imshow('blue screen', blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To paint half or a portion of the screen any collor
blank_scrn[21:170, 20:180]=0,255,0
cv2.imshow('portion green screen', blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Draw rect on blank screen
blank_scrn = np.zeros((300,400,3), dtype = 'uint8')

color_rect = (255,0,0)
thickness = -1
cv2.rectangle(blank_scrn, (0,0),(400,400), color_rect, thickness,)
cv2.imshow('rect on blank scrn', blank_scrn)
cv2.waitKey(0)
cv2.destroyAllWindows()
