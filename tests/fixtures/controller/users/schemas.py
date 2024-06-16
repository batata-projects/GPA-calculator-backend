import pytest

from src.controller.users import UserRequest
from src.db.models import User


@pytest.fixture
def user_request(user1: User) -> UserRequest:
    return UserRequest(
        email=user1.email,
        username=user1.username,
        first_name=user1.first_name,
        last_name=user1.last_name,
        credits=user1.credits,
        grade=user1.grade,
    )
