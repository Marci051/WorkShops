import cv2 as cv
import numpy as np


img = cv.imread('mrincredible.jpeg')
rows, cols, channels = img.shape

# print(img)
gray_pic = np.zeros((rows, cols), dtype=np.uint8)


for row in range(rows):
    for col in range(cols):
        # print(img[row, col])
        b = img[row, col][0]
        g = img[row, col][1]
        r = img[row, col][2]
        gray_value = (int(r) + int(g) + int(b)) // 3
        gray_pic[row, col] = gray_value


cv.imwrite('rgb_to_gray.jpg', gray_pic)
cv.imshow('gray', gray_pic)
cv.waitKey(0)
cv.destroyAllWindows()