import cv2
img = cv2.imread(r"C:\Computer Vision\makne.jpg")
gray_img = cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)
haarcascade =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
faces_rec = haarcascade.detectMultiScale(gray_img,1.1,10)
for (x,y,w,h) in faces_rec:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

cv2.imshow('Detected Eyes',img)
cv2.waitKey(0)
