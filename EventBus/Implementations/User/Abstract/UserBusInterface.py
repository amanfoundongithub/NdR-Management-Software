from abc import ABC, abstractmethod

from Event.Event import Event
from NdR.Participants.User import User


class UserBusInterface(ABC):
    
    @abstractmethod
    def addToBus(self, user : User):
        pass 

    @abstractmethod
    def publishToBus(self, event : Event):
        pass