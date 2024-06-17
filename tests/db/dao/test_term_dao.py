from unittest.mock import Mock

from supabase import Client

from src.db.dao import BaseDAO, TermDAO


def test__init__term_dao() -> None:
    client = Mock(spec=Client)
    dao = TermDAO(client=client)

    assert isinstance(dao, TermDAO)
    assert isinstance(dao, BaseDAO)
