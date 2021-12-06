from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from core import Base
import datetime


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    content = Column(String)

