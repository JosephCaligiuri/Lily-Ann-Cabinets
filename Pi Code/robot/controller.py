import evdev
import serial
import time
import scratch

rc = scratch.RoboClaw("/dev/ttyACM0", 38400)

address = 0x80

def get_controller_values(device):
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_ABS and event.code == 1:
            axis_value = event.value
            # Normalize axis value to range from -100 to 100
            normalized_value = axis_value


            normalized_value = int(normalized_value)


            
            if normalized_value > -20 and normalized_value < 20:
                normalized_value = 0
            

            rc.drive_motor_duty(address, normalized_value)

            print(f"Axis {event.code}: {normalized_value}")


        elif event.type == evdev.ecodes.EV_KEY:
            print(f"Button {event.code}: {event.value}")

def main():
    # Find the event device path for your controller
    # You can use 'ls /dev/input/' to list input devices and find your controller
    controller_path = '/dev/input/event3'  # Replace X with the appropriate event number
    arduino_port = '/dev/ttyACM0'  # Replace with the correct serial port for your Arduino

    try:
        device = evdev.InputDevice(controller_path)
        print(f"Connected to {device.name}")

        
        get_controller_values(device)

    except FileNotFoundError:
        print(f"Controller not found at {controller_path}")


if __name__ == "__main__":
    main()
