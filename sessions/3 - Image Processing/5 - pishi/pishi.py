import cv2 as cv

image = cv.imread('pishi9.jpg')
gray = cv.imread('pishi9.jpg', cv.IMREAD_GRAYSCALE)

detector = cv.CascadeClassifier('haarcascade_frontalcatface.xml')

cats = detector.detectMultiScale(gray)
for (x, y, w, h) in cats:
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv.putText(image, f"cats in this pic: {len(cats)}", (50, 30), cv.FONT_HERSHEY_PLAIN, 2, (255, 100, 190), 2)
cv.imshow('image', image)
cv.waitKey(0)
cv.imwrite('detected.jpg', image)
