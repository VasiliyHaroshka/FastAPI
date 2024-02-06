from typing import Annotated
from annotated_types import MinLen, MaxLen

from pydantic import BaseModel


class User(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(50)]
