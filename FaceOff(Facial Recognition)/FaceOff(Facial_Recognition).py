import cv2

# Load the Haar cascade classifier for facial detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)


while True:
    
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Change the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20, minSize=(30, 30))

    # Create structures around the faces to show identification
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Check if two faces are detected and capture the frame
    if len(faces) >= 2:
        # Show the cropped second registered face 
        face_x, face_y, face_w, face_h = faces[1]
        face_roi = frame[face_y:face_y + face_h, face_x:face_x + face_w]
        face_roi = cv2.resize(face_roi, (300, 300))
        frame[:300, :300] = face_roi
        cv2.imwrite('two_faces_detected.jpg', frame)
        print("Two faces detected! Image captured.")
        break
    # Mirror the framing
    mirrored_frame = cv2.flip(frame, 1)

    # Display the mirrored frame
    cv2.imshow('Mirrored Webcam', mirrored_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close window
cap.release()
cv2.destroyAllWindows()
