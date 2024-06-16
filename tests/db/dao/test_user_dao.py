from unittest.mock import Mock

import pytest
from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao import UserDAO
from src.db.models import User
from src.db.tables import SupabaseTables


class TestUserDAO:
    def test_get_user_by_id_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).select("*").eq(
            "id", user1.id
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        assert user1.id is not None

        result = user_dao.get_user_by_id(user1.id)

        assert result == user1

    @pytest.mark.parametrize(
        "method, method_arg, query_methods, query_return, attribute_name",
        [
            (
                "get_user_by_email",
                ["users[0].email"],
                ["select", "eq"],
                "user1",
                "email",
            ),
            (
                "get_user_by_username",
                ["users_same_username[0].username"],
                ["select", "eq"],
                "user2",
                "username",
            ),
        ],
    )
    def test_get_user_by_attribute_successful(
        self,
        method: str,
        method_arg: list[str],
        query_methods: list[str],
        query_return: str,
        attribute_name: str,
        request: pytest.FixtureRequest,
    ) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_obj = mock_client.table(SupabaseTables.USERS)
        for method_name in query_methods:
            mock_method = getattr(mock_obj, method_name)
            mock_obj = mock_method()

        mock_obj.execute.return_value = APIResponse(
            data=[request.getfixturevalue(query_return).model_dump()],
            count=None,
        )

        result = getattr(user_dao, method)(*method_arg)

        assert result == request.getfixturevalue(query_return)

    def test_create_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).insert(
            user1.model_dump()
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        result = user_dao.create_user(user1.model_dump())

        assert result == user1

    def test_update_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).update(user1.model_dump()).eq(
            "id", user1.id
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        assert user1.id is not None

        result = user_dao.update_user(user1.id, user1.model_dump())

        assert result == user1

    def test_delete_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).delete().eq(
            "id", user1.id
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        assert user1.id is not None

        result = user_dao.delete_user(user1.id)

        assert result == user1

    def test_get_user_by_query_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).select("*").eq(
            "email", user1.email
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        result = user_dao.get_users_by_query(email=user1.email)

        assert result == [user1]
