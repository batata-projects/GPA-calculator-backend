from fastapi import HTTPException, status

from src.auth.schemas import ResetPasswordRequest
from src.db.dao.user_dao import UserDAO


def forget_password(request: ResetPasswordRequest, user_dao: UserDAO) -> None:
    user = user_dao.get_by_query(email=request.email)
    user_dao.client.auth.reset_password_email(request.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return None
