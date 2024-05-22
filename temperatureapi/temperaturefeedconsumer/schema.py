import graphene
from graphene_django import DjangoListField, DjangoObjectType

from temperaturefeedconsumer.models import TemperatureReading

class TemperatureReadingType(graphene.ObjectType):
    value = graphene.Float()
    timestamp = graphene.DateTime()

    def resolve_value(self, info) -> float:
        return self.temperature
    
    def resolve_timestamp(self, info) -> float:
        return self.received_datetime

class TemperatureStatisticsType(graphene.ObjectType):
    min = graphene.Float()
    max = graphene.Float()

    def resolve_min(self, info) -> float:
        result = min(self, key=lambda x: x.temperature)
        return result.temperature
    
    def resolve_max(self, info)-> float:
        result = max(self, key=lambda x: x.temperature)
        return result.temperature


class Query(graphene.ObjectType):
    currentTemperature = graphene.Field(TemperatureReadingType)
    temperatureStatistics = graphene.Field(TemperatureStatisticsType, after=graphene.DateTime(required=True), before=graphene.DateTime(required=True))

    def resolve_currentTemperature(root, info) ->TemperatureReading:
        return TemperatureReading.objects.latest('received_datetime')
    
    def resolve_temperatureStatistics(root, info, after, before) ->TemperatureReading:
        result = TemperatureReading.objects.filter(received_datetime__range=[after, before])
        return result
    

schema = graphene.Schema(query=Query)