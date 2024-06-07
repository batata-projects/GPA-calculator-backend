from fastapi import HTTPException, status
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue.errors import AuthApiError  # type: ignore

from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.responses import AuthResponse, Session
from src.db.dao.user_dao import UserDAO
from src.db.models.users import User


def register(request: RegisterRequest, user_dao: UserDAO) -> AuthResponse:
    try:
        if not request.first_name or not request.last_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="First name and last name are required",
            )
        if not request.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is required",
            )
        if user_dao.get_user_by_email(request.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already in use",
            )
        result = user_dao.client.auth.sign_up(request.auth_model_dump())
        user = User.validate_supabase_user(result.user)
        return AuthResponse(user=user)
    except AuthApiError as e:
        if "Password" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character",
            )
        if "Email rate limit exceeded" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email rate limit exceeded, please try again later",
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed, please check your credentials",
        )


def login(request: LoginRequest, user_dao: UserDAO) -> AuthResponse:
    try:
        if not user_dao.get_user_by_email(request.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        result: GoTrueAuthResponse = user_dao.client.auth.sign_in_with_password(
            {
                "email": request.email,
                "password": request.password,
            }
        )
        user = User.validate_supabase_user(result.user)
        session = Session.validate_supabase_session(result.session)
        return AuthResponse(
            user=user,
            session=session,
        )
    except AuthApiError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login failed, please check your credentials",
        )
