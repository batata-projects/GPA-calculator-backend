from src.controller.routers._base_router import BaseRouter
from src.controller.schemas import CourseQuery
from src.db.dependencies import get_course_dao
from src.db.models import Course

courses_router = BaseRouter[Course](
    prefix="/courses",
    tags=["Courses"],
    name="Course",
    model=Course,
    query=CourseQuery,
    get_dao=get_course_dao,
).build_router()
