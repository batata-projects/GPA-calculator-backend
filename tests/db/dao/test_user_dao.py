from unittest.mock import Mock

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

        result = user_dao.get_by_id(user1.id)

        assert result == user1

    def test_create_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).insert(
            user1.model_dump()
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        result = user_dao.create(user1.model_dump())

        assert result == user1

    def test_update_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).update(user1.model_dump()).eq(
            "id", user1.id
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        assert user1.id is not None

        result = user_dao.update(user1.id, user1.model_dump())

        assert result == user1

    def test_delete_user_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).delete().eq(
            "id", user1.id
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        assert user1.id is not None

        result = user_dao.delete(user1.id)

        assert result == user1

    def test_get_user_by_query_successful(self, user1: User) -> None:
        mock_client = Mock(spec=Client)
        user_dao = UserDAO(mock_client)

        mock_client.table(SupabaseTables.USERS).select("*").eq(
            "email", user1.email
        ).execute.return_value = APIResponse(data=[user1.model_dump()], count=None)

        result = user_dao.get_by_query(email=user1.email)

        assert result == [user1]
