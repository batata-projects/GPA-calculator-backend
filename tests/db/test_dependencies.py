from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.dao.course_dao import CourseDAO
from src.db.dao.term_dao import TermDAO
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import (
    get_available_course_dao,
    get_course_dao,
    get_term_dao,
    get_user_dao,
    get_user_dao_unauthenticated,
)


# Test for get_available_course_dao
def test_get_available_course_dao(mock_authenticated_client) -> None:
    dao = get_available_course_dao()
    assert isinstance(dao, AvailableCourseDAO)
    # assert dao.client == mock_authenticated_client


# Test for get_term_dao
def test_get_term_dao(mock_authenticated_client) -> None:
    dao = get_term_dao()
    assert isinstance(dao, TermDAO)
    # assert dao.client == mock_authenticated_client


# Test for get_course_dao
def test_get_course_dao(mock_authenticated_client) -> None:
    dao = get_course_dao()
    assert isinstance(dao, CourseDAO)
    # assert dao.client == mock_authenticated_client


# Test for get_user_dao
def test_get_user_dao(mock_authenticated_client) -> None:
    dao = get_user_dao()
    assert isinstance(dao, UserDAO)
    # assert dao.client == mock_authenticated_client


# Test for get_user_dao_unauthenticated
def test_get_user_dao_unauthenticated(mock_unauthenticated_client) -> None:
    dao = get_user_dao_unauthenticated()
    assert isinstance(dao, UserDAO)
    # assert dao.client == mock_unauthenticated_client
