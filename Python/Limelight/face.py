import cv2
import math

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video capture device (0 for the default camera)
cap = cv2.VideoCapture(0)

# Set the desired frame width and height for lower resolution
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Calculate the center of the face
        face_center_x = x + w // 2

        # Calculate the center of the frame
        frame_center_x = frame.shape[1] // 2

        # Calculate the horizontal distance (X-axis) between the face center and frame center
        distance_x = frame_center_x - face_center_x

        # Print the distance to the terminal
        print(f"X Distance: {distance_x}")

    # Display the frame with the detected face(s)
    cv2.imshow('Face Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
