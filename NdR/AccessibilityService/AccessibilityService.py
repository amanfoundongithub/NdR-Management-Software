class AccessibilityService(object):
    def __init__(self, name):
        self.__name = name
        self.__list = []
        pass 
    
    def getName(self):
        return self.__name
    
    def addPerson(self, name : str):
        print(name + " has been added to Accessibility service for " , self.__name) 
        self.__list.append(name) 
        return 