from fastapi import HTTPException, status
from gotrue.errors import AuthApiError  # type: ignore

from src.auth.schemas import Credentials
from src.common.responses import AuthResponse
from src.db.dao.user_dao import UserDAO
from src.db.models.users import User


def register(credentials: Credentials, user_dao: UserDAO) -> AuthResponse:
    try:
        if not credentials.first_name or not credentials.last_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="First name and last name are required",
            )
        if not credentials.username and not credentials.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email is required",
            )
        if credentials.email:
            if user_dao.get_user_by_email(credentials.email):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already in use",
                )
        if credentials.username:
            if user_dao.get_user_by_username(credentials.username):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already in use",
                )
        result = user_dao.client.auth.sign_up(credentials.auth_model_dump())
        user = User.validate_supabase_user(result.user)
        return AuthResponse(
            user=user,
            session=result.session,
        )
    except AuthApiError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed, please check your credentials",
        )
