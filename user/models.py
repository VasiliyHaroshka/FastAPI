from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base

if TYPE_CHECKING:
    from posts.models import Post


class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True

    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
