from unittest.mock import Mock

from supabase import Client

from src.db.dao import AvailableCourseDAO, BaseDAO


def test__init__available_course_dao() -> None:
    client = Mock(spec=Client)
    dao = AvailableCourseDAO(client=client)

    assert isinstance(dao, AvailableCourseDAO)
    assert isinstance(dao, BaseDAO)
