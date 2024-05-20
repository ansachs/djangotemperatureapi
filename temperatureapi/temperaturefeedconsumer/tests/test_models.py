

from temperaturefeedconsumer.models import TemperatureReading
from django.utils import timezone

def test_create_temperature_reading(db):
    reading = TemperatureReading.objects.create(temperature=5.34543543,received_datetime=timezone.now())
    reading.save()
    readings = TemperatureReading.objects.all()
    assert len(readings) == 1