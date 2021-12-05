from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core import Base


class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    group = Column(Integer, ForeignKey('group.id'))
    user = Column(String)
    alias = Column(String)
