import cv2
import math
import serial
import time

in1 = 24
in2 = 23
en = 25
temp1 = 1

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

print("\n")
print("The default speed & direction of the motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video stream and wait for the camera to warm up
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# PID constants
Kp = 0.04  # Proportional gain
Ki = 0.0   # Integral gain
Kd = 0.02  # Derivative gain

# Initialize PID variables
previous_error = 0
integral = 0

# Time variables
last_face_detected_time = time.time()

# Initialize distance_x variable
distance_x = 0

def calculate_pid_control(error):
    global previous_error, integral

    # Proportional term
    P = Kp * error

    # Integral term
    integral += error
    I = Ki * integral

    # Derivative term
    D = Kd * (error - previous_error)

    # Calculate the control signal
    control = P + I + D

    control = max(min(control, 100), -100)
    # Update previous error for the next iteration
    previous_error = error

    return control

# Start looping over frames from the video stream
while True:
    # Grab the current frame from the video stream
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # A face is detected, reset the timer
        last_face_detected_time = time.time()

    # Check if more than 500ms have passed without detecting a face
    if time.time() - last_face_detected_time > 0.2:
        speed = 0
    else:
        for (x, y, w, h) in faces:
            # Calculate the center of the face
            face_center_x = x + w // 2

            # Calculate the center of the frame
            frame_center_x = frame.shape[1] // 2

            # Calculate the horizontal distance (X-axis) between the face center and frame center
            distance_x = frame_center_x - face_center_x

            # Calculate the error for the PID controller
            error = distance_x

            # Use the PID controller to calculate the control signal
            control_signal = calculate_pid_control(error)

            # Map the control signal to the speed of your motor
            speed = int(control_signal) * -1

    arduino.write(bytes(str(speed), 'utf-8'))

    print("X Distance: " + str(distance_x) + "  Speed: " + str(speed))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Print to the terminal that a face is detected
        print("Face Detected!")

    # Display the frame with the detected face(s)
    cv2.imshow("Face Detection", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up the video stream and close any open windows
cap.release()
cv2.destroyAllWindows()
