from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from user.models import User


class UserRelationMixin:
    unique_mode: bool = False
    nullable_mode: bool = False
    back_populates_mode: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("user.id"),
            unique=cls.unique_mode,
            nullable=cls.nullable_mode,
        )

    @declared_attr
    def user_id(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls.back_populates_mode,
        )
