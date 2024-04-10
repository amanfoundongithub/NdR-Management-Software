
import sys
sys.path.append('/Users/zaid/Downloads/Software Engineering/Assignments/NdR-Management-Software/Booking-Service')

from sqlalchemy import Column, Integer, String,Float, ForeignKey
from sqlalchemy.orm import relationship
from Service.Base import Base

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    capacity = Column(Integer)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    # Define a relationship with the Event model
    events = relationship('Event', back_populates='venue')
