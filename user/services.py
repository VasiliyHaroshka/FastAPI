from typing import Annotated

from annotated_types import MinLen, MaxLen
from sqlalchemy.orm import Session
from fastapi import Path, HTTPException, status

from user.models import User
from user.schemas import UserUpdate


def create_user(username_in: Annotated[str, MinLen(3), MaxLen(50)], db: Session):
    """Create user in database"""
    user = User(username=username_in)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user


def get_user(id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    """Get user by id"""
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={id} not exists",
        )
    return user


def get_users(db: Session):
    """Get all users from db"""
    users = db.query(User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no users yet",
        )
    return users


def update_user(data: UserUpdate, id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    """Update username by id"""
    user = get_user(id=id, db=db)
    user.username = data.username

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(id: Annotated[int, Path(ge=1, lt=1_000_000)], db: Session):
    """Delete user by id"""
    user = get_user(id=id, db=db)
    db.delete(user)
    db.commit()

    return user
