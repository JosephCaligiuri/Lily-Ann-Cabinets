import cv2
import numpy as np
import math
import serial
import time
import RPi.GPIO as GPIO          

in1 = 24
in2 = 23
en = 25
temp1=1

USB_PORT = '/dev/ttyACM0'

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    


'''try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit() '''



# Define the target color
target_color = np.array([115, 211, 165])

# Initialize the video stream and wait for the camera to warm up
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
cv2.waitKey(3000)

def s_equation(x): #slow decrease equation
    e = math.e
    return 1-math.pow(e, -0.005 * x)
def f_equation(x):
    e = math.e
    return 0.04 * math.pow(e, 0.01 * x) #fast decrease equation


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

    switch = "fast"

    state = "c"

    if switch == "slow":
        speed = s_equation(abs(distance_x))
    if switch == "fast":
        speed = f_equation(abs(distance_x))
    else:
        speed = 0



    if distance_x > 20:
        print("positive")
        state = "p"
        speed = speed
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        #usb.write(b'p')
    elif distance_x < -20:
        print("negitave")
        state = "n"
        speed = speed * -1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH )
        temp1=1
        #usb.write(b'n')   
    else:
        print("center")
        state = "c"
        speed = 0
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        #usb.write(b'c')

    #line = usb.readline().decode().strip()
    #print(line)

    print("Distance:" + str(distance_x) + "Speed:" + str(speed) + "state:" + str(state))

    
    #line = usb.readline().decode().strip()
   ## print(line)
    #temp = str(speed)
    #bDist = temp.encode('ascii')
   # print(bDist)
    #usb.write(bDist)
    
    

    # Draw a square at the center of the frame
    square_size = 10
    square_color = (0, 255, 0)
    cv2.rectangle(frame, (center[0] - square_size // 2, center[1] - square_size // 2), (center[0] + square_size // 2, center[1] + square_size // 2), square_color, 2)

    # Display the frame with the target pixel tracked and the center square
    cv2.imshow("Frame", frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

# Clean up the video stream and close any open windows

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
cap.release()
cv2.destroyAllWindows()
#usb.close()