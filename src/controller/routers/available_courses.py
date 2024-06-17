from src.controller.routers._base_router import BaseRouter
from src.controller.schemas import AvailableCourseQuery
from src.db.dependencies import get_available_course_dao
from src.db.models import AvailableCourse

available_courses_router = BaseRouter[AvailableCourse](
    prefix="/available-courses",
    tags=["Available Courses"],
    name="Available Course",
    model=AvailableCourse,
    query=AvailableCourseQuery,
    get_dao=get_available_course_dao,
).build_router()
