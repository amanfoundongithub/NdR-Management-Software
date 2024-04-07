from EventBus.User.UserBus import UserBus
from EventBus.Event import Event


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
    
    def notifyAvailable(self, user): 
        if self.isAvailable():
            event = Event("available_venue_alt",self.__name) 
            self.__userbus.publishToBus(event, user) 
    
    def isAvailable(self):
        return self.__available > 0
    
    def getAvailable(self):
        return self.__available
    
    def addPeopleToVenue(self, no_of_people):
        print("TICKET BOOKING...")
        print("Before: ", self.__available)
        self.__available = max(0, self.__available - no_of_people) 
        print("After: ", self.__available)
        print() 
    
    def reset(self, params = None):
        self.__available = self.__capacity 
    
    def getName(self):
        return self.__name
    
    def getCapacity(self):
        return self.__capacity