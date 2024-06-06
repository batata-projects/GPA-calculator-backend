from typing import Optional

from src.db.models.utils.models.BaseModel import BaseModel
from src.db.models.utils.types.TermStr import TermStr
from src.db.models.utils.types.UuidStr import UuidStr


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr
