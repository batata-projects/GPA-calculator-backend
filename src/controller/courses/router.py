from fastapi import APIRouter, Depends, Path, Query, status
from pydantic import PositiveFloat

from src.common.responses import APIResponse
from src.controller.courses.schemas import CourseResponse
from src.db.dao.course_dao import CourseDAO
from src.db.dependencies import get_course_dao
from src.db.models.utils import UuidStr

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
    "/user-id/",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by user ID",
)
async def get_courses_by_user_id(
    user_id: UuidStr = Query(..., description="User ID"),
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
    "/available-courses/",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by available courses ID",
)
async def get_courses_by_available_courses_id(
    available_courses_id: UuidStr = Query(..., description="Available courses ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        courses = course_dao.get_courses_by_available_courses_id(available_courses_id)
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
    "/grade/",
    response_model=APIResponse[CourseResponse],
    response_description="Get courses by grade",
)
async def get_courses_by_grade(
    grade: PositiveFloat = Query(..., description="Grade"),
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
    course_data: dict,
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
        course = course_dao.create_course(course_data)
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
    "/",
    response_model=APIResponse[CourseResponse],
    response_description="Update course",
)
async def update_course(
    course_data: dict,
    course_id: UuidStr = Query(..., description="Course ID"),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse[CourseResponse]:
    try:
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
    "/",
    response_model=APIResponse[CourseResponse],
    response_description="Delete course",
)
async def delete_course(
    course_id: UuidStr = Query(..., description="Course ID"),
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
