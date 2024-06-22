from unittest.mock import Mock

from src.db.dao import CourseDAO, UserDAO
from src.db.dependencies import (
    get_course_dao,
    get_user_dao,
    get_user_dao_unauthenticated,
)


def test_get_course_dao_successful() -> None:
    client = Mock()
    dao = get_course_dao(client)
    assert isinstance(dao, CourseDAO)
    assert dao.client == client


def test_get_user_dao_successful() -> None:
    client = Mock()
    dao = get_user_dao(client)
    assert isinstance(dao, UserDAO)
    assert dao.client == client


def test_get_user_dao_unauthenticated_successful() -> None:
    client = Mock()
    dao = get_user_dao_unauthenticated(client)
    assert isinstance(dao, UserDAO)
    assert dao.client == client
