from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.users.router import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
    get_user_by_username,
    update_user,
)
from src.controller.users.schemas import UserResponse
from src.db.dao.user_dao import UserDAO
from src.db.models.users import User


@pytest.mark.asyncio
class TestGetUserById:
    async def test_get_user_by_id_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_id.return_value = user1

        assert user1.id is not None

        response = await get_user_by_id(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "User found"
        assert response.data == UserResponse(users=[user1])

    async def test_get_user_by_id_not_found(self, uuid4: Mock) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_id.return_value = None

        response = await get_user_by_id(user_id=str(uuid4()), user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not found"
        assert response.data is None

    async def test_get_user_by_id_error(self, uuid4: Mock) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_id.side_effect = Exception("Error")

        response = await get_user_by_id(user_id=str(uuid4()), user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetUserByEmail:
    async def test_get_user_by_email_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_email.return_value = user1

        assert user1.email is not None

        response = await get_user_by_email(email=user1.email, user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "User found"
        assert response.data == UserResponse(users=[user1])

    async def test_get_user_by_email_not_found(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_email.return_value = None

        response = await get_user_by_email(email="eg@mail.aub.edu", user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not found"
        assert response.data is None

    async def test_get_user_by_email_error(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_email.side_effect = Exception("Error")

        response = await get_user_by_email(
            email="rmf40@mail.aub.edu", user_dao=user_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetUserByUsername:
    async def test_get_user_by_username_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_username.return_value = user1

        assert user1.username is not None

        response = await get_user_by_username(
            username=user1.username, user_dao=user_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "User found"
        assert response.data == UserResponse(users=[user1])

    async def test_get_user_by_username_not_found(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_username.return_value = None

        response = await get_user_by_username(username="rmf40", user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not found"
        assert response.data is None

    async def test_get_user_by_username_error(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_user_by_username.side_effect = Exception("Error")

        response = await get_user_by_username(username="rmf40", user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetAllUsers:
    async def test_get_all_users_successful(self, user1: User, user2: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_all_users.return_value = [user1, user2]

        response = await get_all_users(user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Users found"
        assert response.data == UserResponse(users=[user1, user2])

    async def test_get_all_users_not_found(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_all_users.return_value = []

        response = await get_all_users(user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Users not found"
        assert response.data is None

    async def test_get_all_users_error(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_all_users.side_effect = Exception("Error")

        response = await get_all_users(user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestCreateUser:
    async def test_create_user_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create_user.return_value = user1

        response = await create_user(
            username=user1.username,
            email=user1.email,
            first_name=user1.first_name,
            last_name=user1.last_name,
            credits=user1.credits,
            counted_credits=user1.counted_credits,
            grade=user1.grade,
            user_dao=user_dao,
        )

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "User created"
        assert response.data == UserResponse(users=[user1])

    async def test_create_user_duplicate(self, user1: User, user2: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create_user.return_value = None

        response = await create_user(
            username=user1.username,
            email=user1.email,
            first_name=user1.first_name,
            last_name=user1.last_name,
            credits=user1.credits,
            counted_credits=user1.counted_credits,
            grade=user1.grade,
            user_dao=user_dao,
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not created"
        assert response.data is None

    async def test_create_user_error(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create_user.side_effect = Exception("Error")

        response = await create_user(
            username=user1.username,
            email=user1.email,
            first_name=user1.first_name,
            last_name=user1.last_name,
            credits=user1.credits,
            counted_credits=user1.counted_credits,
            grade=user1.grade,
            user_dao=user_dao,
        )
        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestUpdateUser:
    async def test_update_user_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user1.username = "new_username"
        user_dao.update_user.return_value = user1

        assert user1.id is not None

        response = await update_user(
            user_id=user1.id, username=user1.username, user_dao=user_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "User updated"
        assert response.data == UserResponse(users=[user1])

    async def test_update_user_not_found(
        self,
        user1: User,
    ) -> None:
        user_dao = Mock(spec=UserDAO)
        user1.username = "new_username"
        user_dao.update_user.return_value = None
        assert user1.id is not None
        response = await update_user(
            user_id=user1.id, username=user1.username, user_dao=user_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not updated"
        assert response.data is None

    async def test_update_user_error(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user1.username = "new_username"
        user_dao.update_user.return_value = Exception("Error")
        assert user1.id is not None
        response = await update_user(
            user_id=user1.id, username=user1.username, user_dao=user_dao
        )
        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "error" in response.message
        assert response.data is None


@pytest.mark.asyncio
class TestDeleteUser:
    async def test_delete_user_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.delete_user.return_value = user1
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "User deleted"
        assert response.data == UserResponse(users=[user1])

    async def test_delete_user_not_found(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.delete_user.return_value = None
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not deleted"
        assert response.data is None

    async def test_delete_user_error(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.delete_user.side_effect = Exception("Error")
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None
