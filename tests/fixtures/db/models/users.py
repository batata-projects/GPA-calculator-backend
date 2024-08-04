from unittest.mock import Mock

import pytest

from src.db.models import User


@pytest.fixture
def users(uuid_generator: Mock) -> list[User]:
    return [
        User(
            id=uuid_generator(),
            email="jad@mail.com",
            first_name="Jad",
            last_name="Shaker",
        ),
        User(
            id=uuid_generator(),
            email="rayan@mail.com",
            first_name="Rayan",
            last_name="Fakhreddine",
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
