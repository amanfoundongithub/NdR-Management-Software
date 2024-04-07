from ..Abstract.Venue import Venue


class VenueC(Venue):
    '''
    Initializes a 200 capacity venue at the 
    city center
    '''
    def __init__(self, userbus):
        super().__init__("Venue C", 200, userbus) 