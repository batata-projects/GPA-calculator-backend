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
    queried_courses = dao.get_by_query(**query_params)
    queried_course = None
    if len(queried_courses) > 0:
        queried_course = queried_courses[0]
    if queried_course and queried_course.credits != request["credits"]:
        raise ValueError("Course already exists with different credit value")
    elif queried_course and queried_course.graded != request["graded"]:
        raise ValueError("Course already exists with different graded value")
    query_params = {
        "subject": request["subject"],
        "course_code": request["course_code"],
        "term": request["term"],
    }
    queried_courses = dao.get_by_query(**query_params)
    if len(queried_courses) > 0:
        raise ValueError("Course already exists with the same term")
    return await courses_router_class.create(request, dao)


@courses_router_class.router.post("/many")
async def create_many(
    request: list[dict[str, Any]] = courses_router_class.request_many,
    dao: BaseDAO[Course] = Depends(courses_router_class.get_dao),
) -> APIResponse:
    for course in request:
        query_params = {
            "subject": course["subject"],
            "course_code": course["course_code"],
        }
        queried_courses = dao.get_by_query(**query_params)
        if len(queried_courses) > 0:
            queried_course = queried_courses[0]
            if queried_course and queried_course.credits != course["credits"]:
                raise ValueError("Course already exists with different credit value")
            elif queried_course and queried_course.term == course["term"]:
                raise ValueError("Course already exists with the same term")
            elif queried_course and queried_course.graded != course["graded"]:
                raise ValueError("Course already exists with different graded value")
    return await courses_router_class.create_many(request, dao)


@courses_router_class.router.put("/{id}")
async def update(
    id: UuidStr,
    request: dict[str, Any] = courses_router_class.request,
    dao: BaseDAO[Course] = Depends(courses_router_class.get_dao),
) -> APIResponse:
    course_to_update = dao.get_by_query(id=id)[0]

    if not dao.get_by_query(
        **{
            "subject": course_to_update.subject,
            "course_code": course_to_update.course_code,
            "credits": request["credits"],
        }
    ):
        raise ValueError("Course exists with different credit value")
    if course_to_update.credits != request["credits"]:
        raise ValueError("Cannot update credits of a course")
    elif course_to_update.graded != request["graded"]:
        raise ValueError("Cannot update graded status of a course")
    elif (
        course_to_update.subject != request["subject"]
        or course_to_update.course_code != request["course_code"]
    ):
        query_params = {
            "subject": request["subject"],
            "course_code": request["course_code"],
        }
        queried_courses = dao.get_by_query(**query_params)
        if len(queried_courses) > 0:
            queried_course = queried_courses[0]
            if queried_course and queried_course.credits != request["credits"]:
                raise ValueError("Course already exists with different credit value")
            elif queried_course and queried_course.graded != request["graded"]:
                raise ValueError("Course already exists with different graded value")
        for course in queried_courses:
            if course.term == request["term"]:
                raise ValueError("Course already exists with the same term")
    return await courses_router_class.update(id, request, dao)


courses_router = courses_router_class.build_router()
