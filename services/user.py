from models.user import User
from sqlalchemy.orm import Session
from schemas import user


def create_user(data: user.User, db):
    """Create user in database"""
    user = User(username=data.username)

    try:
        db.add(user)
        db.commit()
        db.refresh()
    except Exception as e:
        print(e)

    return user


def get_user(id: int, db: Session):
    "Get user by username"
    return db.query(User).filter(User.id == id).first()


def update_user(data: user.User, id: int, db: Session):
    """Update username by id"""
    user = db.query(User).filter(User.id == id).first()
    user.username = data.username

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(id: int, db: Session):
    """Delete user by id"""
    user = db.query(User).filter(User.id == id).delete()
    db.commit()

    return user
