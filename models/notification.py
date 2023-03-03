
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Notification(BaseModel, Base):
    """Representation of Notifications """

    __tablename__ = 'notifications'
    read_status = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(255), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
