import tkinter as tk
from serial import Serial
from lilyanncabinets import sheets, main
import time


sheets.createNewSheet()


ser = Serial('COM10', 9600)  # Open serial port at 9600 baud.

def a():
    text_widget.delete("1.0", tk.END)
    ser.write(b'1')
    data = ser.readline().strip()
    text_widget.insert(tk.END, data)

    sheets.writeToSheet(2, 1, str(data))    
    
    

def b():
    text_widget.delete("1.0", tk.END)
    ser.write(b'2')
    data = ser.readline().strip()
    text_widget.insert(tk.END, data)

def c():
    text_widget.delete("1.0", tk.END)
    ser.write(b'4')
    data = ser.readline().strip()
    text_widget.insert(tk.END, data)

# Create the window
root = tk.Tk()
root.title("Text Window Example")

# Create the Text widget
text_widget = tk.Text(root, height=10, width=30)
text_widget.pack()

# Create the buttons
button1 = tk.Button(root, text="Block 1", command=a)
button1.pack(side=tk.LEFT)

button2 = tk.Button(root, text="Block 2", command=b)
button2.pack(side=tk.LEFT)

button3 = tk.Button(root, text="Block 4", command=c)
button3.pack(side=tk.LEFT)

# Start the main event loop
root.mainloop()
