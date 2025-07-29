import cv2 as cv
import numpy as np


bg = np.zeros((500, 800, 3))

bg[:, :] = (43, 142, 243)

rows, cols, channels = bg.shape
print(rows, cols)

distance = cols // 8
# middle line
cv.line(bg, (cols//2, 0), (cols//2, rows), 0, 2)
# middle circle
cv.circle(bg, (cols//2, rows//2), distance//2, 0, 2)

# left
cv.rectangle(bg, (0, 180), ((distance*2), 320), 0, 2)
cv.ellipse(bg, (0, rows//2), (250, rows//2), 180, 90, 270, 0, 2)
cv.circle(bg, (200, rows//2), distance//2, 0, 2)

# right
cv.rectangle(bg, (cols, 320), (600, 180), 0, 2)
cv.ellipse(bg, (cols, rows//2), (250, rows//2), 0, 90, 270, 0, 2)
cv.circle(bg, (600, rows//2), distance//2, 0, 2)





cv.imshow('bg', bg)
cv.waitKey(0)

cv.imwrite('output.png', bg)