from flask import Flask, request

app = Flask(__name__)

@app.route('/joystick', methods=['POST'])
def joystick():
    data = request.get_json()
    joystick_x = data['x']
    joystick_y = data['y']
    print('Joystick coordinates: ({}, {})'.format(joystick_x, joystick_y))
    return 'OK'

if __name__ == '__main__':
    app.run()
