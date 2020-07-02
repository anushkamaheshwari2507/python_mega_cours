# just for detecting the face
import cv2
from cv2.cv2 import CascadeClassifier

face_cascade = CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)
print(faces)
print(type(faces))
# just to make rectangle on the face
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("gray", img)
cv2.waitKey(0)
cv2.destroyAllWindow()
