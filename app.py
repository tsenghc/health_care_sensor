import datetime
import sqlite3

import requests
from flask import Flask, jsonify, render_template, request
from fdk300 import FDK300
from fdk400 import FDK400
from m170 import M170
app = Flask(__name__)
con = sqlite3.connect('check_log.db', check_same_thread=False)
fdk300 = FDK300("C6:05:04:07:4D:54")


@app.route('/add_present_user', methods=['POST'])
def add_present_user():
    res = request.json
    user_id = res.get('user_id')
    user_name = res.get('user_name')
    temperature = res.get('temperature')
    cur = con.cursor()
    update_time = datetime.datetime.now().isoformat()
    query_string = f'''
    INSERT INTO record ( user_id, user_name,temperature, update_time )
    VALUES('{user_id}','{user_name}','{temperature}','{update_time}')'''
    cur.execute(query_string)
    con.commit()
    return jsonify({"status": user_id}), 200


@app.route('/present_user')
def present_user():
    cur = con.cursor()
    query_string = '''
    SELECT user_id,user_name,temperature FROM "record"
    WHERE DATETIME(record.update_time)>DATETIME('now','-5 second' , 'localtime')
    ORDER BY record.update_time DESC
    LIMIT 1'''
    out = {'user_id': '', 'user_name': 'wait', 'temperature': 0}
    for i in cur.execute(query_string):
        out = {'user_id': i[0], 'user_name': i[1], 'temperature': i[2]}
    return jsonify(out), 200


@ app.route('/temperature')
def temperature():
    out = {'temperature': ""}
    for i in range(10):
        temperature = fdk300.get_temperature()
        out = {'temperature': temperature}
        print(out)
        return jsonify(out), 200


@ app.route('/finger')
def finger():
    m170 = M170()
    out = m170.get_sensor_data()
    print(out)
    return jsonify(out), 200


@ app.route('/pressure')
def pressure():
    fdk400 = FDK400()
    pressure = fdk400.get_sensor_data()
    print(pressure)

    return jsonify(pressure), 200


@ app.route('/')
def index():
    return render_template('index.html')


@ app.route('/history')
def history():
    return render_template('history.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True, threaded=True)
