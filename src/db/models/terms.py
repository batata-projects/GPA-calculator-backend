from typing import Optional

from src.common.utils.models import BaseModel
from src.common.utils.types import TermStr, UuidStr


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr
