# opencv is basically used to work on images or to process images
import cv2

img = cv2.imread("galaxy.jpg",1)
print(img)
#this is basically used to see your image
cv2.imshow("galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindow()
# you can also see the shape and dimension of any image
print(cv2.shape(img))
