import cv2
import numpy as numpy
path= r"C:/Users/kaviy/Downloads/G.jpg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
