
class EventAdmin(object):
    def __init__(self, name : str, event : str):
        self.__name = name 
        self.__event = event 
        
        self.__venue_participants = {
            'Venue A' : 500,
            'Venue B' : 200,
            'Venue C' : 200
        }
    
    def getVenueUpdate(self, data):
        try:
            name_of_venue = data['name']
            joined_people = int(data['demand'])
        except Exception:
            return 
        
        if name_of_venue in self.__venue_participants:
            self.__venue_participants[name_of_venue] -= joined_people
            print("-------------")
            print(self.__name)
            print("ADMIN LOG: ", joined_people, " tickets booked for ", name_of_venue) 
            print("LEFT: ", self.__venue_participants.get(name_of_venue))
            print("--------------")
    
    def getName(self):
        return self.__name