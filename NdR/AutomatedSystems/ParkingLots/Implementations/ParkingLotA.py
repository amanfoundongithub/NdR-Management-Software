from ..Abstract.ParkingLot import ParkingLot

class ParkingLotA(ParkingLot):
    '''
    Initializes a 200 passenger Parking Lot
    '''
    def __init__(self, userbus):
        super().__init__("Parking Lot A",200, userbus) 