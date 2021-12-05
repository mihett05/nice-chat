from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime

from core import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    contacts = relationship("Contact", backref="user")
    registered = Column(DateTime, nullable=False, default=datetime.datetime.now())
    last_online = Column(DateTime, nullable=False, default=datetime.datetime.now())
    online = Column(Boolean, default=True)
