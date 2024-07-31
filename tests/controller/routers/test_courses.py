import pytest
from fastapi import status

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
    ) -> None:
        # Test creating a course with the same subject and course_code but different credits
        # It should be successful
        response = await router_successful.create(
            course1.model_dump(), test_dao_successful
        )

        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_201_CREATED
        assert res == {
            "message": "course created",
            "data": {"item": course1.model_dump()},
        }

    async def test_create_same_course_different_credits(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        course1: Course,
    ) -> None:
        # Test creating a course with the same subject and course_code but different credits
        # It should raise a ValueError
        course1.credits = 4
        response = await router_successful.create(
            course1.model_dump(), test_dao_successful
        )

        res = eval(response.body.decode("utf-8"))
        print(res)
        with pytest.raises(ValueError):
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            # assert res == {"message": "Course already exists with different credit value"}
