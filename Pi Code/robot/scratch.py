import serial
import struct

def crc16(packet):
    crc = 0
    for byte in packet:
        crc = crc ^ (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
    return crc & 0xFFFF

class RoboClaw:
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(port, baudrate, timeout=1)
    
    def send_command(self, command):
        self.serial.write(command)
        self.serial.flush()
    
    def drive_motor_duty(self, address, duty):
        duty_bytes = struct.pack('>h', duty)
        command = bytes([address, 32]) + duty_bytes
        crc = crc16(command)
        crc_bytes = struct.pack('>H', crc)
        command += crc_bytes
        print("Sending command:", command)
        self.send_command(command)
    
    def close(self):
        self.serial.close()

if __name__ == "__main__":
    roboclaw = RoboClaw("COM8", 38400)  
    motor_address = 0x80  
    duty_cycle = 0  # Example duty cycle value (-32767 to +32767)

    roboclaw.drive_motor_duty(motor_address, duty_cycle)
    
    roboclaw.close()  # Close the serial connection
