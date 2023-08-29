import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path=r"C:/Users/student/Desktop/Computer Vision/purple"
img=cv2.imread(path)

imgDilation=cv2.dilate(img,kernel,iterations=10)

cv2.imshow("img Dilation",imgDilation)
cv2.waitKey()
