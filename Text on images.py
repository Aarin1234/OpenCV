import cv2

image = cv2.imread('Images\Pikachu.png')


#font
font = cv2.FONT_HERSHEY_COMPLEX

#origin
org = (50,50)

#fontscale
fontScale = 2

#colored text(b,g,r)
color = (0,255,0)

#line thickness
thickness = 3

#using cv2.putText
image = cv2.putText(image,'hello', org, font, fontScale, color, thickness,
 cv2.LINE_AA)
#displaying the image
window_name = 'Text on images'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
