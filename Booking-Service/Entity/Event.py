import sys
sys.path.append('/Users/zaid/Downloads/Software Engineering/Assignments/NdR-Management-Software/Booking-Service')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Service.Base import Base
import json
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_type = Column(String)
    venue_id = Column(Integer, ForeignKey('venues.id'))
    start_time = Column(String)
    end_time = Column(String)
    booked_seats = Column(Integer, default=0)

    # Define a relationship with the Venue model
    venue = relationship('Venue', back_populates='events')
    # Define a relationship with the Booking model
    bookings = relationship('Booking', back_populates='event')
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)