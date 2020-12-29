from cv2 import cv2
import numpy as np
from random import randint
import time

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

cv2.line(img, (0,0), (300,300), (50,128,255), 3)
cv2.rectangle(img, (0,0), (250,350), (255,0,0, 2), cv2.FILLED)
cv2.circle(img, (400,50), 30, (0,255,100), 5)
cv2.putText(img, "Hello there", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
cv2.imshow("Image", img)


cv2.waitKey(0)