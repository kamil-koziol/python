from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    s, frame = cap.read()
    frame = 