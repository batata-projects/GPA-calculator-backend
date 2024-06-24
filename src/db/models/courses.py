from typing import Optional

from src.common.utils.types import (
    CourseCodeStr,
    CourseGradeFloat,
    SubjectStr,
    TermInt,
    UuidStr,
)
from src.db.models import BaseModel


class Course(BaseModel):
    id: Optional[UuidStr] = None
    user_id: UuidStr
    subject: SubjectStr
    course_code: CourseCodeStr
    term: TermInt
    credits: int
    grade: Optional[CourseGradeFloat] = None
    graded: bool

    @classmethod
    def convert_to_term_number(cls, term_name: str, year: int) -> int:
        term_name = term_name.strip()
        if not 1000 <= year <= 9999:
            raise ValueError(f"Invalid year: {year}")
        if term_name == "Fall":
            return year * 100 + 10
        elif term_name == "Winter":
            return year * 100 + 15
        elif term_name == "Spring":
            return year * 100 + 20
        elif term_name == "Summer":
            return year * 100 + 30
        else:
            raise ValueError(f"Invalid term name: {term_name}")

    # TODO: Test this method
    @classmethod
    def convert_to_term_name(cls, term_number: int) -> str:
        year = term_number // 100
        term = term_number % 100
        if term == 10:
            return f"Fall {year}"
        elif term == 15:
            return f"Winter {year}"
        elif term == 20:
            return f"Spring {year}"
        elif term == 30:
            return f"Summer {year}"
        else:
            raise ValueError(f"Invalid term number: {term_number}")
