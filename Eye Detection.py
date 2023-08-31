import cv2

# Load the pre-trained eye detection model (Haar Cascade Classifier)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the image
image_path = r"c:/Users/student/Desktop/Computer Vision/jk-v-jimin.jfif"
img = cv2.imread(image_path)
#img=cv2.resize(img,(400,400))
# Convert the image to grayscale for eye detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eye in the grayscale image
eye = eye_cascade.detectMultiScale(gray,1.1,10)

# Print the number of eye detected
print(f"Number of Eye detected: {len(eye)}")

# Draw rectangles around the detected eye
for (x, y, w, h) in eye:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with rectangles around the eye
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
