from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import TermStr, UuidStr


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr
