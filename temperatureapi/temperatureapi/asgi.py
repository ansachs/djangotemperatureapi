"""
ASGI config for temperatureapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import asyncio
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'temperatureapi.settings')
django.setup()

from django.core.asgi import get_asgi_application
import threading
from temperaturefeedconsumer.ws_temperaturedata import capture_data

application = get_asgi_application()

def run_ws():
    asyncio.run(capture_data())


threading.Thread(target=run_ws).start()
