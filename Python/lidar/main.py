import serial

# Configure the serial port
ser = serial.Serial(
    port='/dev/serial0',  # Serial port on Raspberry Pi 3
    baudrate=230400,      # Baud rate of UART device
    timeout=1             # Timeout in seconds
)

# Read and print data
while True:
    data = ser.read()

    decoded_data = data.decode('utf-8', errors='ignore')
    for byte_data in data:
        byte_value = bytes([byte_data])  # Convert integer to byte object
        print(byte_value.hex())
