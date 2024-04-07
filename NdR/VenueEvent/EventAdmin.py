from .VenueEvent import VenueEvent


class EventAdmin(object):
    def __init__(self, name : str, event : VenueEvent):
        self.__name = name 
        self.__event = event 
    
    def getName(self):
        return self.__name