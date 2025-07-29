import cv2 as cv


detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)
if not cap.isOpened():
        print("Error: Could not open webcam. Check if it's connected or in use by another application.")

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_roi = frame[y:y + h, x:x + w]

        small_face = cv.resize(face_roi, (int(w * 0.08), int(h * 0.08)), interpolation=cv.INTER_LINEAR)
        mosaic_face_roi = cv.resize(small_face, (w, h), interpolation=cv.INTER_NEAREST)

        frame[y:y + h, x:x + w] = mosaic_face_roi

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break