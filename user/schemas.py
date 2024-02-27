from typing import Annotated
from annotated_types import MinLen, MaxLen
from fastapi import Path

from pydantic import BaseModel


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(50)]


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserGet(UserBase):
    id: Annotated[int, Path(ge=1, le=1_000_000)]
