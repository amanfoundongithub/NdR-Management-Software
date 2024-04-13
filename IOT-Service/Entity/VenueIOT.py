import sys
sys.path.append('../../IOT-Service')

import random
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Service import base

Base = base.Base

class VenueIOT(Base):
    __tablename__ = 'venue_iot'
    id = Column(Integer, primary_key=True)
    venue_id = Column(Integer, ForeignKey('parking_lots.id'))
    iot_device_id = Column(Integer)
    entered = Column(Integer)
    exited = Column(Integer)