import cv2
def rescale_frame(frame, scale = 0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions)


capture = cv2.VideoCapture('dog.mp4')

while True:
    isTrue, frame = capture.read()
    resized_frame =rescale_frame(frame, 
                                 scale = 0.35)
    cv2.imshow('orginal video', frame)
    cv2.imshow('resized video', resized_frame)
    if cv2.waitKey(20) & 0XFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
