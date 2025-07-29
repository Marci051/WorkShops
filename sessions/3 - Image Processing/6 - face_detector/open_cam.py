import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv.imshow('Camera Feed', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break

cap.release()
cv.destroyAllWindows()