from src.controller._base.router import BaseRouter
from src.db.dependencies import get_user_dao
from src.db.models import User

users_router = BaseRouter[User](
    prefix="/users",
    tags=["Users"],
    name="User",
    model=User,
    get_dao=get_user_dao,
).build_router()
