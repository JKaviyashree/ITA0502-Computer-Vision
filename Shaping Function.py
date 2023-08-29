#Rectangle
import numpy as np
import cv2
img = np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(img,(30,30),(300,200),(0,255,0),5)
cv2.imshow("Rectangle",img)
cv2.waitKey()

#Square
import numpy as np
import cv2
img = np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(img,(30,30),(300,300),(0,255,0),5)
cv2.imshow("Square",img)
cv2.waitKey()

#Line
import numpy as np
import cv2
img = np.zeros((400,400,3),dtype="uint8")
cv2.line(img,(20,160),(100,160),(0,255,0),5)
cv2.imshow("Line",img)
cv2.waitKey()

#Circle
import numpy as np
import cv2
img = np.zeros((400,400,3),dtype="uint8")
cv2.circle(img,(200,200),80,(0,255,0),5)
cv2.imshow("Circle",img)
cv2.waitKey()
