from EventBus.User.UserBus import UserBus
from EventBus.Event import Event



class ParkingLot(object):
    '''
    Parking Lot Base Class 
    '''
    def __init__(self, 
                 name : str,
                 capacity : int,
                 userbus : UserBus,):
        self.__name      = name 
        self.__capacity  = capacity
        self.__available = capacity
        self.__userbus   = userbus 
    
    def notifyAvailable(self, user): 
        if self.__available > 0:
            event = Event("available_lot_alt",self.__name) 
            self.__userbus.publishToBus(event, user) 
    
    def addVehicles(self, demand : int):
        previous = self.__available
        
        self.__available = max(0, self.__available - demand) 
        
        print("\nCAR PARKING AT " + self.__name + "\nPrevious: " 
              + str(previous) + " Now:" + str(self.__available), 
              end = '\n\n')
        return 

    def removeVehicles(self, demand : int):
        previous = self.__available
        
        self.__available = min(self.__capacity, self.__available + demand) 
        
        print("\nCAR REMOVAL AT " + self.__name + "\nPrevious: " 
              + str(previous) + " Now:" + str(self.__available), 
              end = '\n\n') 
    
    def isAvailable(self):
        return self.__available > 0
    
    def getCapacity(self):
        return self.__capacity

    def getName(self):
        return self.__name