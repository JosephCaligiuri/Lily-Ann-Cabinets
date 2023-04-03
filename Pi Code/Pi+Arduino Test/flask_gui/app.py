from flask import Flask, Response, render_template
import cv2
import serial

# USB_PORT = "/dev/ttyACM0"

'''try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()'''

app = Flask(__name__)

def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/forward')
def forward():
    # insert your Python code here
   # usb.write(b'move_f')
    print("forward")
    result = "Forward"
    return result

@app.route('/back')
def back():
   # usb.write(b'move_b')
    print("back")
    result = "Back"
    return result

@app.route('/left')
def left():
   # usb.write(b'move_l')
    print("left")
    result = "left"
    return result

@app.route('/right')
def right():
   # usb.write(b'move_r')
    print("right")
    result = "right"
    return result

@app.route('/stop')
def stop():
   # usb.write(b'stop')
    print("stop")
    result = "Stop"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)