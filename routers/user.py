from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db

from services import user as user_service
from schemas import user as user_schema

router = APIRouter()


@router.post("/", tags=["user"])
async def create(data: user_schema.User, db: Session = Depends(get_db)):
    return user_service.create_user(data, db)


@router.get("/{id}", tags=["user"])
async def get(id: int = None, db: Session = Depends(get_db)):
    return user_service.get_user(id, db)


@router.get("/all/", response_model=List[user_schema.User], tags=["user"])
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.put("/{id}", tags=["user"])
async def update(data: user_schema.User, id: int = None, db: Session = Depends(get_db)):
    return user_service.update_user(data, id, db)


@router.delete("/{id}", tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return user_service.delete_user(id, db)
