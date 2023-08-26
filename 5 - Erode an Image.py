import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path=r"C:/Users/student/Desktop/Computer Vision/purple"
img=cv2.imread(path)

imgEroded=cv2.erode(img,kernel,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
