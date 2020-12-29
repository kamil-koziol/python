from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
print(img.shape)
width = img.shape[0]
height = img.shape[1]
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2 = np.float32([[0,0], [width, 0], [0,height], [width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)

cv2.waitKey(0)