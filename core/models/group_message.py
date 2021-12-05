from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core import Base
import datetime


class GroupMessages(Base):
    __tablename__ = 'group_messages'

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer)
    group = Column(Integer, ForeignKey('group.id'))
    date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    content = Column(String)

