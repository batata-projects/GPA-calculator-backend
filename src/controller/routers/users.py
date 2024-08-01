from typing import Any

from fastapi import Depends, status

from src.common.responses import APIResponse
from src.common.utils.types import UuidStr
from src.controller.routers._base_router import BaseRouter
from src.core.user.dashboard import get_dashboard_data
from src.db.dao import CourseDAO, UserDAO
from src.db.dependencies import get_course_dao, get_user_dao
from src.db.models import User
from src.db.models.courses import Course

users_router_class = BaseRouter[User](
    prefix="/users",
    tags=["Users"],
    name="User",
    model=User,
    get_dao=get_user_dao,
)


@users_router_class.router.get("/dashboard/{user_id}")
async def get_dashboard(
    user_id: UuidStr,
    user_dao: UserDAO = Depends(get_user_dao),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse:
    try:
        user = user_dao.get_by_id(user_id)
        if user is None:
            return APIResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                message="User not found",
            )
        user_data = user.model_dump(exclude={"grade"})
        user_data["gpa"] = 0
        if user.counted_credits:
            user_data["gpa"] = round(user.grade / user.counted_credits, ndigits=10)
        del user_data["counted_credits"]

        courses = course_dao.get_by_query(user_id=user_id)

        terms: dict[Any, Any] = {}

        for course in courses:
            term = course.term
            if term not in terms:
                terms[term] = {
                    "name": " ".join(map(str, Course.convert_to_term_name(term))),
                    "gpa": 0.0,
                    "grade": 0.0,
                    "credits": 0,
                    "counted_credits": 0,
                    "courses": {},
                }
            if course.graded and course.grade is not None and course.grade != -1:
                terms[term]["grade"] += course.grade * course.credits
                terms[term]["counted_credits"] += course.credits
            if course.grade:
                terms[term]["credits"] += course.credits
            terms[term]["courses"][course.id] = course.model_dump(
                exclude={"id", "user_id"}
            )

        for term in terms:
            if terms[term]["counted_credits"]:
                terms[term]["gpa"] = round(
                    terms[term]["grade"] / terms[term]["counted_credits"],
                    ndigits=10,
                )
            del terms[term]["grade"]
            del terms[term]["counted_credits"]

        return APIResponse(
            status_code=status.HTTP_200_OK,
            message="Dashboard data retrieved",
            data=get_dashboard_data(user, courses),
        )

    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


users_router = users_router_class.build_router()
