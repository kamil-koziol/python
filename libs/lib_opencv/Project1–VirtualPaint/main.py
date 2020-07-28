from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

circles = []

myColors = {}
myColors["Blue"] = [(55,151,2),(132,255,255), (255,0,0)]

def getContours(_img):
    rects = []
    contours, hierarchy = cv2.findContours(_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cnt_length = cv2.arcLength(cnt, True)
            cnt_vertexes_approx = cv2.approxPolyDP(cnt, 0.02*cnt_length, True)
            rects.append(cv2.boundingRect(cnt_vertexes_approx))
    return rects

while True:
    success, frame = cap.read()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color in myColors:
        mask = cv2.inRange(frame_hsv, myColors[color][0], myColors[color][1])
        rect = getContours(mask)

        for position in rect:
            x,y,w,h = position
            circles.append(((x+w//2,y), myColors[color][2]))

    
    for circle in circles:
        cv2.circle(frame, circle[0], 5, circle[1], cv2.FILLED)
    
    cv2.imshow("Result",frame)
    cv2.waitKey(1)