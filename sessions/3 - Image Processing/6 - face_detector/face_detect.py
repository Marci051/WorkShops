import cv2 as cv


detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv.imread('face_test.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (180, 30, 200), 2)
    cv.putText(img, f"humans in this pic: {len(faces)}", (50, 30), cv.FONT_HERSHEY_PLAIN, 2, (255, 100, 190), 2)
    cv.imshow('image', img)
    cv.waitKey(0)
