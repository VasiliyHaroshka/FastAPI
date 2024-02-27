from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True

    username: Mapped = mapped_column(String(50), unique=True, index=True)
