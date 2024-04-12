import random
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from math import radians, sin, cos, sqrt, atan2

from Service import base    
from Entity import ParkingLot
from Entity import VenueIOT
# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///IOT_Service.db', echo=True)

# Create a base class for declarative class definitions
Base = base.Base

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()

ParkingLot = ParkingLot.ParkingLot
VenueIOT = VenueIOT.VenueIOT

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
    
    @staticmethod
    def fetchVenueAvailability(venue_id):
        '''Implementation to Fetch Venue Availability'''
        pass
    
    @staticmethod
    def fetchAllVenues():
        '''Implementation to Fetch All Venues'''
        pass
