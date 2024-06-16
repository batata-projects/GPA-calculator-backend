from .available_courses.router import router as available_courses_router
from .courses.router import router as courses_router
from .status import router as status_router
from .terms.router import router as terms_router
from .users.router import router as users_router

__all__ = [
    "available_courses_router",
    "courses_router",
    "status_router",
    "terms_router",
    "users_router",
]
