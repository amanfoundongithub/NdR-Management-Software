from NdR.VenueEvent.EventAdmin import EventAdmin
from ..Event    import Event

class EventAdminBus(object):
    
    def __init__(self):
        
        self.__EventAdmins = {}
        self.__bus   = {}
        
        # Subscribe all the events 
        self.__bus['booked_tickets'] = EventAdmin.getVenueUpdate
        
    
    def addToBus(self, eventAdmin : EventAdmin):
        if eventAdmin.getName() not in self.__EventAdmins:
            self.__EventAdmins[eventAdmin.getName()] = eventAdmin
    
    def publishToBus(self, event : Event, name_of_EventAdmin = None): 
        name = event.getName() 
        if name not in self.__bus: 
            return 
        
        if name_of_EventAdmin is None: 
            for eventAdmin in self.__EventAdmins:
                self.__bus[name](self.__EventAdmins[eventAdmin], event.getData())
        else: 
            if name_of_EventAdmin in self.__EventAdmins:
                self.__bus[name](self.__EventAdmins[name_of_EventAdmin], 
                                 event.getData())
    