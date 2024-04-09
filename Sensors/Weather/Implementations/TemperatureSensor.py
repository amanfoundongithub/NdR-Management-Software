from ..Abstract.SensorInterface  import Sensor

from EventBus.Implementations.User.Implementation.WeatherBus import WeatherBus
from Event.Event              import Event

import random 

class TemperatureSensor(Sensor):
    '''
    Temperature Sensor to record temperature
    '''
    def __init__(self,
                 weatherbus : WeatherBus):
        self.__weatherbus = weatherbus
        pass 

    def sendValues(self):
        temperature = random.choice([35, 35.3, 36, 37, 36.57, 30.22]) 
        
        event = Event("temperature", temperature)
        self.__weatherbus.publishToBus(event) 