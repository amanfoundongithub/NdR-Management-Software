

class Event(object):
    '''
    Event object that contains the name and the details of the events in Event Driven Architecture 
    '''
    def __init__(self, 
                 event_name : str, 
                 event_data):
        self.__name = event_name 
        self.__data = event_data
    
    def getName(self):
        return self.__name

    def getData(self):
        return self.__data 