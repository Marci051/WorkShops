import cv2 as cv


img = cv.imread('jon_snow.jpg')
inverted = 255 - img
blurred = cv.GaussianBlur(inverted, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blurred', blurred)
cv.waitKey(0)

cv.imshow('inverted', inverted)
cv.waitKey(0)

blurred = 255 - blurred

output = img / blurred
output *= 255

cv.imwrite('output.png', output)
