import pytest

from src.controller.users import UserResponse
from src.db.models import User


class TestUserResponse:
    def test_user_response_successful(self, user1: User) -> None:
        user_response = UserResponse(items=[user1])
        assert user_response.items == [user1]

    def test_user_response_empty(self) -> None:
        user_response = UserResponse()
        assert user_response.items == []

    def test_user_multiple_users(self, user1: User, user2: User) -> None:
        user_response = UserResponse(items=[user1, user2])
        assert user_response.items == [user1, user2]

    def test_user_response_invalid_user(self) -> None:
        with pytest.raises(ValueError):
            UserResponse(items=[{"name": "User 1"}])  # type: ignore
