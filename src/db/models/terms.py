from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import UuidStr


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: str
