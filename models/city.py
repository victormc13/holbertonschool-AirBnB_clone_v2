#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storage_t == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place',
                              backref='cities',
                              cascade='all, delete, delete-orphan')

    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City instance"""
        super().__init__(*args, **kwargs)
