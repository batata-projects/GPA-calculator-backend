from pydantic import BaseModel

from src.db.models.utils import UuidStr


class TermResponse(BaseModel):
    id: UuidStr
    name: str
