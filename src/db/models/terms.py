from typing import Optional

from src.db.models.utils import BaseModelCustomized, TermStr, UuidStr


class Term(BaseModelCustomized):
    id: Optional[UuidStr] = None
    name: TermStr
