import cv2  # OpenCV library for computer vision tasks

# Initialize the webcam (0 is the default webcam index)
cap = cv2.VideoCapture(0)

# Create a background subtractor for motion detection
# `history` defines the number of frames to build the background model
# `varThreshold` determines the sensitivity of the motion detection
object_detector = cv2.createBackgroundSubtractorMOG2(history=30, varThreshold=50)

while True:
    # Capture a frame from the webcam
    _, img = cap.read()

    # Apply the background subtractor to detect motion
    detected = object_detector.apply(img)

    # Calculate the intensity of detected motion
    # Divide the sum of detected pixels by a scaling factor for easier comparison
    motion_level = detected.sum() / 100000

    # Categorize the motion intensity into different levels
    if motion_level > 100:
        text = '3rd level motion detected!'  # High-intensity motion
    elif motion_level > 10:
        text = '2nd level motion detected!'  # Moderate-intensity motion
    elif motion_level > 1:
        text = '1st level motion detected!'  # Low-intensity motion
    else:
        text = 'Stable'  # No significant motion detected

    # Print the motion level category to the console
    print(text)

    # Overlay the motion level text on the original frame
    cv2.putText(img, text, (10, 30), 1, 2, (0, 255, 0), 2)  # Green text

    # Display the original frame with the motion level overlay
    cv2.imshow('Original', img)

    # Display the processed frame highlighting detected motion
    cv2.imshow('Detected', detected)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
