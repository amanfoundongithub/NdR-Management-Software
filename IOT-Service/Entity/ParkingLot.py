import sys
sys.path.append('../../IOT-Service')

import random
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, ForeignKey,String,Float
from sqlalchemy.orm import relationship
from Service import base

Base = base.Base  

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
