from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Post(Base):
    # __tablename__ = "post"
    # __allow_unmapped__ = True

    title: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )
