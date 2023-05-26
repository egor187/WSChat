'esversion: 6'

const sio = io();

sio.on('connect', (sid, environ) => {console.log('connected')});
sio.on('disconnect', () => {console.log('disconnected')});
sio.on('users_count', (count) => {console.log('There are ' + count.count + ' users')}); // notificate all users except new one


// link to chat room => sio.emit() messaging
