from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    An interface for implementation of the sensors
    """
    @abstractmethod
    def sendValues(self):
        pass 