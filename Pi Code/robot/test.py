import RPi.GPIO as GPIO
import time

# Define pin numbers
cw_ccw_pin = 27  # GPIO 27 for CW/CCW control
pwm_pin = 22     # GPIO 22 for PWM control

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(cw_ccw_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(pwm_pin, 10000)  # 10000 Hz frequency
pwm.start(0)  # Start with 0% duty cycle

# Control the motor
GPIO.output(cw_ccw_pin, GPIO.LOW)  # Set direction (HIGH for clockwise)
pwm.ChangeDutyCycle(1)  # Set speed (50% duty cycle)

# Run the motor for 5 seconds
time.sleep(5)

# Cleanup
pwm.stop()
GPIO.cleanup()