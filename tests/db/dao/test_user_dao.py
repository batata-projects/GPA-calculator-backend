from unittest.mock import Mock

from supabase import Client

from src.db.dao import BaseDAO, UserDAO


def test__init__user_dao() -> None:
    client = Mock(spec=Client)
    dao = UserDAO(client=client)

    assert isinstance(dao, UserDAO)
    assert isinstance(dao, BaseDAO)
