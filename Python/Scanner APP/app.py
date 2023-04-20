import serial
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    text = "test"
    return flask.render_template("index.html", dynamic_text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)