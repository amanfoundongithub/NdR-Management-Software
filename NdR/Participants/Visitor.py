from EventBus.Implementations.User.Abstract.UserBusInterface import UserBusInterface
from NdR.Participants.User import User
from Sensors.ParkingLot.MatSensor import ParkingMatSensor
from Sensors.VenueSensors.QRCode import QRCode

class Visitor(object):
    def __init__(self, name, preference,disability = None, acBus = None):
        self.__user = User(name, preference, disability = disability, acBus = acBus) 
    
    def addToBus(self, bus : UserBusInterface):
        bus.addToBus(self.__user)
    
    def scanQRCode(self, qrCode : QRCode):
        qrCode.checkAvailability(self.__user.getName()) 
    
    def scanMatSensor(self, parkingSensor : ParkingMatSensor):
        parkingSensor.checkAvailable(self.__user.getName())
    
        
        
        