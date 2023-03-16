import cv2
import numpy as np

import serial

USB_PORT = '/dev/ttyACM0'

#'''
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit() 

#'''

# Define the target color
target_color = np.array([115, 211, 165])

# Initialize the video stream and wait for the camera to warm up
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 5)
cv2.waitKey(3000)

# Start looping over frames from the video stream
while True:
    # Grab the current frame from the video stream
    ret, frame = cap.read()

    # Resize the frame for faster processing
    frame = cv2.resize(frame, (640, 480))

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

    # Draw a circle and centroid on the frame at the location of the target pixel, and print its RGB value and distances
    cv2.circle(frame, tuple(target_pixel[::-1]), 5, (0, 0, 255), -1)
    pixel = frame[target_pixel[0], target_pixel[1]]
   # print(f"RGB value: {pixel}, distance to center: {distance_to_center:.2f}, distance on x-axis: {distance_x:.2f}")



    if distance_x > 0:
        print("positive")
        usb.write(b'p')
    elif distance_x < 0:
        print("negitave")
        usb.write(b'n')    

    #line = usb.readline().decode().strip()
    #print(line)

    '''
    #line = usb.readline().decode().strip()
    #print(line)
    temp = str(distance_x)
    bDist = temp.encode('ascii')
    print(bDist)
    usb.write(bDist)

    '''
    

    # Draw a square at the center of the frame
    square_size = 50
    square_color = (0, 255, 0)
    cv2.rectangle(frame, (center[0] - square_size // 2, center[1] - square_size // 2), (center[0] + square_size // 2, center[1] + square_size // 2), square_color, 2)

    # Display the frame with the target pixel tracked and the center square
    cv2.imshow("Frame", frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up the video stream and close any open windows
cap.release()
cv2.destroyAllWindows()
usb.close()
