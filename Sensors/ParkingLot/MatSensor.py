from NdR.AutomatedSystems.ParkingLots.Abstract.ParkingLot import ParkingLot

from EventBus.Implementations.User.UserBus   import UserBus
from EventBus.Implementations.ParkingLot.ParkingLotBus import ParkingLotBus
from Event.Event import Event

import random 

class ParkingMatSensor(object):
    '''
    Parking Mat sensor counts number of cars 
    '''
    def __init__(self, parkingLot : ParkingLot,
                 userbus : UserBus,
                 parkbus : ParkingLotBus):
        self.__parkingLot = parkingLot
        self.__userbus   = userbus
        self.__parkbus  = parkbus
        pass 
    
    def checkAvailable(self, user):
        if self.__parkingLot.isAvailable():
            event = Event("available_lot", self.__parkingLot.getName())
            self.__userbus.publishToBus(event,user)
            pass
        else: 
            event = Event("find_available_lot", user)
            self.__parkbus.publishToBus(event) 
            pass
    
    def sendValues(self):
        demand = random.choice([ 35, 4,])
        
        if demand == 0:
            return 
        elif demand > 0:
            # More cars came up 
            event = Event('add_vehicles', demand)
            self.__parkbus.publishToBus(event, self.__parkingLot.getName()) 
        else:
            event = Event('remove_vehicles', -demand)
            self.__parkbus.publishToBus(event, self.__parkingLot.getName())
    