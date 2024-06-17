from typing import Optional

from src.common.utils.types import TermStr
from src.controller.schemas._base_schemas import BaseQuery
from src.db.models import Term


class TermQuery(BaseQuery[Term]):
    name: Optional[TermStr] = None
