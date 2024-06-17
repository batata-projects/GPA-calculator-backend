from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.users import UserRequest, UserResponse
from src.controller.users.router import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users_by_query,
    update_user,
)
from src.db.dao import UserDAO
from src.db.models import User


@pytest.mark.asyncio
class TestGetUserById:
    async def test_get_user_by_id_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_id.return_value = user1

        assert user1.id is not None

        response = await get_user_by_id(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "User found"
        assert response.data == UserResponse(items=[user1])

    async def test_get_user_by_id_not_found(self, valid_uuid: Mock) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_id.return_value = None

        response = await get_user_by_id(user_id=str(valid_uuid), user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not found"
        assert response.data is None

    async def test_get_user_by_id_error(self, valid_uuid: Mock) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_id.side_effect = Exception("Error")

        response = await get_user_by_id(user_id=str(valid_uuid), user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetUsersByQuery:
    async def test_get_users_by_query_successful(
        self, user1: User, user2: User
    ) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_query.return_value = [user1, user2]

        response = await get_users_by_query(user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Users found"
        assert response.data == UserResponse(items=[user1, user2])

    async def test_get_users_by_query_not_found(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_query.return_value = []

        response = await get_users_by_query(user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Users not found"
        assert response.data is None

    async def test_get_users_by_query_error(self) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.get_by_query.side_effect = Exception("Error")

        response = await get_users_by_query(user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestCreateUser:
    async def test_create_user_successful(
        self, user1: User, user_request: UserRequest
    ) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create.return_value = user1

        response = await create_user(user_request, user_dao)

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "User created"
        assert response.data == UserResponse(items=[user1])

    async def test_create_user_fail(self, user_request: UserRequest) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create.return_value = None

        response = await create_user(user_request, user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not created"
        assert response.data is None

    async def test_create_user_error(self, user_request: UserRequest) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.create.side_effect = Exception("Error")

        response = await create_user(user_request, user_dao)
        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestUpdateUser:
    async def test_update_user_successful(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user1.username = "new_username"
        user_dao.update.return_value = user1

        assert user1.id is not None

        response = await update_user(
            user_id=user1.id, username=user1.username, user_dao=user_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "User updated"
        assert response.data == UserResponse(items=[user1])

    async def test_update_user_not_found(
        self,
        user1: User,
    ) -> None:
        user_dao = Mock(spec=UserDAO)
        user1.username = "new_username"
        user_dao.update.return_value = None
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
        user_dao.update.return_value = Exception("Error")
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
        user_dao.delete.return_value = user1
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "User deleted"
        assert response.data == UserResponse(items=[user1])

    async def test_delete_user_not_found(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.delete.return_value = None
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "User not deleted"
        assert response.data is None

    async def test_delete_user_error(self, user1: User) -> None:
        user_dao = Mock(spec=UserDAO)
        user_dao.delete.side_effect = Exception("Error")
        assert user1.id is not None
        response = await delete_user(user_id=user1.id, user_dao=user_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None
