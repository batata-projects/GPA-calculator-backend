from unittest.mock import Mock

from supabase import Client

from src.db.dao import BaseDAO, CourseDAO


def test__init__course_dao() -> None:
    client = Mock(spec=Client)
    dao = CourseDAO(client=client)

    assert isinstance(dao, CourseDAO)
    assert isinstance(dao, BaseDAO)
