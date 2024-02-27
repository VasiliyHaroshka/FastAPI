from typing import List, Annotated

from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from database.db import get_db

from user import schemas as user_schema
from user import services as user_service

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(data_in: str, db: Session = Depends(get_db)):
    return user_service.create_user(data_in, db)


@router.get("/{id}")
async def get(id: int = None, db: Session = Depends(get_db)):
    return user_service.get_user(id, db)


@router.get("/all/", response_model=List[user_schema.UserGet])
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.put("/{id}")
async def update(data: user_schema.UserUpdate, id: int = None, db: Session = Depends(get_db)):
    return user_service.update_user(data, id, db)


@router.delete("/{id}")
async def delete(id: int = None, db: Session = Depends(get_db)) -> None:
    return user_service.delete_user(id, db)
