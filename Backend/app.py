# pylint: skip-file
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

import time
import threading


from RPi import GPIO
import spidev
from models import DS18B20, LDR, PIR, LCD, Mcp, Serial


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hier mag je om het even wat schrijven, zolang het maar geheim blijft en een string is'

socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# One Wire
# temperatuur_sensor = DS18B20('28-02119245e9af')
# DS18B20
temperatuur_sensor = DS18B20.DS18B20('28-00000bcf0c9b', socketio)
temperatuur_sensor.start()

ldr = LDR.LDR(socketio)
ldr.start()

pir = PIR.PIR(socketio)
pir.start()


lcd = LCD.LCD(22, 27, [20, 13, 26, 23, 24, 25, 12, 16])
lcd.start()
    
ser = Serial.Serial(socketio, '/dev/ttyS0', 9600)
ser.start()

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
@socketio.on('connect')
def init_connection():
    socketio.emit('temperatuur', DataRepository.get_latest_value(1))
    socketio.emit('Licht', DataRepository.get_latest_value(2))
    socketio.emit('PIR', DataRepository.get_latest_value(3))
    print('User connected')

if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')

