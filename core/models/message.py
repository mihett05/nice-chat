from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core import Base
import datetime


class Contact(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('contact.user_id'))
    receiver_id = Column(Integer, ForeignKey('contact.contact_id'))
    date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    content = Column(String)

