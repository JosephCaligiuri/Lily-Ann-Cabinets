# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import os
# Create an instance of TKinter Window or frame
win = tk.Tk()

# Set the size of the window
#win.attributes('-fullscreen',True)

# Create a Label to capture the Video frames
label =tk.Label(win)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

   label.pack()

def capture():
    # Capture a frame from the video stream
    ret, frame = cap.read()

    if ret:
        # Create the /img directory if it doesn't exist
        img_dir = "img"
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        # Save the captured frame as "capture.jpg" in the /img directory
        file_path = os.path.join(img_dir, "capture.jpg")
        cv2.imwrite(file_path, frame)


show_frames()

win.bind('<f>', capture())

button = tk.Button(win, text='Stop', width=25, command=win.destroy)
button.pack()






win.mainloop()