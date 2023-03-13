import cv2
import numpy as np

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer_model.xml')

# Set the font and text color for displaying the name of the recognized person
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)

# Open the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # For each face detected, perform face recognition
    for (x, y, w, h) in faces:
        # Extract the face region of interest (ROI)
        face_roi = gray[y:y+h, x:x+w]

        # Perform face recognition on the ROI
        label, confidence = face_recognizer.predict(face_roi)

        # If the confidence is below a threshold, display the name of the recognized person
        if confidence < 100:
            name = "Your Name"
            cv2.putText(frame, name, (x, y-10), font, 1, text_color, 2)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the video stream with face detection and recognition
    cv2.imshow('Face Recognition', frame)

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
