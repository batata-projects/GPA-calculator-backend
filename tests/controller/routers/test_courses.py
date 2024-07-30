from typing import Any, Dict
from unittest.mock import Mock

import pytest

from src.common.responses.API_response import APIResponse
from src.controller.routers.courses import courses_router, courses_router_class
from src.db.dao.course_dao import CourseDAO


@pytest.mark.asyncio
class TestCoursesRouter:
    def test_courses_router(self) -> None:
        assert courses_router.prefix == "/courses"
        assert courses_router.tags == ["Courses"]


@pytest.mark.asyncio
class TestValidationInRouter:
    async def test_create_course(self, request: Dict[str, Any]):
        course_dao = Mock(spec=CourseDAO)
        response = await courses_router_class.create(request=request, dao=course_dao)
        assert isinstance(response, APIResponse)
        assert response.data["subject"] == request["subject"]
        assert response.data["course_code"] == request["course_code"]

    async def test_create_same_course_different_credits(self, course1):
        course_dao = Mock(spec=CourseDAO)
        course1.credits = 4
        with pytest.raises(ValueError):
            await courses_router_class.create(request=course1, dao=course_dao)
