import cv2

cap = cv2.VideoCapture(0)

object_detector = cv2.createBackgroundSubtractorMOG2(history=30, varThreshold=50)

while True:
    _, img = cap.read()
    detected = object_detector.apply(img)

    if detected.sum()/100000 > 100:
        text = '3rd level motion detected!'
    elif detected.sum()/100000 > 10:
        text = '2nd level motion detected!'
    elif detected.sum()/100000 > 1:
        text = '1st level motion detected!'
    else:
        text = 'Stable'

    print(text)
    cv2.putText(img, text, (10, 30), 1, 2, (0, 255, 0), 2)

    cv2.imshow('Original', img)
    cv2.imshow('Detected', detected)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()