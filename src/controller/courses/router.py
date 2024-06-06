from typing import Optional

from fastapi import APIRouter, Depends, Path, Query, status
from pydantic import PositiveFloat

from src.common.responses import APIResponse
from src.controller.courses.schemas import CourseResponse
from src.db.dao.course_dao import CourseDAO
from src.db.dependencies import get_course_dao
from src.db.models.utils.types.UuidStr import UuidStr

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)


@router.get(
    "/{course_id}",
    response_model=APIResponse[CourseResponse],
    response_description="Get course by ID",
)
async def get_course_by_id(
    course_id: UuidStr = Path(..., description="Course ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        course = course_dao.get_course_by_id(course_id)
        if course:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Course found",
                data=CourseResponse(courses=[course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Course not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/{user_id}",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by user ID",
)
async def get_courses_by_user_id(
    user_id: UuidStr = Path(..., description="User ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        courses = course_dao.get_courses_by_user_id(user_id)
        if courses:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Courses found",
                data=CourseResponse(courses=courses),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Courses not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/{available_course_id}",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by available courses ID",
)
async def get_courses_by_available_courses_id(
    available_course_id: UuidStr = Path(..., description="Available courses ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        courses = course_dao.get_courses_by_available_courses_id(available_course_id)
        if courses:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Courses found",
                data=CourseResponse(courses=courses),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Courses not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/{grade}",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by grade",
)
async def get_courses_by_grade(
    grade: PositiveFloat = Path(..., description="Grade"),
    user_id: UuidStr = Query(..., description="User ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        courses = course_dao.get_courses_by_grade(grade, user_id)
        if courses:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Courses found",
                data=CourseResponse(courses=courses),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Courses not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.post(
    "/",
    response_model=APIResponse[CourseResponse],
    response_description="Create course",
)
async def create_course(
    available_course_id: UuidStr = Query(..., description="Available courses ID"),
    user_id: UuidStr = Query(..., description="User ID"),
    grade: Optional[PositiveFloat] = Query(None, description="Grade"),
    passed: Optional[bool] = Query(None, description="Passed"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        course = course_dao.create_course(
            {
                "available_course_id": available_course_id,
                "user_id": user_id,
                "grade": grade,
                "passed": passed,
            }
        )
        if course:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Course created",
                data=CourseResponse(courses=[course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Course not created",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.put(
    "/{course_id}",
    response_model=APIResponse[CourseResponse],
    response_description="Update course",
)
async def update_course(
    course_id: UuidStr = Path(..., description="Course ID"),
    available_course_id: Optional[UuidStr] = Query(
        None, description="Available courses ID"
    ),
    user_id: Optional[UuidStr] = Query(None, description="User ID"),
    grade: Optional[PositiveFloat] = Query(None, description="Grade"),
    passed: Optional[bool] = Query(None, description="Passed"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        course_data = {
            "available_course_id": available_course_id,
            "user_id": user_id,
            "grade": grade,
            "passed": passed,
        }

        course_data = {k: v for k, v in course_data.items() if v is not None}

        course = course_dao.update_course(course_id, course_data)
        if course:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Course updated",
                data=CourseResponse(courses=[course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Course not updated",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.delete(
    "/{course_id}",
    response_model=APIResponse[CourseResponse],
    response_description="Delete course",
)
async def delete_course(
    course_id: UuidStr = Path(..., description="Course ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        course = course_dao.delete_course(course_id)
        if course:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Course deleted",
                data=CourseResponse(courses=[course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Course not deleted",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/",
    response_model=APIResponse[CourseResponse],
    response_description="Get all courses",
)
async def get_all_courses(
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        courses = course_dao.get_all_courses()
        if courses:
            return APIResponse[CourseResponse](
                status=status.HTTP_200_OK,
                message="Courses found",
                data=CourseResponse(courses=courses),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Courses not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )
