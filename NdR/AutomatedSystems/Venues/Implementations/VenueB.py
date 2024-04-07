from ..Abstract.Venue import Venue


class VenueB(Venue):
    '''
    Initializes a 200 capacity venue at the 
    city center
    '''
    def __init__(self, userbus):
        super().__init__("Venue B",200, userbus)  