### Implementation of NdR Management System using Event-Driven Architecture 
----
We have implemented the system using event driven architecture. The following shows the details of each of the folders:

- **NdR Folder**
    - This folder contains all the elements related to the NdR hardware. 
    - The following are the elements in the NdR Folder:
        - Accessibility Service 
            - This consists of an object that represents the Accessibility Service for disabled people 
        - Automated Systems
            - Consists of the Parking Lots and the Venue systems 
        - Booking Window
            - Consists of the Booking Window for the Venue 
        - Participants 
            - Consists of the User and the Visitor objects 
        - VenueEvent 
            - Consists of the Event as well as the Admins of these events

- **Sensors** 
    - This folder contains the sensors 
    - The following are the elements of this folder:
        - Parking Lot contains sensors related to Parking Lots, such as Mat Sensor and Cameras etc. to get number of cars being parked 
        - Venue Sensors are the sensors to check availability of seats in a venue 
        - Weather sensors are used to send weather information to the User. 
    
- **EventBus** 
    - This consists of the communication method between the individual classes. 
    - Several buses are defined for communication as follows:
        - One bus is dedicated to providing information about weather to the users and is called WeatherBus.
        - One bus is dedicated to providing the users with the availability of the venue and parking lot and is called the UserBus. 
        - One bus is dedicated to notifying Accessibility Services about disabled people and is called AccessibilityBus. 
        - One bus is dedicated to event related to Venue and is called VenueBus. 
        - One bus is dedicated to event related to Parking Lots and is called Parking Lot Bus. 
        - Two Buses are there for events. The Admin Bus is dedicated to providing communication about venue with the admin of the event, while the User Notifier notifies the users about specific types of events being conducted. 

    - All the buses forms a queue to send messages. All these messages have a special format, called Events. This is described in `Event.py` class. The buses have the `addToBus` feature to add a user to the bus and `publishToBus` to publish any event to all the members of the bus. 


### Feature Implementation
