import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# Loop to continuously capture frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
