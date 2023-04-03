import pigpio

from time import sleep
pi = pigpio.pi()
servo = pi.set_mode(12, pi.p)
val = -1

try:
    
    while True:
        servo.value = val
        sleep(0.1)
        val = val + 0.01
        if val > 1:
            val = -1
except KeyboardInterrupt:
	print("Program stopped")