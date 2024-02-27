from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base
from user.mixin import UserRelationMixin


if TYPE_CHECKING:
    from user.models import User


class Post(UserRelationMixin, Base):
    __tablename__ = "post"
    # __allow_unmapped__ = True
    back_populates_mode = "posts"

    title: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

