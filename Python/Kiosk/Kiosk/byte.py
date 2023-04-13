import tkinter as tk
import serial
from lilyanncabinets import sheets, main
import time


USB_PORT = "COM10"


try:
    usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
    print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
    print("Exiting program.")
    exit()

while True:
    command = input("enter command: ")
    data = usb.readline().strip()

    if command == "a":
        usb.write(b'a')

    
    print(data)
   