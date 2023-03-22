from flask import Flask, Response, render_template
import cv2

from servo import Servo

pan = Servo(pin=13)
tilt = Servo(pin=12)

p = 0
t = 0

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

    print("forward")
    t = t - 10
    result = "Forward"
    return result

@app.route('/back')
def back():
    
    print("back")
    t = t + 10
    result = "Back"
    return result

@app.route('/left')
def left():
    
    print("left")
    p = p + 10
    result = "left"
    return result

@app.route('/right')
def right():
    
    print("right")
    p = p - 10
    result = "right"
    return result

@app.route('/stop')
def stop():
    
    print("stop")
    result = "Stop"
    return result

pan.set_angle(p)
tilt.set_angle(t)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)