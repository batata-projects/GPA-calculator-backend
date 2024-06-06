from fastapi import Depends
from supabase import Client

from src.db.base import get_authenticated_client, get_unauthenticated_client
from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.dao.course_dao import CourseDAO
from src.db.dao.term_dao import TermDAO
from src.db.dao.user_dao import UserDAO


# ! Check if this is a good approach for auth/unauth
def get_available_course_dao(
    client: Client = Depends(get_authenticated_client),
) -> AvailableCourseDAO:
    return AvailableCourseDAO(client)


def get_term_dao(client: Client = Depends(get_authenticated_client)) -> TermDAO:
    return TermDAO(client)


def get_course_dao(client: Client = Depends(get_authenticated_client)) -> CourseDAO:
    return CourseDAO(client)


def get_user_dao(client: Client = Depends(get_authenticated_client)) -> UserDAO:
    return UserDAO(client)


def get_user_dao_unauthenticated(
    client: Client = Depends(get_unauthenticated_client),
) -> UserDAO:
    return UserDAO(client)
