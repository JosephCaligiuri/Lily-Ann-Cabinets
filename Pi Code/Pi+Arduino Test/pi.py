
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2
# Imports
import serial
# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  w - Move Forward")
   print("  s - Move Backward")
   print("  a - Strafe to the left")
   print("  d - Strafe to the right")
   print("  k - Stop Motion")
   print("  r - Retrieve Arduino value")
   print("  x - exit program")
# Main
# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()
# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()

#sending commands to arduino 
while True:
   command = input("Enter command: ")
   if command == "r":  # read Arduino A0 pin value
      usb.write(b'read_a0')  # send command to Arduino
      line = usb.readline()  # read input from Arduino
      line = line.decode()  # convert type from bytes to string
      line = line.strip()  # strip extra whitespace characters
      if line.isdigit():  # check if line contains only digits
         value = int(line)  # convert type from string to int
      else:
         print("Unknown value '" + line + "', setting to 0.")
         value = 0
      print("Arduino A0 value:", value)
   elif command == "w":  
      usb.write(b'move_f')  
      print("Forward")
   elif command == "s":  
      usb.write(b'move_b')  
      print("Back")
   elif command == "a":  
      usb.write(b'move_l')  
      print("Left")
   elif command == "d": 
      usb.write(b'move_r')
      print("Right")
   elif command =="k":
      usb.write(b'stop')
      print("Stopped")
   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()