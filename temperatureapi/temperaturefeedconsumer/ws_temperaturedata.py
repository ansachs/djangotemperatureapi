import asyncio
import json
import websockets

from django.utils import timezone
from temperaturefeedconsumer.models import TemperatureReading


def process_msg(data):
    # print(data['payload']['data']['temperature'])
    reading = TemperatureReading.objects.create(temperature=data['payload']['data']['temperature'] , received_datetime=timezone.now())
    reading.save()
    

async def capture_data():
    uri = "ws://localhost:1000/graphql"
    start = {
        "type": "start",
        "payload": {"query": "subscription { temperature }"}
    }
    async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data = await websocket.recv()
            await asyncio.to_thread(process_msg, json.loads(data))