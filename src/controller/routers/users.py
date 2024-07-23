from fastapi import Depends, status

from src.common.responses import APIResponse
from src.common.utils.types import UuidStr
from src.controller.routers._base_router import BaseRouter
from src.core.user.dashboard import get_dashboard_data
from src.db.dao import CourseDAO, UserDAO
from src.db.dependencies import get_course_dao, get_user_dao
from src.db.models import User

users_router = BaseRouter[User](
    prefix="/users",
    tags=["Users"],
    name="User",
    model=User,
    get_dao=get_user_dao,
).build_router()


@users_router.get("/dashboard/{user_id}")
async def get_dashboard(
    user_id: UuidStr,
    user_dao: UserDAO = Depends(get_user_dao),
    course_dao: CourseDAO = Depends(get_course_dao),
) -> APIResponse:
    try:

        user = user_dao.get_by_id(user_id)
        courses = course_dao.get_by_query(user_id=user_id)

        return APIResponse(
            status_code=status.HTTP_200_OK,
            message="Dashboard data retrieved",
            # data={"user": user_data, "terms": terms},
            data=get_dashboard_data(user, courses),
        )

    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )
