from NdR.Participants.User import User
from Sensors.ParkingLot.MatSensor import ParkingMatSensor
from Sensors.VenueSensors.QRCode import QRCode


class Visitor(object):
    def __init__(self, user : User):
        self.__user = user 
    
    def scanQRCode(self, qrCode : QRCode):
        qrCode.checkAvailability(self.__user.getName()) 
    
    def scanMatSensor(self, parkingSensor : ParkingMatSensor):
        parkingSensor.checkAvailable(self.__user.getName())
    
        
        
        