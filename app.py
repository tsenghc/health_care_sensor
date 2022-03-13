from flask import Flask, jsonify, render_template

from fdk300 import FDK300
from fdk400 import FDK400
from m170 import M170
from mtk_a1 import MTKA1

app = Flask(__name__)


@ app.route('/fdk300')
def fdk300():
    fdk300 = FDK300()
    _temp = fdk300.get_sensor_data()
    sensor_data = {'temperature': _temp['temperature']}
    return jsonify(sensor_data), 200


@ app.route('/fdk400')
def fdk400():
    fdk400 = FDK400()
    _temp = fdk400.get_sensor_data()
    sensor_data = {'pressure_S': 0, 'pressure_D': 0}
    sensor_data['pressure_S'] = _temp['pressure_S']
    sensor_data['pressure_D'] = _temp['pressure_D']
    return jsonify(sensor_data), 200


@ app.route('/mtka1')
def mtka1():
    scale = MTKA1()
    sensor_data = {'weight': 0}
    _temp = scale.get_sensor_data()
    sensor_data['weight'] = _temp['weight']
    return jsonify(sensor_data), 200


@ app.route('/m170')
def m170():
    m170 = M170()
    sensor_data = {'oxygen': 0, 'pulse': 0}
    _temp = m170.get_sensor_data()
    sensor_data['oxygen'] = _temp['oxygen']
    sensor_data['pulse'] = _temp['pulse']
    return jsonify(sensor_data), 200


@ app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True, threaded=True)
