import pytest

from src.controller.routers._base_router import BaseRouter
from src.controller.routers.courses import courses_router
from src.db.models.courses import Course
from tests.fixtures.db.dao._base_dao import TestDAO
from tests.fixtures.db.models._base_model import TestObject


@pytest.mark.asyncio
class TestCoursesRouter:
    def test_courses_router(self) -> None:
        assert courses_router.prefix == "/courses"
        assert courses_router.tags == ["Courses"]


@pytest.mark.asyncio
class TestValidationInCreate:
    async def test_create_same_course_same_credits(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        course1: Course,
    ) -> None: ...

    async def test_create_same_course_different_credits(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        course1: Course,
    ) -> None: ...
