from typing import Optional

from fastapi import APIRouter, Depends, Path, Query, status
from pydantic import NonNegativeInt

from src.common.responses import APIResponse
from src.common.utils.types import CourseCodeStr, CourseNameStr, UuidStr
from src.controller.available_courses import (
    AvailableCourseRequest,
    AvailableCourseResponse,
)
from src.db.dao import AvailableCourseDAO
from src.db.dependencies import get_available_course_dao

router = APIRouter(
    prefix="/available-courses",
    tags=["Available Courses"]
    )


@router.get(
    "/",
    response_model=APIResponse[AvailableCourseResponse],
    response_description="Get available courses by query",
)
async def get_available_courses_by_query(
    term_id: Optional[UuidStr] = Query(None, description="Term ID"),
    name: Optional[CourseNameStr] = Query(None, description="Course name"),
    code: Optional[CourseCodeStr] = Query(None, description="Course code"),
    credits: Optional[NonNegativeInt] = Query(None, description="Credit"),
    graded: Optional[bool] = Query(None, description="Graded"),
    available_course_dao: AvailableCourseDAO = Depends(get_available_course_dao),
) -> APIResponse[AvailableCourseResponse]:
    try:
        available_courses = available_course_dao.get_available_courses_by_query(
            term_id, name, code, credits, graded
        )
        if available_courses:
            return APIResponse[AvailableCourseResponse](
                status=status.HTTP_200_OK,
                message="Available courses found",
                data=AvailableCourseResponse(available_courses=available_courses),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND, message="Available courses not found"
        )
    except Exception as e:
        return APIResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))


@router.post(
    "/",
    response_model=APIResponse[AvailableCourseResponse],
    response_description="Create available course",
)
async def create_available_course(
    request: AvailableCourseRequest,
    available_course_dao: AvailableCourseDAO = Depends(get_available_course_dao),
) -> APIResponse[AvailableCourseResponse]:
    try:
        available_course = available_course_dao.create_available_course(
            request.model_dump()
        )
        if available_course:
            return APIResponse[AvailableCourseResponse](
                status=status.HTTP_201_CREATED,
                message="Available course created",
                data=AvailableCourseResponse(available_courses=[available_course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND, message="Available course not created"
        )
    except Exception as e:
        return APIResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))


@router.get(
    "/{available_course_id}",
    response_model=APIResponse[AvailableCourseResponse],
    response_description="Get available course by id",
)
async def get_available_course_by_id(
    available_course_id: UuidStr = Path(..., description="Available Course ID"),
    available_course_dao: AvailableCourseDAO = Depends(get_available_course_dao),
) -> APIResponse[AvailableCourseResponse]:
    try:
        available_course = available_course_dao.get_available_course_by_id(
            available_course_id
        )
        if available_course:
            return APIResponse[AvailableCourseResponse](
                status=status.HTTP_200_OK,
                message="Available course found",
                data=AvailableCourseResponse(available_courses=[available_course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND, message="Available course not found"
        )
    except Exception as e:
        return APIResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))


@router.put(
    "/{available_course_id}",
    response_model=APIResponse[AvailableCourseResponse],
    response_description="Update available course",
)
async def update_available_course(
    available_course_id: UuidStr = Path(..., description="Available Course ID"),
    term_id: Optional[UuidStr] = Query(None, description="Term ID"),
    name: Optional[CourseNameStr] = Query(None, description="Course name"),
    code: Optional[CourseCodeStr] = Query(None, description="Course code"),
    credits: Optional[NonNegativeInt] = Query(None, description="Credit"),
    graded: Optional[bool] = Query(None, description="Graded"),
    available_course_dao: AvailableCourseDAO = Depends(get_available_course_dao),
) -> APIResponse[AvailableCourseResponse]:
    try:
        available_course_data = {
            "term_id": term_id,
            "name": name,
            "code": code,
            "credits": credits,
            "graded": graded,
        }

        available_course_data = {
            k: v for k, v in available_course_data.items() if v is not None
        }

        available_course = available_course_dao.update_available_course(
            available_course_id, available_course_data
        )
        if available_course:
            return APIResponse[AvailableCourseResponse](
                status=status.HTTP_200_OK,
                message="Available course updated",
                data=AvailableCourseResponse(available_courses=[available_course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND, message="Available course not updated"
        )
    except Exception as e:
        return APIResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))


@router.delete(
    "/{available_course_id}",
    response_model=APIResponse[AvailableCourseResponse],
    response_description="Delete available course",
)
async def delete_available_course(
    available_course_id: UuidStr = Path(..., description="Available Course ID"),
    available_course_dao: AvailableCourseDAO = Depends(get_available_course_dao),
) -> APIResponse[AvailableCourseResponse]:
    try:
        available_course = available_course_dao.delete_available_course(
            available_course_id
        )
        if available_course:
            return APIResponse[AvailableCourseResponse](
                status=status.HTTP_200_OK,
                message="Available course deleted",
                data=AvailableCourseResponse(available_courses=[available_course]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND, message="Available course not deleted"
        )
    except Exception as e:
        return APIResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))
