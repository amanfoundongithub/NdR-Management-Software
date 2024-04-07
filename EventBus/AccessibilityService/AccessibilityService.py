from NdR.AccessibilityService.AccessibilityService import AccessibilityService
from ..Event    import Event

class AccessibilityBus(object):
    
    def __init__(self):
        
        self.__users = {}
        self.__bus   = {}
        
        # Subscribe all the events 
        self.__bus['add'] = AccessibilityService.addPerson
        
    
    def addToBus(self, user : AccessibilityService):
        if user.getName() not in self.__users:
            self.__users[user.getName()] = user
    
    def publishToBus(self, event : Event, name_of_user = None):
        name = event.getName() 
        if name not in self.__bus: 
            return 
        
        if name_of_user is None: 
            for user in self.__users:
                self.__bus[name](self.__users[user], event.getData())
        else: 
            if name_of_user in self.__users:
                self.__bus[name](self.__users[name_of_user], 
                                 event.getData())
    