from pydantic import BaseModel
from src.db.models.utils import UuidStr
from typing import Optional

class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: str
