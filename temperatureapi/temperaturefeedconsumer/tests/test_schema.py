from collections import namedtuple
from datetime import datetime
from graphene.test import Client
import pytest
from temperaturefeedconsumer.schema import schema
from temperaturefeedconsumer.models import TemperatureReading

TempDate = namedtuple('TempDate',['temperature', 'received_datetime'])

@pytest.fixture
def setup_temperature_data(db) -> list[TempDate]:
    start_date_data = TempDate(5, datetime.fromisoformat('2024-05-21T12:00:00+00:00'))
    end_date_data = TempDate(20, datetime.fromisoformat('2024-05-25T12:00:00+00:00'))
    mid_date_data = TempDate(10, datetime.fromisoformat('2024-05-23T12:00:00+00:00'))

    for temperature, received_datetime in [start_date_data, end_date_data, mid_date_data]:
        reading = TemperatureReading.objects.create(temperature=temperature,received_datetime=received_datetime)
        reading.save()
    
    return [start_date_data, mid_date_data, end_date_data]

def test_schema_temperature_statistics(setup_temperature_data):
    # setup
    latest_data = max(setup_temperature_data, key=lambda x: x.received_datetime.timestamp())
    earliest_data = min(setup_temperature_data, key=lambda x: x.received_datetime.timestamp())
    
    #act
    client = Client(schema)
    request = '''{{
        temperatureStatistics(before: "{before}", after: "{after}") {{
            max
            min
        }}
    }}'''.format(before = str(latest_data.received_datetime.isoformat()), after = str(earliest_data.received_datetime.isoformat()))
    
    executed = client.execute(request)

    #assert
    assert executed == {
        'data': {
            "temperatureStatistics": {
                "max": 20.0,
                "min": 5.0
                }
        }
    }


def test_schema_temperature_reading(setup_temperature_data):
    # setup
    latest_data = max(setup_temperature_data, key=lambda x: x.received_datetime.timestamp())
    
    #act
    client = Client(schema)
    request = '''{
        currentTemperature {
            value
            timestamp
        }
    }'''

    executed = client.execute(request)

    #assert
    assert executed == {
        'data': {
            "currentTemperature": {
                "timestamp": '2024-05-25T12:00:00+00:00',
                "value": latest_data.temperature
                }
        }
    }