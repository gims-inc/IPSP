
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class ServiceRequest(BaseModel,Base):

    __tablename__ = 'service_requests'
    provider_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    consumer_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    status = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)