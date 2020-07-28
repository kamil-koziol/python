from cv2 import cv2
import numpy as np
from time import sleep


img = cv2.imread("Resources/lambo.png")

def avgColour(img: np.ndarray):
    numOfPixels = img.shape[0] * img.shape[1]
    img.mean(0).mean(0)
    r, g,b = 0,0,0
    for y in img:
        for x in y:
            r += x[0]
            g += x[1]
            b += x[2]
    return (int(r/numOfPixels), int(g/numOfPixels), int(b/numOfPixels))


cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()

    color = np.zeros((512,512,3), dtype=np.uint8)
    color[:] = frame.mean(0).mean(0)
    
    cv2.imshow("Video",color)
    cv2.waitKey(100)