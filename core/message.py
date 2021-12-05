from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session
from jose import jwt

from core.models import Message, Contact, User


def get_messages(db: Session, user: int, contact: int) -> Optional[Contact]:
    messages = db.query(Contact).filter_by(contact_id=contact, user_id=user).first().messages.all()
    return messages


def new_message(db: Session, user: int, contact: int, msg_content: str) -> Optional[Contact]:
    contact_obj = db.query(Contact).filter_by(contact_id=contact, user_id=user).first()
    new_msg = Message(content=msg_content)
    contact_obj.messages.append(new_msg)
    db.commit()
    return new_msg


def create_contact(db: Session, user: int, contact: int) -> bool:
    contact_obj = db.query(Contact).filter_by(contact_id=contact, user_id=user).first()
    contact_obj = db.query(User).filter_by(id=user).first().contacts.filter_by(contact_id=contact).first()
    if contact:
        return False
    else:
        user = db.query(User).filter_by(username=username).first()
        new_contact = Message(contact_id=contact)
    contact_obj.messages.append(new_msg)
    db.commit()

    new_msg = Message(sender_id=user, receiver_id=contact, content=msg)
    db.add(new_msg)
    db.commit()

    return True
