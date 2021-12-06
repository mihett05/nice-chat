from typing import Optional

from sqlalchemy.orm import Session

from core.models import Message


def get_messages(db: Session):
    messages = db.query(Message).all()
    return messages


def add_message(db: Session, user: int, msg_content: str):
    new_msg = Message(content=msg_content, sender_id=user)
    db.add(new_msg)
    db.commit()
    return new_msg
