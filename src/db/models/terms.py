from typing import Optional

from src.common.utils.models.BaseModel import BaseModel
from src.common.utils.types.TermStr import TermStr
from src.common.utils.types.UuidStr import UuidStr


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr
