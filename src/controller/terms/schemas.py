from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field

from src.common.utils.types.TermStr import TermStr
from src.db.models.terms import Term


class TermRequest(PydanticBaseModel):
    name: TermStr = Field(..., description="Term name")


class TermResponse(PydanticBaseModel):
    terms: list[Term] = []
