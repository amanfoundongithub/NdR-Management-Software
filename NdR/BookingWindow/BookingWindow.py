from EventBus.Implementations.Venue.VenueBus import VenueBus
from Event.Event          import Event 

class BookingWindow(object):
   """
   An instance of Booking Window for the NdR
   """ 
   def __init__(self, 
                venuebus : VenueBus,
                name_venue : str):
       self.__venue = name_venue 
       self.__venuebus = venuebus
    
   def bookTickets(self, demand):
       event = Event("add_people", demand) 
       self.__venuebus.publishToBus(event, self.__venue) 
       
    
   
   