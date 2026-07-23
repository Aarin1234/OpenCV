import cv2
import sys
import numpy
import os

hard_file = 'haar_face.xml'
datasets = 'dataset'
sub_data = 'Aarin'
path = os.path.join(datasets, sub_data)

if not os.path.isdir(path):
    os.makedir(path)
    width,height = (130,100)
    webcam = cv2.VideoCapture(0)
    print("[INFO] Capturing face images. Press 'q' to quit")
    count = 1
    while count<10:
        _, frame = webcam.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
