import numpy as np
import cv2 as cv


img = cv.imread('rotate_task.jpg')
print(img.shape)

img = cv.rotate(img, cv.ROTATE_180)
cv.imshow('rotated', img)
cv.waitKey(0)
cv.imwrite('rotated.jpg', img)
