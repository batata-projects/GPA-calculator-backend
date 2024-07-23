from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.routers.users import get_dashboard, users_router
from src.db.dao import CourseDAO, UserDAO
from src.db.models import Course, User


def test_users_router() -> None:
    assert users_router.prefix == "/users"
    assert users_router.tags == ["Users"]


@pytest.mark.asyncio
async def test_get_dashboard_successful(
    user1: User, course1: Course, course2: Course
) -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.return_value = user1
    course_dao.get_by_query.return_value = [course1, course2]

    assert user1.id is not None

    response = await get_dashboard(user1.id, user_dao=user_dao, course_dao=course_dao)
    res = eval(response.body.decode("utf-8"), {"true": True, "false": False})

    assert response.status_code == status.HTTP_200_OK

    term = course1.term

    assert res == {
        "message": "Dashboard data retrieved",
        "data": {
            "terms": {
                str(term): {
                    "courses": {
                        course1.id: course1.model_dump(exclude={"id", "user_id"}),
                        course2.id: course2.model_dump(exclude={"id", "user_id"}),
                    },
                    "credits": course1.credits + course2.credits,
                    "gpa": 4.3,
                    "name": " ".join(map(str, Course.convert_to_term_name(term))),
                }
            },
            "user": {
                "id": user1.id,
                "credits": course1.credits + course2.credits,
                "email": user1.email,
                "first_name": user1.first_name,
                "last_name": user1.last_name,
                "gpa": 4.3,
            },
        },
    }


@pytest.mark.asyncio
async def test_get_dashboard_user_not_found(uuid_generator: Mock) -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.return_value = None

    response = await get_dashboard(
        uuid_generator(), user_dao=user_dao, course_dao=course_dao
    )
    res = eval(response.body.decode("utf-8"))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert res == {"message": "User not found", "data": {}}


@pytest.mark.asyncio
async def test_get_dashboard_failed() -> None:
    user_dao = Mock(spec=UserDAO)
    course_dao = Mock(spec=CourseDAO)
    user_dao.get_by_id.side_effect = Exception("Internal Server Error")

    response = await get_dashboard(Mock(), user_dao=user_dao, course_dao=course_dao)
    res = eval(response.body.decode("utf-8"))

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert res == {"message": "Internal Server Error", "data": {}}
