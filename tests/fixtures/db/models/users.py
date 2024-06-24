from unittest.mock import Mock

import pytest

from src.db.models import User


@pytest.fixture
def users(valid_uuid: Mock) -> list[User]:
    return [
        User(
            id=valid_uuid,
            email="jss31@mail.aub.edu",
            first_name="Jad",
            last_name="Shaker",
            credits=6,
            counted_credits=3,
            grade=12.9,
        ),
        User(
            id=valid_uuid,
            email="rmf40@mail.aub.edu",
            first_name="Rayan",
            last_name="Fakhreddine",
            credits=16,
            counted_credits=15,
            grade=14.0,
        ),
    ]


@pytest.fixture
def user1(users: list[User]) -> User:
    return users[0]


@pytest.fixture
def user2(users: list[User]) -> User:
    return users[1]


@pytest.fixture
def users_same_first_name(
    users: list[User],
) -> list[User]:
    users[0].first_name = users[1].first_name
    return users


@pytest.fixture
def users_same_last_name(
    users: list[User],
) -> list[User]:
    users[0].last_name = users[1].last_name
    return users


@pytest.fixture
def users_same_credits(
    users: list[User],
) -> list[User]:
    users[0].credits = users[1].credits
    return users


@pytest.fixture
def users_same_counted_credits(
    users: list[User],
) -> list[User]:
    users[0].counted_credits = users[1].counted_credits
    return users


@pytest.fixture
def users_same_grade(
    users: list[User],
) -> list[User]:
    users[0].grade = users[1].grade
    return users
