import cv2
import numpy as np
path=r"C:/Users/student/Desktop/Computer Vision/purple"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(imgBlur,100,200)
cv2.imshow("Img Canny",imgCanny)
cv2.waitKey()
