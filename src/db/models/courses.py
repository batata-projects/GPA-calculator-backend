from typing import Optional

from src.common.utils.types import CourseGradeFloat, CourseStr, TermInt, UuidStr
from src.db.models import BaseModel


class Course(BaseModel):
    id: Optional[UuidStr] = None
    user_id: UuidStr
    subject: CourseStr
    course_code: CourseStr
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

    @classmethod
    def convert_to_term_name(cls, term_number: int) -> tuple[str, int]:
        year = term_number // 100
        term = term_number % 100
        if term == 10:
            return "Fall", year
        elif term == 15:
            return "Winter", year
        elif term == 20:
            return "Spring", year
        elif term == 30:
            return "Summer", year
        else:
            raise ValueError(f"Invalid term number: {term_number}")
