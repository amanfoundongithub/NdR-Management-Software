from EventBus.Implementations.Venue.VenueBus import VenueBus
from EventBus.Implementations.VenueEvents.UserNotifierBus import UserNotifierBus
from EventBus.Implementations.VenueEvents.EventAdminBus   import EventAdminBus

from Event.Event import Event

class VenueEvent(object):
    '''
    The Event being conducted at the venue
    '''
    def __init__(self, name : str, type : str, venuebus : VenueBus, userbus : UserNotifierBus):
        self.__type = type
        self.__name = name   
        self.__venuebus = venuebus
        self.__userbus  = userbus 
    
    def startEvent(self, event_bus : EventAdminBus):
        event = Event("start_event", event_bus) 
        self.__venuebus.publishToBus(event) 
         
    
    def recommendEvent(self):
        event = Event("recommend_event",{
            'name' : self.__name, 
            'type' : self.__type,
        })
        self.__userbus.publishToBus(event)
        
    
    def endEvent(self):
        event = Event("start_event", {})
        self.__venuebus.publishToBus(event) 
    
    def getType(self):
        return self.__type
    
    def getName(self):
        return self.__name 