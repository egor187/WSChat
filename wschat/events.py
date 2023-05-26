import socketio


sio = socketio.Server(async_mode='eventlet', engineio_logger=True)
users_count = 0


@sio.event
def connect(sid, environ):
    global users_count
    users_count += 1
    sio.emit('users_count', users_count)


@sio.event
def disconnect(sid):
    print('Disconnect', sid)
