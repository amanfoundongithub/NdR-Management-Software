from ..Abstract.ParkingLot import ParkingLot

class ParkingLotB(ParkingLot):
    '''
    Initializes a 150 passenger parking Lot 
    '''
    def __init__(self, userbus):
        super().__init__("Parking Lot B",150, userbus)