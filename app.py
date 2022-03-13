import random

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@ app.route('/fdk300')
def fdk300():
    sensor_data = {'temperature': random.randint(10,100)}
    return jsonify(sensor_data), 200


@ app.route('/fdk400')
def fdk400():
    sensor_data = {'pressure_S': 0, 'pressure_D': 0}
    sensor_data['pressure_S'] = random.randint(10,100)
    sensor_data['pressure_D'] = random.randint(10,100)
    return jsonify(sensor_data), 200


@ app.route('/mtka1')
def mtka1():
    sensor_data = {'weight': 0}
    sensor_data['weight'] = random.randint(10,100)
    return jsonify(sensor_data), 200


@ app.route('/m170')
def m170():
    sensor_data = {'oxygen': 0, 'pulse': 0}
    sensor_data['oxygen'] = random.randint(10,100)
    sensor_data['pulse'] = random.randint(10,100)
    return jsonify(sensor_data), 200


@ app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(host='127.0.0.1', debug=True, port=5000)
