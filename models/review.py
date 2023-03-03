
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    on_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    by_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    on_user = relationship('User', foreign_keys=on_user_id)
    by_user = relationship('User', foreign_keys=by_user_id)
    

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
