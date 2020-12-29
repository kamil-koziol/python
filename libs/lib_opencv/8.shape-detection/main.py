from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img, (7,7), 1)
img = cv2.Canny(img, 50,50)

def getContours(_img):
    contours, hierarchy = cv2.findContours(_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # area = cv2.contourArea(cnt)
        # cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
        cnt_length = cv2.arcLength(cnt, True)
        cnt_vertexes_approx = cv2.approxPolyDP(cnt, 0.02*cnt_length, True)
        x,y,w,h = cv2.boundingRect(cnt_vertexes_approx)
        cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 3)

getContours(img)
cv2.imshow("Image", img)
cv2.imshow("Contours", imgContour)
cv2.waitKey(0)