import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT) # Front Left
GPIO.setup(27, GPIO.OUT)

GPIO.setup(24, GPIO.OUT) # Front Right
GPIO.setup(23, GPIO.OUT)

GPIO.setup(26, GPIO.OUT) # Back Left 
GPIO.setup(19, GPIO.OUT)

GPIO.setup(21, GPIO.OUT) # Back Right
GPIO.setup(20, GPIO.OUT)



try:
    while 1:

        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)

        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)

        GPIO.output(26, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)

        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO