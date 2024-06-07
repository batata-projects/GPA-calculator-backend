from pydantic import BaseModel as PydanticBaseModel

from src.db.models.terms import Term


class TermResponse(PydanticBaseModel):
    terms: list[Term] = []
