import pygame

import scratch

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Initialize RoboClaw object with appropriate serial port and baud rate


# Address of the RoboClaw controller (usually 0x80)
address = 0x80


motor_channel = 1

roboclaw = scratch.RoboClaw("COM8", 38400)  

try:
    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get joystick input
        joystick_count = pygame.joystick.get_count()
        if joystick_count > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            
            # Get joystick Y-axis value
            axis_y_value = joystick.get_axis(1)  # Assuming the Y-axis is the second axis
            
            # Map joystick input to motor speed
            speed = int(axis_y_value * 32767)  # Map joystick value (-1 to 1) to motor speed (0 to 127)

            print("speed: " + str(speed))
            print("joystick: " + str(axis_y_value))
            
            # Control motor
            roboclaw.drive_motor_duty(address, speed)
        else:
            print("Joystick not found!")
            running = False  # Stop if joystick is not found
        
        pygame.time.delay(50)  # Adjust delay as needed
        
finally:
    # Stop motor
    roboclaw.drive_motor_duty(address, 0)
    pygame.quit()  # Quit pygame
