from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True

    id: Mapped = mapped_column(Integer, primary_key=True)
    username: Mapped = mapped_column(String, unique=True, index=True)
