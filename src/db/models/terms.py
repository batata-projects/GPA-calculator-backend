from typing import Optional

from src.common.utils.types import TermStr, UuidStr
from src.db.models import BaseModel


class Term(BaseModel):
    id: Optional[UuidStr] = None
    name: TermStr

    @classmethod
    def convert_from_sis_term(cls, term: str) -> "Term":
        year = term[:4]
        semester = term[4:]
        if semester == "10":
            semester = "Fall"
        elif semester == "15":
            semester = "Winter"
        elif semester == "20":
            semester = "Spring"
        elif semester == "30":
            semester = "Summer"
        else:
            raise ValueError("Invalid term")
        start = int(year) - 1
        end = year
        return Term(name=f"{semester} {start} - {end}")

    def get_sis_term(self) -> str:
        semester, start, _, end = self.name.split()
        if semester == "Fall":
            semester = "10"
        elif semester == "Winter":
            semester = "15"
        elif semester == "Spring":
            semester = "20"
        elif semester == "Summer":
            semester = "30"
        else:
            raise ValueError("Invalid term")
        return f"{end}{semester}"
