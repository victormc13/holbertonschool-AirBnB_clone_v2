#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
# from models import storage


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    id: Column(String(60), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Add a relationship between City and State
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """Instatntiates a new city"""
        super().__init__(*args, **kwargs)
