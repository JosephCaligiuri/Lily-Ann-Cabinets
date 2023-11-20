import cv2
import numpy as np
import math
import serial
import time

in1 = 24
in2 = 23
en = 25
temp1 = 1

USB_PORT = '/dev/ttyACM0'

#arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

print("\n")
print("The default speed & direction of the motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

# Define the target color
target_color = np.array([0, 24, 179])

# Initialize the video stream and wait for the camera to warm up
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv2.CAP_PROP_EXPOSURE, 0)
cv2.waitKey(3000)

# PID constants
Kp = 0.06  # Proportional gain
Ki = 0.0  # Integral gain
Kd = 0.01  # Derivative gain

# Initialize PID variables
previous_error = 0
integral = 0

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

    # Resize the frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    #frame = (frame * .2).astype(np.uint8)

    # Compute the Euclidean distance to the target color for each pixel
    distances = np.sqrt(np.sum(np.square(frame - target_color), axis=2))

    # Find the pixel with the minimum distance to the target color
    min_distance = np.min(distances)
    min_distance_indices = np.argwhere(distances == min_distance)
    target_pixel = min_distance_indices[len(min_distance_indices) // 2]

    # Calculate the distance from the center of the frame to the target pixel
    center = (frame.shape[1] // 2, frame.shape[0] // 2)
    distance_to_center = np.sqrt(np.sum(np.square(center - target_pixel)))

    # Calculate the distance in pixels along the x-axis
    distance_x = target_pixel[1] - center[0]

    # Calculate the error for the PID controller
    error = distance_x

    # Use the PID controller to calculate the control signal
    control_signal = calculate_pid_control(error)

    # Map the control signal to the speed of your motor
    speed = int(control_signal)

    #arduino.write(bytes(str(speed), 'utf-8'))

    print("Distance: " + str(distance_x) + "  Speed: " + str(speed))

    # Draw a square at the center of the frame
    square_size = 10
    square_color = (0, 255, 0)
    cv2.rectangle(frame, (center[0] - square_size // 2, center[1] - square_size // 2), (center[0] + square_size // 2, center[1] + square_size // 2), square_color, 2)

    # Draw a circle at the target pixel
    cv2.circle(frame, tuple(target_pixel[::-1]), 5, (0, 0, 255), -1)

    # Display the frame with the target pixel tracked and the center square
    cv2.imshow("Frame", frame)

    #time.sleep(.01)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up the video stream and close any open windows
cap.release()
cv2.destroyAllWindows()
