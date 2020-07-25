import cv2

img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9,9), 0)
imgCanny = cv2.Canny(img, 150,200)

kernel = np.ones((5,5), np.uint8)
imgDilatation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("GrayImage",imgGray)
cv2.imshow("BlureedImage", imgBlur)
cv2.imshow("Edges", imgCanny)
cv2.imshow("Dilatation", imgDilatation)

cv2.waitKey(0)