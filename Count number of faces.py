import cv2

# Load the pre-trained face detection model (Haar Cascade Classifier)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = r"C:\Computer Vision\jk-v-jimin.jpg"
img = cv2.imread(image_path)
img=cv2.resize(img,(400,400))
# Convert the image to grayscale for face detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

# Print the number of faces detected
print(f"Number of faces detected: {len(faces)}")

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with rectangles around the faces
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
