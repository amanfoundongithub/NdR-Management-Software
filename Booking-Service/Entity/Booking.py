import sys
sys.path.append('../../Booking-Service')

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Service import base 

Base = base.Base


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_id = Column(Integer, ForeignKey('events.id'))
    num_tickets = Column(Integer)

    # Define a relationship with the Event model
    event = relationship('Event', back_populates='bookings')
