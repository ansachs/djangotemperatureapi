"""
ASGI config for temperatureapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import asyncio
import os

from django.core.asgi import get_asgi_application

from temperaturefeedconsumer.ws_temperaturedata import capture_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'temperatureapi.settings')

application = get_asgi_application()

def run_ws():
    asyncio.run(capture_data())

import threading
threading.Thread(target=run_ws).start()
