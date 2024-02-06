from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Path

from user.models import User


def create_user(data: User, db: Session):
    """Create user in database"""
    user = User(username=data.username)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user


def get_user(id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    "Get user by id"
    return db.query(User).filter(User.id == id).first()


def get_users(db: Session):
    "Get all users from db"
    return db.query(User).all()


def update_user(data: User, id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    """Update username by id"""
    user = db.query(User).filter(User.id == id).first()
    user.username = data.username

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    """Delete user by id"""
    user = db.query(User).filter(User.id == id).delete()
    db.commit()

    return user
