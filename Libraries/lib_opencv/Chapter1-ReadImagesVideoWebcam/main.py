from cv2 import cv2

img = cv2.imread("Resources/lena.png")
cv2.imshow("Result", img)

cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, image = cap.read()
    cv2.imshow("Video", image)
    cv2.waitKey(1)