import cv2
import numpy as np

# Define the color range you want to track (in BGR format)
lower_color = np.array([180, 180, 120])
upper_color = np.array([255, 255, 255])

# Create a VideoCapture object (0 for default camera or a video file path)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Create a mask to isolate the pixels in the specified color range
    mask = cv2.inRange(frame, lower_color, upper_color)

    # Apply the mask to the frame to display only the pixels within the range
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the result
    cv2.imshow("Color Tracking", result)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
