from Sensors.ParkingLot.MatSensor                      import ParkingMatSensor

from Sensors.VenueSensors.QRCode                       import QRCode

from Sensors.Weather.Implementations.TemperatureSensor import TemperatureSensor
from Sensors.Weather.Implementations.HumiditySensor    import HumiditySensor

from NdR.AccessibilityService.AccessibilityService  import AccessibilityService

from NdR.AutomatedSystems.ParkingLots.Implementations.ParkingLotA import ParkingLotA
from NdR.AutomatedSystems.ParkingLots.Implementations.ParkingLotB import ParkingLotB

from NdR.AutomatedSystems.Venues.Implementations.VenueA import VenueA
from NdR.AutomatedSystems.Venues.Implementations.VenueB import VenueB
from NdR.AutomatedSystems.Venues.Implementations.VenueC import VenueC

from NdR.Participants.Visitor import Visitor

from NdR.VenueEvent.VenueEvent import VenueEvent
from NdR.VenueEvent.EventAdmin import EventAdmin

from NdR.BookingWindow.BookingWindow import BookingWindow

from EventBus.Implementations.User.UserBus                              import UserBus
from EventBus.Implementations.Venue.VenueBus                            import VenueBus
from EventBus.Implementations.ParkingLot.ParkingLotBus                  import ParkingLotBus
from EventBus.Implementations.User.WeatherBus                        import WeatherBus
from EventBus.Implementations.VenueEvents.UserNotifierBus                import UserNotifierBus
from EventBus.Implementations.User.AccessibilityServiceBus import AccessibilityBus
from EventBus.Implementations.VenueEvents.EventAdminBus                  import EventAdminBus

import random 
import time 

# Initialize Event Buses to communicate with the system  
userEventBus    = UserBus() 
usernotifierBus = UserNotifierBus() 
venueEventBus   = VenueBus() 
parkingLotBus   = ParkingLotBus() 
weatherBus      = WeatherBus() 
acBus           = AccessibilityBus() 

# Initialize Sensors of temperature and humidity for the users 
tempSensor = TemperatureSensor(
    weatherbus = weatherBus
)
humSensor  = HumiditySensor(
    weatherbus = weatherBus
)

# Initialize the Parking Lots and the Parking Mat Sensors 
parkingLotA = ParkingLotA(userbus = userEventBus)
parkingLotBus.addToBus(parkingLotA)

parkingMatSensorA = ParkingMatSensor(parkingLot = parkingLotA,
                                     userbus = userEventBus,
                                     parkbus = parkingLotBus)


parkingLotB = ParkingLotB(userbus = userEventBus)
parkingLotBus.addToBus(parkingLotB) 

parkingMatSensorB = ParkingMatSensor(parkingLot = parkingLotB,
                                     userbus = userEventBus,
                                     parkbus = parkingLotBus)


# Initialize the Venues 
venueA = VenueA(userbus = userEventBus)
venueEventBus.addToBus(venueA)

qrCodeA = QRCode(venue = venueA, 
                 userbus = userEventBus, 
                 venuebus = venueEventBus)

bookingWindowA = BookingWindow(venuebus = venueEventBus,
                               name_venue = venueA.getName()) 


venueB = VenueB(userbus = userEventBus)
venueEventBus.addToBus(venueB)

qrCodeB = QRCode(venue = venueB, 
                 userbus = userEventBus, 
                 venuebus = venueEventBus)

bookingWindowB = BookingWindow(venuebus = venueEventBus,
                               name_venue = venueB.getName()) 

venueC = VenueC(userbus = userEventBus) 
venueEventBus.addToBus(venueC)

qrCodeC = QRCode(venue = venueC, 
                 userbus = userEventBus, 
                 venuebus = venueEventBus)

bookingWindowC = BookingWindow(venuebus = venueEventBus,
                               name_venue = venueC.getName()) 


# Accessibility Service
accessibilityService = AccessibilityService("blind") 
acBus.addToBus(accessibilityService)

accessibilityService = AccessibilityService("deaf")
acBus.addToBus(accessibilityService) 

visitors = [] 

i = 0 
# Start the event! 
 
venue_event = VenueEvent(name = "Lecture by Dr. SK", 
                         type = "science",
                         venuebus = venueEventBus,
                         userbus = usernotifierBus)



types = ["science", "comedy", "game"] 


while True: 
    # Every minute we try to create a new event 
    if i%12 == 0:
        print("New event started!") 
        venue_event.endEvent() 
        venue_event = VenueEvent(name = "Henry Sir Lecture", type = "science", venuebus = venueEventBus,
                                 userbus = usernotifierBus)

        adminBus = EventAdminBus()
        for iota in ['Harjin','Kaul','Yashdeep','Jakob']:
            admin = EventAdmin(name = iota, event = venue_event.getName())
            adminBus.addToBus(admin)
        
        venue_event.startEvent(event_bus = adminBus) 
        venue_event.recommendEvent() 
    
    i += 1

    # Someone visits and becomes a visitor with probability 0.4 per time 
    if random.random() < 0.4:
        # Visitor name 
        name = input("Enter the name of the person: ")
        index = int(input('Enter the index (0 based) you are interested in ["science", "comedy", "game"]: ') )
        disability = input("Are you disabled?")
        disability = {'yes' : True, 'no' : False}[disability]
        if disability == True:
            disability = list(input('Enter disabilties:').split())
            ny = Visitor(name, types[index], disability = disability, acBus = acBus) 
        else: 
            ny = Visitor(name, types[index]) 
        visitors.append(ny)
        ny = ny.getUser() 
     
        userEventBus.addToBus(ny)
        weatherBus.addToBus(ny) 
        usernotifierBus.addToBus(ny)
        
        n = int(input("Tickets:"))
        bookingWindowA.bookTickets(demand = n)  
        
    if random.random() < 0.5:
        if visitors != []:
            visitors[-1].scanQRCode(qrCodeA)
    
    if random.random() < 0.5:
        if visitors != []:
            visitors[-1].scanMatSensor(parkingMatSensorA)
        parkingMatSensorA.sendValues() 
    
    # Weather Sensor sending values to the Users at the end of the iterations! 
    tempSensor.sendValues() 
    humSensor.sendValues() 
    
    time.sleep(1.0) 