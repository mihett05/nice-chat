from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core import Base


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    messages = relationship("Message", backref="contact")
