from typing import Any

from src.common.utils.types import TermInt
from src.db.models import Course, User


def get_dashboard_data(user: User, courses: list[Course]) -> dict[str, Any]:
    # specify Any
    terms: dict[TermInt, Any] = {}
    courses_dict: dict[tuple[str, str], dict[str, Any]] = {}

    credits = 0
    counted_credits = 0
    grade = 0

    for course in courses:

        term = course.term
        if term not in terms:
            terms[term] = {
                "name": " ".join(map(str, Course.convert_to_term_name(term))),
                "gpa": 0.0,
                "credits": 0,
                "counted_credits": 0,
                "grade": 0.0,
                "courses": {},
            }
        terms[term]["credits"] += (
            course.credits if course.grade != -1 else 0
        )  # change format of ifs
        terms[term]["counted_credits"] += (
            course.credits if course.grade != -1 and course.graded else 0
        )
        terms[term]["grade"] += (
            course.grade * course.credits if course.grade != -1 and course.graded else 0
        )
        terms[term]["courses"][course.id] = course.model_dump(exclude={"id", "user_id"})

        key = (course.subject, course.course_code)
        if key in courses_dict:
            courses_dict[key]["grade"] = max(courses_dict[key]["grade"], course.grade)
        else:
            courses_dict[key]["grade"] = course.grade
            courses_dict[key]["credits"] = course.credits
            courses_dict[key]["graded"] = course.graded

    for term in terms:
        if term["counted_credits"]:
            term["gpa"] = term["grade"] / term["counted_credits"]
        del term["grade"]
        del term["counted_credits"]

    for course in courses_dict:
        credits += course["credits"] if course["grade"] != -1 else 0
        counted_credits += (
            course["credits"] if course["grade"] != -1 and course["graded"] else 0
        )
        grade += (
            (course["grade"] * course["credits"])
            if course["grade"] != -1 and course["graded"]
            else 0
        )

    user_data = user.model_dump()
    user_data["gpa"] = grade / counted_credits if counted_credits else 0

    return {"user": user_data, "terms": terms}
