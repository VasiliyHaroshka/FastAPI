from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base
from .mixin import UserRelationMixin

if TYPE_CHECKING:
    from posts.models import Post


class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True

    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")


class Profile(UserRelationMixin, Base):
    unique_mode = True
    back_populates_mode = "profile"

    first_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    info: Mapped[str | None] = mapped_column(Text(500), nullable=True)


