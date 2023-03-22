import sys

sys.path.append('./')

from servo import Servo
from time import sleep

pan = Servo(pin=13)
tilt = Servo(pin=12)

while True:

    val = int(input("In: "))
   
    #pan.set_angle(val)
    tilt.set_angle(val)
    
    if val == 1:
        break
    
        