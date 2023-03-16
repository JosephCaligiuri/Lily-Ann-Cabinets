import pyautogui
from PIL import ImageGrab

# Create a loop that runs until the user presses 'q'
while True:
    # Get the current position of the cursor
    x, y = pyautogui.position()
    
    # Grab a screenshot of the screen and get the RGB value of the pixel under the cursor
    im = ImageGrab.grab()
    pixel = im.getpixel((x, y))
    print(f"Position: ({x}, {y}) RGB value: {pixel}")
    
    # Wait for the user to press a key (to allow time for the RGB value to be displayed)
    if input("Press Enter to continue or 'q' to quit...") == 'q':
        break
