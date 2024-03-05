
from roboclaw import Roboclaw

# Initialize RoboClaw object with appropriate serial port and baud rate
roboclaw = Roboclaw("COM8",38400)  # Adjust serial port and baud rate as needed

# Address of the RoboClaw controller (usually 0x80)
address = 0x80

# Open serial port
roboclaw.Open()

# Define duty cycle (-32767 to 32767, where -32767 represents -100% duty and 32767 represents +100% duty)
duty_cycle = 20000  # Example duty cycle value

# Drive M1 with duty cycle
success = roboclaw.drive_motor_m1(address, duty_cycle)

if success:
    print("M1 driven successfully with duty cycle:", duty_cycle)
else:
    print("Failed to drive M1 with duty cycle:", duty_cycle)
