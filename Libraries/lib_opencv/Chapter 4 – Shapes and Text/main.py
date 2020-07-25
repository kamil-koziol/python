from cv2 import cv2
import numpy as np
from random import randint
import time

img = np.zeros((512,512,3), np.uint8)
print(img.shape)


# cv2.line(img, (0,0), (300,300), (50,128,255), 3)
cap = cv2.VideoCapture(0)

while True:
    s, f = cap.read()
    f = cv2.Canny(f, 75,75)
    cv2.imshow('video', f)
    if cv2.waitKey(1) == ord('q'):
        break

# while True:
#     img[:] = (0,0,0)
#     cv2.line(
#         img, 
#         (0,0), 
#         (randint(100,512),randint(100,512)), 
#         (randint(0,255),randint(0,255),randint(0,255)), 
#         3
#     )
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1000) == ord("q"):
#         break