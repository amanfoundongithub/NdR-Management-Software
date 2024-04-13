import sys
sys.path.append('../../Booking-Service')

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer,Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from Service import base
from Entity import Booking
from Entity import Event
from Entity import Venue


# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///booking_service.db', echo=True)

# Create a base class for declarative class definitions
Base = base.Base
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()

Booking = Booking.Booking
Event = Event.Event
Venue = Venue.Venue

class BookingService:
    @staticmethod
    def create_booking(user_id, event_id, num_tickets):
        booking = Booking(user_id=user_id, event_id=event_id, num_tickets=num_tickets)
        event = session.query(Event).get(event_id)
        event.booked_seats += num_tickets
        session.add(booking)
        session.commit()
        return booking

    @staticmethod
    def get_booking(id):
        return session.query(Booking).get(id)

    @staticmethod
    def get_all_bookings():
        return session.query(Booking).all()

    @staticmethod
    def create_event(name, event_type, venue_id, start_time, end_time):
        event = Event(name=name, event_type=event_type, venue_id=venue_id, start_time=start_time, end_time=end_time)
        session.add(event)
        session.commit()
        return event

    @staticmethod
    def get_event(id):
        return session.query(Event).get(id)

    @staticmethod
    def get_all_events():
        return session.query(Event).all()

    @staticmethod
    def create_venue(name, capacity, location,latitude,longitude):
        venue = Venue(name=name, capacity=capacity, location=location,latitude=latitude,longitude=longitude)
        session.add(venue)
        session.commit()
        return venue

    @staticmethod
    def get_venue(id):
        return session.query(Venue).get(id)

    @staticmethod
    def get_all_venues():
        return session.query(Venue).all()

    @staticmethod
    def get_free_tickets(event_id):
        try : 
            event = session.query(Event).get(event_id)
            venue = session.query(Venue).get(event.venue_id)
            if venue and event:
                return venue.capacity - event.booked_seats
        ##print the error 
        except :
            pass
        return 0

    @staticmethod
    def close_session():
        session.close()

