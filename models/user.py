
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    full_name = Column(String(128), nullable=True)
    user_name = Column(String(128), nullable=True)
    phone = Column(String(128), nullable=True)
    adress = Column(String(128), nullable=True)
    gender = Column(String(10),nullable=True)
    dp = Column(String(128),nullable=True)
    skill = Column(String(128), nullable=True)
    about = Column(String(1024), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    availability = Column(String(128), nullable=True)
    user_type = Column(String(128), nullable=True)
    region = Column(String(128), nullable=True)
    town = Column(String(128), nullable=True)
    country = Column(String(128), nullable=True)

    # service_request = relationship("ServiceRequest", backref="user")
    # service_request2 = relationship("ServiceRequest", backref="user")

    #reviews = relationship("Review", backref="user")
    notifications = relationship("Notification",backref="user")

    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)


    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)


    # def userdata(self, userId):
    #     return self.query().
