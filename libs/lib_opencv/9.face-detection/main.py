from cv2 import cv2
import numpy as np

facecascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(grayFrame, 1.1, 4)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    cv2.imshow("Video", frame)
    cv2.waitKey(1)