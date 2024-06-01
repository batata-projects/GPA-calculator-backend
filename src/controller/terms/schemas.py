from pydantic import BaseModel

from src.db.models.terms import Term


class TermResponse(BaseModel):
    terms: list[Term] = []
