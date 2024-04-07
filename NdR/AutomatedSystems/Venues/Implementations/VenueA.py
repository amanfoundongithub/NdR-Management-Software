from ..Abstract.Venue import Venue


class VenueA(Venue):
    '''
    Initializes a 500 capacity venue at the 
    city center
    '''
    def __init__(self, userbus):
        super().__init__("Venue A",500, userbus) 