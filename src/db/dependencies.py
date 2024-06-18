from fastapi import Depends
from supabase import Client

from src.db.base import (
    get_authenticated_client,
    get_scrapper_client,
    get_unauthenticated_client,
)
from src.db.dao import AvailableCourseDAO, CourseDAO, TermDAO, UserDAO


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


def get_scrapper_terms_dao(client: Client = get_scrapper_client()) -> TermDAO:
    return TermDAO(client)


def get_scrapper_available_courses_dao(
    client: Client = get_scrapper_client(),
) -> AvailableCourseDAO:
    return AvailableCourseDAO(client)
