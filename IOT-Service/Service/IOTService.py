import random
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from math import radians, sin, cos, sqrt, atan2

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///IOT_Service.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Venue model
class ParkingLot(Base):
    __tablename__ = 'parking_lots'
    #define some attributes for Parking Lot
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    parked = Column(Integer)
    iot_device_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    
# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()

class IOTService():

    @staticmethod
    def createParkingLot(name, location, capacity, parked,iot_device_id,latitude , longitude):
        parking_lot = ParkingLot(name=name, location=location, capacity=capacity,parked = parked, iot_device_id=iot_device_id,latitude=latitude,longitude=longitude)
        session.add(parking_lot)
        session.commit()
        return parking_lot

    @staticmethod
    def fetchFromSensor():
        '''Implementation to Fetch Data from Sensor ID'''
        pass
        
    @staticmethod
    def fetchParkingLot(parking_lot_id):
        IOTService.fetchFromSensor()
        parking_lot = session.query(ParkingLot).filter_by(id=parking_lot_id).first()
        return parking_lot

    @staticmethod
    def fetchAllParkingLots():
        IOTService.fetchFromSensor()
        parking_lots = session.query(ParkingLot).all()
        return parking_lots
    
    @staticmethod
    def fetchAvailableParkingLots():
        IOTService.fetchFromSensor()
        parking_lots = session.query(ParkingLot).filter(ParkingLot.capacity > ParkingLot.parked).all()
        return parking_lots