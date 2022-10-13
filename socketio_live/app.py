import eventlet
import socketio
from random import randint

sio = socketio.Server(cors_allowed_origins="*", async_mode='eventlet')
app = socketio.WSGIApp(sio)    

def ping_in_intervals():
    while True:
        sio.emit('randomData', randint(0,9999))
        sio.sleep(5)

@sio.on('connect')
def ping(*args):
    sio.emit('connect', 'connected')

@sio.on('disconnect')
def ping(*args):
    sio.emit('disconnect', 'disconnected')

thread = sio.start_background_task(ping_in_intervals)
eventlet.wsgi.server(eventlet.listen(('', 445)), app)