import cv2
import sys
import numpy
import os

haar_file = 'haar_face.xml'
datasets = 'dataset'
sub_data = 'Aarin'
path = os.path.join(datasets, sub_data)

if not os.path.isdir(path):
    os.mkdir(path)
width,height = (130,100)

face_cascade = cv2.CascadeClassifier(haar_file)

if face_cascade.empty():
        print('Error: haar_face.xml not found!')
        sys.exit()
webcam = cv2.VideoCapture(0)
print("[INFO] Capturing face images. Press 'q' to quit")
count = 1
while count<10:
        _, frame = webcam.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            face = gray_img[y:y+h, x:x+w]
            face_resize = cv2.resize(face, (w,h))
            cv2.imwrite(f'path/{count}.png', face_resize)
            print(f'[INFO] saved face{count}')
            count+=1

            #to capture ten images of the face
            if count > 10:
                break
        cv2.imshow('face capture', frame)
        if cv2.waitKey(10) == ord('q'):
            break
print('[INFO] capture demo')
webcam.release()
cv2.destroyAllWindows()
