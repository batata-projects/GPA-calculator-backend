from pydantic import BaseModel


class Term(BaseModel):
    name: str
