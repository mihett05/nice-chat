from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    admin = Column(Integer, ForeignKey('user.id'))
    members = relationship("Member", backref="group")
    messages = relationship("Message", backref="group")
