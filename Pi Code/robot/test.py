import evdev
import serial
import time

def get_controller_values(device, arduino):
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            axis_value = event.value
            # Normalize axis value to range from -100 to 100
            normalized_value = (axis_value - 127) / 127.0 * 100.0
            print(f"Axis {event.code}: {normalized_value}")
            # Send the normalized value over serial to Arduino
            arduino.write(bytes(str(normalized_value), 'utf-8'))
        elif event.type == evdev.ecodes.EV_KEY:
            print(f"Button {event.code}: {event.value}")

def main():
    controller_path = '/dev/input/event0'  # Replace X with the appropriate event number
    arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
    try:
        device = evdev.InputDevice(controller_path)
        print(f"Connected to {device.name}")

        
        time.sleep(2)  # Allow time for Arduino to initialize

        get_controller_values(device, arduino)

    except FileNotFoundError:
        print(f"Controller not found at {controller_path}")
    except serial.SerialException:
        print(f"Arduino not found at {arduino}")
    finally:
        if 'ser' in locals() and arduino.is_open:
            arduino.close()

if __name__ == "__main__":
    main()
