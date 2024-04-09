from EventBus.Abstract.EventBusInterface import EventBusInterface
from NdR.AutomatedSystems.ParkingLots.Abstract.ParkingLot import ParkingLot
from Event.Event    import Event


class ParkingLotBus(EventBusInterface):
    def __init__(self):
        
        self.__users = {}
        self.__bus   = {}
        
        # Subscribe all the events 
        self.__bus['find_available_lot'] = ParkingLot.notifyAvailable
        self.__bus['add_vehicles'] = ParkingLot.addVehicles
        self.__bus['remove_vehicles'] = ParkingLot.removeVehicles
    
    def addToBus(self, user : ParkingLot):
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
                