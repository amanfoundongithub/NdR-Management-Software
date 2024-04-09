from abc import ABC, abstractmethod

from Event.Event import Event


class EventBusInterface(ABC):
    
    @abstractmethod
    def addToBus(self, user):
        pass 
    
    @abstractmethod
    def publishToBus(self, event : Event, name_of_user = None):
        pass  