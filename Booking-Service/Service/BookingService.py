from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer,Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///booking_service.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Venue model
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

# Define the Event model
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

# Define the Booking model
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_id = Column(Integer, ForeignKey('events.id'))
    num_tickets = Column(Integer)

    # Define a relationship with the Event model
    event = relationship('Event', back_populates='bookings')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()

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

