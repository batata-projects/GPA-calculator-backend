from typing import Any

from fastapi import Depends

from src.common.responses import APIResponse
from src.common.utils.types import UuidStr
from src.controller.routers._base_router import BaseRouter
from src.db.dao import BaseDAO
from src.db.dependencies import get_course_dao
from src.db.models import Course

courses_router_class = BaseRouter[Course](
    prefix="/courses",
    tags=["Courses"],
    name="Course",
    model=Course,
    get_dao=get_course_dao,
)


@courses_router_class.router.post("/")
async def create(
    request: dict[str, Any] = courses_router_class.request,
    dao: BaseDAO[Course] = Depends(courses_router_class.get_dao),
) -> APIResponse:
    query_params = {
        "subject": request["subject"],
        "course_code": request["course_code"],
    }
    queried_course = dao.get_by_query(**query_params)[0]
    if queried_course and queried_course.credits != request["credits"]:
        raise ValueError("Course already exists with different credit value")
    return await courses_router_class.create(request, dao)


@courses_router_class.router.post("/many")
async def create_many(
    request: list[dict[str, Any]] = courses_router_class.request_many,
    dao: BaseDAO[Course] = Depends(courses_router_class.get_dao),
) -> APIResponse:
    # check for same course subject and course_code in the request list
    # then if same found check their credits
    ############################# UNDER CONSTRUCTION #############################
    for course in request:
        courses = [
            course
            for course in request
            if course["subject"] == course["subject"]
            and course["course_code"] == course["course_code"]
        ]
        if len(courses) > 1:
            for course in courses:
                if course["credits"] != courses[0]["credits"]:
                    raise ValueError("Same course exists with different credit value")

    for course in request:
        query_params = {
            "subject": course["subject"],
            "course_code": course["course_code"],
        }
        queried_courses = dao.get_by_query(**query_params)
        if queried_course:
            queried_course = queried_courses[0]
            # print(queried_course)
        if queried_course and queried_course.credits != course["credits"]:
            raise ValueError("Course already exists with different credit value")
    return await courses_router_class.create_many(request, dao)


@courses_router_class.router.put("/")
async def update(
    id: UuidStr,
    request: dict[str, Any] = courses_router_class.request,
    dao: BaseDAO[Course] = Depends(courses_router_class.get_dao),
) -> APIResponse:
    return await courses_router_class.update(id, request, dao)


courses_router = courses_router_class.build_router()
