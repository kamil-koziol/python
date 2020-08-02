
from cv2 import cv2
import numpy as np

# 70 levels of gray 
gscale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
  
# 10 levels of gray 
gscale2 = '@%#*+=-:. '

img = cv2.imread("IMG_0957.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (64,64))
img = cv2.Canny(img, 150,150)
# text = "jd"
# shape, offsetY = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
# print(offsetY)
# img = np.zeros((shape[1]*2, shape[0]))
# cv2.putText(img, text, (0,offsetY*3), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

with open("ascii.txt", "w") as f:
    for row in img:
        for x in row:
            f.write(gscale2[int(x*9)//255])
        f.write("\n")