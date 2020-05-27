# pylint: skip-file
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

import time
import threading


from RPi import GPIO
from models.DS18B20 import DS18B20

# One Wire
# temperatuur_sensor = DS18B20('28-02119245e9af')
# DS18B20
temperatuur_sensor = DS18B20('28-00000bcf0c9b')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hier mag je om het even wat schrijven, zolang het maar geheim blijft en een string is'

socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)


# API ENDPOINTS
endpoint = '/api/v1/'

@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."

@app.route(endpoint + 'componenten/')
def get_componenten():
    data = DataRepository.get_componenten()
    return jsonify(data), 200

@app.route(endpoint + 'componenten/<sensorid>/')
def get_sensor_by_sensorid(sensorid):
    data = DataRepository.get_component_by_componentid(componentid)
    return jsonify(data), 200

@app.route(endpoint + 'componenten/historiek/')
def get_historiek():
    data = DataRepository.get_componenthistoriek()
    return jsonify(data), 200

@app.route(endpoint + 'componenten/<componentid>/historiek/')
def get_history_by_componentid(componentid):
    data = DataRepository.get_componenthistory_by_componentid(componentid)
    return jsonify(data), 200


# SOCKET IO


if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')


# while True:
#     DataRepository.meting(1, temperatuur_sensor.inlezen_temp())
#     time.sleep(30)