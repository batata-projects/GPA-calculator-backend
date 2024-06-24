from unittest.mock import Mock

import pytest

from src.controller.routers.users import get_dashboard, users_router
from src.db.dao import CourseDAO, UserDAO
from src.db.models import Course, User


def test_users_router() -> None:
    assert users_router.prefix == "/users"
    assert users_router.tags == ["Users"]


@pytest.mark.asyncio
async def test_get_dashboard_successful(user1: User, course1: Course) -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.return_value = user1
    course_dao.get_by_query.return_value = [course1]

    assert user1.id is not None

    response = await get_dashboard(user1.id, user_dao=user_dao, course_dao=course_dao)

    assert response.status == 200
    assert response.message == "Dashboard data retrieved"

    user1_data = user1.model_dump(exclude={"counted_credits"})
    user1_data["gpa"] = user1.grade / user1.counted_credits

    assert response.data is not None
    assert response.data["user"] == user1_data
    assert response.data["terms"] is not None


@pytest.mark.asyncio
async def test_get_dashboard_user_not_found(valid_uuid: Mock) -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.return_value = None

    response = await get_dashboard(valid_uuid, user_dao=user_dao, course_dao=course_dao)

    assert response.status == 404
    assert response.message == "User not found"
    assert response.data is None


@pytest.mark.asyncio
async def test_get_dashboard_failed() -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.side_effect = Exception("Internal Server Error")

    response = await get_dashboard(Mock(), user_dao=user_dao, course_dao=course_dao)

    assert response.status == 500
    assert response.message == "Internal Server Error"
    assert response.data is None
