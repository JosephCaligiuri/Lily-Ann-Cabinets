import serial
import flask

app = flask.Flask(__name__)

@app.before_first_request
def readUSB():
    usb = serial.Serial("\\\\.\\COM10", 9600)
    data = usb.readline().strip()
    return data

@app.route("/")
def index():
    text = readUSB()
    return flask.render_template("index.html", dynamic_text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)