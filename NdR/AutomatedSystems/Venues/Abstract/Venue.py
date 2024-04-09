from EventBus.Implementations.User.Implementation.UserBus             import UserBus
from EventBus.Implementations.VenueEvents.EventAdminBus import EventAdminBus
from Event.Event                    import Event


class Venue(object):
    '''
    Venues of the NdR 
    '''
    def __init__(self, 
                 name : str,
                 capacity : int,
                 userbus : UserBus,
                 ):
        self.__name      = name 
        self.__capacity  = capacity
        self.__available = capacity
        self.__userbus   = userbus
        
        self.__adminbus = None 
    
    def notifyAvailable(self, user): 
        if self.isAvailable():
            event = Event("available_venue_alt",self.__name) 
            self.__userbus.publishToBus(event, user) 
    
    def isAvailable(self):
        return self.__available > 0
    
    def getAvailable(self):
        return self.__available
        
    def addPeopleToVenue(self, no_of_people):
        prev = self.__available
        print("TICKET BOOKING...")
        print("Before: ", self.__available)
        self.__available = max(0, self.__available - no_of_people) 
        fin = self.__available
        print("After: ", self.__available)
        print() 
        
        if self.__adminbus is not None:
            joined_people = prev - fin 
            if joined_people > 0:
                event = Event("booked_tickets", {'name' : self.__name , 'demand' : joined_people})
                self.__adminbus.publishToBus(event) 
            pass 
    
    def startEvent(self, event_bus : EventAdminBus):
        self.__available = self.__capacity
        self.__adminbus  = event_bus
    
    def reset(self, params = None):
        self.__available = self.__capacity 
        self.__adminbus  = None 
    
    def getName(self):
        return self.__name
    
    def getCapacity(self):
        return self.__capacity