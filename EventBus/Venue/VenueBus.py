from NdR.AutomatedSystems.Venues.Abstract.Venue import Venue
from ..Event    import Event


class VenueBus(object):
    def __init__(self):
        
        self.__users = {}
        self.__bus   = {}
        
        # Subscribe all the events 
        self.__bus['find_available_venue'] = Venue.notifyAvailable
        
        self.__bus['start_event']          = Venue.startEvent
        self.__bus['end_event']            = Venue.reset
        
        self.__bus['add_people']           = Venue.addPeopleToVenue
    
    def addToBus(self, user : Venue):
        if user.getName() not in self.__users:
            self.__users[user.getName()] = user 
    
    def publishToBus(self, event : Event, name_of_venue = None):
        name = event.getName() 
        if name not in self.__bus: 
            return 
        
        if name_of_venue is None: 
            for user in self.__users:
                self.__bus[name](self.__users[user], event.getData())
        else: 
            if name_of_venue in self.__users:
                self.__bus[name](self.__users[name_of_venue], 
                                 event.getData())
                