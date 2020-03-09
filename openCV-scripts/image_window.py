import cv2

image = cv2.imread('../.images/cane.jpg')

cv2.imshow('image', image)
cv2.waitKey(0)