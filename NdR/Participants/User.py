from EventBus.Event import Event
class User(object):
    def __init__(self, name, preference,disability = None, acBus = None):
        self.__pref = preference 
        self.__name = name 
        
        if disability is not None:
            event = Event("add", {'name' : self.__name, 'disabilities' : disability})
            acBus.publishToBus(event) 
    
    def getName(self):
        return self.__name
    
    def getTemperature(self, value):
        print("I am", self.__name, "& Temperature recieved: ", value) 
        return 
    
    def getHumidity(self, value):
        print("I am", self.__name, "& Humidity recieved: ", value) 
        return 
    
    def getAvailableVenue(self, name):
        print("I am " + self.__name + " and Venue named: " + name + " is available!") 
    
    def getAltVenue(self, name):
        print("\nVenue is full! You can try " + name + " , " + self.getName() + "\n") 
    
    def getAvailableLot(self, name):
        print("\nLot named " + name + " is available! for " + self.getName() + '\n')   
    
    def getAltLot(self, name):
        print("Lot is full! You can try " + name + " , " + self.getName())   
    
    def getEventRecommendation(self, data):
        name = data['name']
        tpe  = data['type']
        
        if tpe == self.__pref:
            print("Hey " + self.getName() + "! Event " + name + " is starting!\n") 
    
        