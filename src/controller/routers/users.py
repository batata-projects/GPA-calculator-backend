from typing import Any

from fastapi import Depends, status

from src.common.responses import APIResponse
from src.common.utils.types import UuidStr
from src.controller.routers._base_router import BaseRouter
from src.db.dao import CourseDAO, UserDAO
from src.db.dependencies import get_course_dao, get_user_dao
from src.db.models import Course, User

users_router = BaseRouter[User](
    prefix="/users",
    tags=["Users"],
    name="User",
    model=User,
    get_dao=get_user_dao,
).build_router()


# TODO: Add tests
@users_router.get("/dashboard/{user_id}")
async def get_dashboard(
    user_id: UuidStr,
    user_dao: UserDAO = Depends(get_user_dao),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[dict[str, Any]]:
    try:
        user = user_dao.get_by_id(user_id)
        if not user:
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message="User not found",
            )
        user_data = user.model_dump()
        user_data["gpa"] = 0
        if user.counted_credits:
            user_data["gpa"] = user.grade / user.counted_credits
        del user_data["counted_credits"]

        courses = course_dao.get_by_query(user_id=user_id)

        # TODO: Define the type of the terms variable
        terms: dict[Any, Any] = {}

        for course in courses:
            term = course.term
            if term not in terms:
                terms[term] = {
                    "name": Course.convert_to_term_name(term),
                    "gpa": 0.0,
                    "grade": 0.0,
                    "credits": 0,
                    "counted_credits": 0,
                    "courses": {},
                }
            if course.graded and course.grade:
                if type(terms[term]["grade"]) != float:
                    terms[term]["grade"] = 0.0
                    terms[term]["counted_credits"] = 0
                terms[term]["grade"] += course.grade * course.credits
                terms[term]["counted_credits"] += course.credits
            if course.grade:
                terms[term]["credits"] += course.credits
            terms[term]["courses"][course.id] = course.model_dump(
                exclude={"id", "user_id"}
            )

        for term in terms:
            if terms[term]["counted_credits"]:
                terms[term]["gpa"] = (
                    terms[term]["grade"] / terms[term]["counted_credits"]
                )
            del terms[term]["grade"]
            del terms[term]["counted_credits"]

        return APIResponse[dict[str, Any]](
            status=status.HTTP_200_OK,
            message="Dashboard data retrieved",
            data={"user": user_data, "terms": terms},
        )

    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )
