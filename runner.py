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

from NdR.Participants.User import User
from NdR.Participants.Visitor import Visitor

from NdR.VenueEvent.VenueEvent import VenueEvent

from NdR.BookingWindow.BookingWindow import BookingWindow

from EventBus.User.UserBus                              import UserBus
from EventBus.Venue.VenueBus                            import VenueBus
from EventBus.ParkingLot.ParkingLotBus                  import ParkingLotBus
from EventBus.Weather.WeatherBus                        import WeatherBus
from EventBus.VenueEvent.UserNotifierBus                import UserNotifierBus
from EventBus.AccessibilityService.AccessibilityService import AccessibilityBus

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


venue_event.startEvent() 


types = ["science", "comedy", "game"] 


while True: 
    i += 1
    
    # Every minute we try to create a new event 
    if i%12 == 0:
        venue_event.endEvent() 
        venue_event = VenueEvent(name = "Henry Sir Lecture", type = "science", venuebus = venueEventBus,
                                 userbus = usernotifierBus)
        venue_event.startEvent() 
        venue_event.recommendEvent() 

    # Someone visits and becomes a visitor with probability 0.4 per time 
    if random.random() < 0.4:
        # Visitor name 
        name = input("Enter the name of the person: ")
        index = int(input('Enter the index (0 based) you are interested in ["science", "comedy", "game"]: ') )
        disability = input("Are you disabled?")
        disability = {'yes' : True, 'no' : False}[disability]
        if disability == True:
            ny = User(name, types[index], disability = disability, acBus = acBus) 
        else: 
            ny = User(name, types[index]) 
        visitors.append(Visitor(ny)) 
        userEventBus.addToBus(ny)
        weatherBus.addToBus(ny) 
        usernotifierBus.addToBus(ny) 
        
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