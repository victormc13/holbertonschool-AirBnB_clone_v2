#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


# Retrieve the value of the environment variable 'STORAGE_TYPE'
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')


if storage_type == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        id = Column(String(60), nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)

        cities = relationship(
                "City", back_populates="state", cascade="all, delete-orphan")
else:
    class State(BaseModel):
        @property
        def cities(self):
            """Getter attribute that returns a list of City instances
        with state_id equals to the current State.id"""
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
