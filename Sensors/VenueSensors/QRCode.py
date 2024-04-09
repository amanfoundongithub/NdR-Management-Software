from NdR.AutomatedSystems.Venues.Abstract.Venue import Venue

from EventBus.Implementations.User.UserBus   import UserBus
from EventBus.Implementations.Venue.VenueBus import VenueBus
from Event.Event import Event

class QRCode(object):
    '''
    QR Code object of the Venue 
    '''
    def __init__(self, 
                 venue : Venue,
                 userbus : UserBus,
                 venuebus : VenueBus):
        self.__venue     = venue
        self.__userbus   = userbus
        self.__venuebus  = venuebus
        pass 
    
    def checkAvailability(self, user : str):
        '''
        Sends the details regarding the availability of the venue to the User
        '''
        if self.__venue.isAvailable():
            event = Event("available_venue", self.__venue.getName())
            self.__userbus.publishToBus(event,user)
            pass
        else: 
            event = Event("find_available_venue", user)
            self.__venuebus.publishToBus(event) 
            pass
    
    