from unittest.mock import Mock

import pytest

from src.db.models.users import User


@pytest.fixture
def users(uuid4: Mock) -> list[User]:
    return [
        User(
            id=str(uuid4()),
            email="jss31@mail.aub.edu",
            username="Jad",
            first_name="Jad",
            last_name="Shaker",
            credits=12,
            counted_credits=15,
            grade=15.0,
        ),
        User(
            id=str(uuid4()),
            email="ld06@aub.edu.lb",
            username="Lara",
            first_name="Lara",
            last_name="Dagher",
            credits=15,
            counted_credits=15,
            grade=14.0,
        ),
    ]


@pytest.fixture
def users_same_email(
    users: list[User],
) -> list[User]:
    users[1].email = users[0].email
    return users


@pytest.fixture
def users_same_username(
    users: list[User],
) -> list[User]:
    users[1].username = users[0].username
    return users


@pytest.fixture
def users_same_first_name(
    users: list[User],
) -> list[User]:
    users[1].first_name = users[0].first_name
    return users


@pytest.fixture
def users_same_last_name(
    users: list[User],
) -> list[User]:
    users[1].last_name = users[0].last_name
    return users


@pytest.fixture
def users_same_credits(
    users: list[User],
) -> list[User]:
    users[1].credits = users[0].credits
    return users


@pytest.fixture
def users_same_counted_credits(
    users: list[User],
) -> list[User]:
    users[1].counted_credits = users[0].counted_credits
    return users


@pytest.fixture
def users_same_grade(
    users: list[User],
) -> list[User]:
    users[1].grade = users[0].grade
    return users
