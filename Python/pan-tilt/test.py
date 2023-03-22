
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

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()

#sending commands to arduino 
while True:
   command = input("Enter command: ")
   if command == "r":  # read Arduino A0 pin value
      print("tet")
   elif command == "w":  
      
      print("Forward")
   elif command == "s":  
      
      print("Back")
   elif command == "a":  
      
      print("Left")
   elif command == "d": 
      
      print("Right")
   elif command =="k":
      
      print("Stopped")
   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()