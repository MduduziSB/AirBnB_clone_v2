#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv as gv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    storage_type = gv("HBNB_TYPE_STORAGE")

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute to retrieve linked City instances"""
            from models import storage
            from models.city import City
            city_instances = storage.all(City)
            return [city for city in city_instances.values()
                    if city.state_id == self.id]
