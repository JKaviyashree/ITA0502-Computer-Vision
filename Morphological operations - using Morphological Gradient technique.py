import cv2
import numpy as np
img = cv2.imread("C:/Users/kaviy/Downloads/G.jpg", cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(600,600))
kernel = np.ones((5,5), np.uint8)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Gradient", grad)
cv2.waitKey
