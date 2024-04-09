from ..Abstract.SensorInterface import Sensor

from EventBus.Implementations.User.Implementation.WeatherBus import WeatherBus
from Event.Event              import Event
import random 

class HumiditySensor(Sensor):
    '''
    Humidity Sensor to record humidity
    '''
    def __init__(self,
                 weatherbus : WeatherBus):
        self.__weatherbus = weatherbus
        pass 

    def sendValues(self):
        humidity = random.choice([2, 4, 10.7, 1.33, 0.445, 8.556]) 
        
        event = Event("humidity", humidity)
        self.__weatherbus.publishToBus(event) 