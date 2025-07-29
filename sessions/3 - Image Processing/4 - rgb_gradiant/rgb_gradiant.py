import cv2 as cv
import numpy as np


bg = np.zeros((400, 800, 3))

for i in range(400):
    bg[i, :] = (110 + i, 250 - i, 30 + i)

cv.imwrite('bg1.jpg', bg)
cv.imshow('background', bg)
cv.waitKey(0)