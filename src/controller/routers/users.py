from src.controller.routers._base_router import BaseRouter
from src.controller.schemas import UserQuery
from src.db.dependencies import get_user_dao
from src.db.models import User

users_router = BaseRouter[User](
    prefix="/users",
    tags=["Users"],
    name="User",
    model=User,
    query=UserQuery,
    get_dao=get_user_dao,
).build_router()
