from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
from dynamicqrauth import tokengen, createbase64QR
import time

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@socketio.on('connect', namespace='/getqr')
def test_connect():
    print('Client Connected')
        

@socketio.on('sendqr', namespace='/getqr')
def sendqr(sendqr):
    print("Number of pings: "+ str(sendqr))
    url = "https://attandance-app.herokuapp.com/getattendance"
    token = tokengen(url)
    qr = createbase64QR(url, token)
    emit('base64qr', qr, namespace='/getqr')


@socketio.on('disconnect', namespace='/getqr')
def test_disconnect():
    print('Client disconnected')

# if __name__ == '__main__':
#     socketio.run(app)