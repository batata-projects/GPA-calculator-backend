from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field

from src.common.utils.types import TermStr
from src.db.models import Term


class TermRequest(PydanticBaseModel):
    name: TermStr = Field(..., description="Term name")


class TermResponse(PydanticBaseModel):
    terms: list[Term] = []
