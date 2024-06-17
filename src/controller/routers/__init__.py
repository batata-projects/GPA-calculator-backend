from .available_courses import available_courses_router
from .courses import courses_router
from .terms import terms_router
from .users import users_router

__all__ = [
    "available_courses_router",
    "courses_router",
    "terms_router",
    "users_router",
]
