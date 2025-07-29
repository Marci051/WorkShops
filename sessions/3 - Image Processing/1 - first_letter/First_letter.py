import cv2 as cv
import numpy as np


bg = np.zeros((400, 400))

# F
bg[90:120, 130:280] = 255
bg[200:230, 130:280] = 255
bg[90:340, 130:160] = 255

# A





cv.imwrite('first_letter.jpg', bg)
cv.imshow('bg', bg)
cv.waitKey(0)


