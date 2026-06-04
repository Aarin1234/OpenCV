import cv2

capture = cv2.VideoCapture(0)#0 is for your system integrated camera
#and 1 is for and other camera

while True:
    isTrue,frame = capture.read()
    cv2.imshow('My video', frame)
    if cv2.waitKey(20) & 0XFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
