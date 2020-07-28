from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerMedianFlow_create()

for i in range(10):
    s, frame = cap.read()

bbox = cv2.selectROI("Video",frame, True)
tracker.init(frame, bbox)

while True:
    s, frame = cap.read()
    success, bbox = tracker.update(frame)
    if success:
        x,y,w,h = bbox
        x,y,w,h = int(x), int(y), int(w), int(h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,150), 2)
        
    cv2.imshow("Video", frame)
    cv2.waitKey(1)