from collections import defaultdict
from typing import Any, Dict, List

from src.db.models import Course, User


def get_dashboard_data(user: User, courses: List[Course]) -> Dict[str, Any]:
    user_data = user.model_dump()
    user_data["gpa"] = 0.0
    total_grade_points = 0.0
    total_counted_credits = 0
    total_credits = 0

    terms: Dict[Any, Any] = {}

    # dictionary for quick lookup
    course_dict = defaultdict(list)
    for course in courses:
        key = (course.subject, course.course_code, course.credits)
        course_dict[key].append(course)

    # check courses
    for new_course in courses:
        key = (new_course.subject, new_course.course_code, new_course.credits)
        similar_courses = [
            course
            for course in course_dict[key]
            if course.grade > -1 and course.id != new_course.id
        ]

        term = new_course.term
        if term not in terms:
            terms[term] = {
                "name": " ".join(map(str, Course.convert_to_term_name(term))),
                "gpa": 0.0,
                "grade": 0.0,
                "credits": 0,
                "counted_credits": 0,
                "courses": {},
            }

        if similar_courses:
            max_course = max(
                similar_courses, key=lambda c: (c.grade, c.term)
            )  # setting the max similar course as the main course
            if (
                max_course.grade < new_course.grade
                and new_course.grade != -1
                and new_course.graded
            ):
                # If the new course grade is higher, replace the max course grade with the new course grade
                total_grade_points += (new_course.grade * new_course.credits) - (
                    max_course.grade * max_course.credits
                )
                terms[term]["grade"] += new_course.grade * new_course.credits
                terms[term]["counted_credits"] += new_course.credits
                terms[term]["credits"] += new_course.credits

            else:
                terms[term]["grade"] += new_course.grade * new_course.credits
                terms[term]["counted_credits"] += new_course.credits
                terms[term]["credits"] += new_course.credits

                # If the new course grade is not higher, skip adding this course
                continue

        else:
            if (
                new_course.graded
                and new_course.grade is not None
                and new_course.grade != -1
            ):
                # Add the new course grade and credits to the user data
                total_grade_points += new_course.grade * new_course.credits
                total_counted_credits += new_course.credits
                terms[term]["grade"] += new_course.grade * new_course.credits
                terms[term]["counted_credits"] += new_course.credits
                terms[term]["credits"] += new_course.credits
            elif not new_course.graded and (
                new_course.grade == 1 or new_course.grade == 0
            ):
                # Only add the credits for pass/fail courses
                total_credits += new_course.credits
                terms[term]["credits"] += new_course.credits

        terms[term]["courses"][new_course.id] = {
            "subject": new_course.subject,
            "course_code": new_course.course_code,
            "term": new_course.term,
            "credits": new_course.credits,
            "grade": new_course.grade,
            "graded": new_course.graded,
        }

        for term in terms:
            if terms[term]["counted_credits"]:
                terms[term]["gpa"] = (
                    terms[term]["grade"] / terms[term]["counted_credits"]
                )
            del terms[term]["grade"]
            del terms[term]["counted_credits"]

        if total_counted_credits:
            user_data["gpa"] = total_grade_points / total_counted_credits
        user_data["total_credits"] = total_credits
        user_data["counted_credits"] = total_counted_credits
        return {"user": user_data, "terms": terms}
