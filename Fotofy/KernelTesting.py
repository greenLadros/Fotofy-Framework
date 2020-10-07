
import cv2 as cv
import numpy as np

img = cv.imread('img.jpg')

smoothKernel = np.ones((5,5),np.float32) / 25
result = cv.filter2D(img, -1, smoothKernel)

#you can also
#result = cv.blur(img, (5,5))

kernel = np.ones((5,5), np.uint8)
result = cv.erode(img, kernel, iterations=3)

cv.imshow('Before', img)
cv.imshow('After', result)
cv.waitKey(0)
