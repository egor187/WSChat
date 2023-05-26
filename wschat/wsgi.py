"""
WSGI config for wschat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wschat.settings')
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())

from wschat.events import sio
import socketio

application = socketio.WSGIApp(sio, application)

import eventlet.wsgi
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), application)
