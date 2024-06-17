from typing import Optional

from src.common.utils.types import TermStr, UuidStr
from src.db.models import BaseModel


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr
