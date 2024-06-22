from fastapi import Depends
from supabase import Client

from src.db.base import get_authenticated_client, get_unauthenticated_client
from src.db.dao import CourseDAO, UserDAO


def get_course_dao(client: Client = Depends(get_authenticated_client)) -> CourseDAO:
    return CourseDAO(client)


def get_user_dao(client: Client = Depends(get_authenticated_client)) -> UserDAO:
    return UserDAO(client)


def get_user_dao_unauthenticated(
    client: Client = Depends(get_unauthenticated_client),
) -> UserDAO:
    return UserDAO(client)
