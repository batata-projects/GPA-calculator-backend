from typing import Any

from pydantic import BaseModel as PydanticBaseModel

from src.common.utils.types import CourseStr, TermInt, UuidStr
from src.db.models import Course, User


class Term(PydanticBaseModel):
    name: str
    gpa: float = 0.0
    credits: int = 0
    counted_credits: int = 0
    grade: float = 0.0
    courses: dict[UuidStr, Course] = {}


def get_dashboard_data(user: User, courses: list[Course]) -> dict[str, Any]:
    terms: dict[TermInt, Term] = {}
    courses_dict: dict[tuple[CourseStr, CourseStr], Course] = {}

    credits = 0
    counted_credits = 0
    grade = 0.0

    for course in courses:
        if not course.id:
            raise ValueError("Course ID is required")

        term_number = course.term

        if term_number not in terms:
            terms[term_number] = Term(
                name=" ".join(map(str, Course.convert_to_term_name(term_number)))
            )

        if course.grade is not None and course.grade != -1:
            terms[term_number].credits += course.credits
            if course.graded:
                terms[term_number].counted_credits += course.credits
                terms[term_number].grade += course.grade * course.credits

        terms[term_number].courses[course.id] = course
        key = (course.subject, course.course_code)

        if key not in courses_dict:
            courses_dict[key] = course
        else:
            courses_dict[key].grade = max(
                [courses_dict[key].grade, course.grade],
                default=None,
                key=lambda x: (x is not None, x),
            )

    for term in terms.values():
        if term.counted_credits:
            term.gpa = round(term.grade / term.counted_credits, ndigits=10)

    for course in courses_dict.values():
        if course.grade is not None and course.grade != -1:
            credits += course.credits
            if course.graded:
                counted_credits += course.credits
                grade += course.grade * course.credits

    return {
        "user": {
            **user.model_dump(
                exclude={
                    "counted_credits",
                    "grade",
                }
            ),
            "gpa": (
                round(grade / counted_credits, ndigits=10) if counted_credits else 0.0
            ),
        },
        "terms": {
            term_number: term.model_dump(
                exclude={
                    "grade": ...,
                    "counted_credits": ...,
                    "courses": {course.id: {"user_id", "id"} for course in courses},
                }
            )
            for term_number, term in terms.items()
        },
    }
