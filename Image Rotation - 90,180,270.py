import cv2
path= r"C:/Users/student/Desktop/Computer Vision/purple"
img = cv2.imread(path)
src = cv2.resize(img,(400,400))
window_name1 = 'Image 90 degree Rotation'
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name1, image)
#cv2.waitKey(0)

window_name2 = 'Image 180 degree Rotation'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name2, image)
#cv2.waitKey(0)

window_name3='Image 270 degree Rotation'
image=cv2.rotate(src,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name3,image)
cv2.waitKey(0)

