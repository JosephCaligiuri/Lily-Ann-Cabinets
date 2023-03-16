import cv2
import numpy as np

# Load the pre-trained face detector model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_recognizer.yml')

# Create a window to display the camera feed
cv2.namedWindow('Live Facial Recognition', cv2.WINDOW_NORMAL)

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Loop over each detected face
    for (x, y, w, h) in faces:
        # Extract the face region of interest (ROI)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Use the face recognition model to predict the ID of the person
        id_, confidence = recognizer.predict(roi_gray)

        # Draw a rectangle around the face
        color = (255, 0, 0) # blue
        thickness = 2
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness)

        # Display the ID of the person and their confidence score
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = f'Unknown'+ str(confidence)
        if confidence < 140:
            name = f'Person {id_}'
        cv2.putText(frame, name, (x+5, y-5), font, 1, color, thickness, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Live Facial Recognition', frame)

    # Wait for a key press and check if it is the "q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()