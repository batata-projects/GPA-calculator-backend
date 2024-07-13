from fastapi import APIRouter, Depends, status

from src.auth.auth import login, register
from src.auth.password_reset import forget_password, reset_password
from src.auth.schemas import (
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
)
from src.common.responses import APIResponse
from src.common.responses.API_response import APIResponse
from src.db.dao import UserDAO
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import get_user_dao, get_user_dao_unauthenticated

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post(
    "/register",
    response_class=APIResponse,
    summary="Register",
    description="Register a new user",
)
async def register_route(
    request: RegisterRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse:
    return APIResponse(
        message="Registration successful",
        status_code=status.HTTP_200_OK,
        data=register(request, user_dao).model_dump(),
    )


@auth_router.post(
    "/login",
    response_class=APIResponse,
    summary="Login",
    description="Login to the system",
)
async def login_route(
    request: LoginRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse:
    return APIResponse(
        message="Login successful",
        status_code=status.HTTP_200_OK,
        data=login(request, user_dao).model_dump(),
    )


@auth_router.post(
    "/forgot-password",
    response_class=APIResponse,
    summary="Reset Password",
    description="Reset user password",
)
async def forgot_password_route(
    request: ForgotPasswordRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse:
    return APIResponse(
        message="Password reset successful",
        status_code=status.HTTP_200_OK,
        data=forget_password(request, user_dao).model_dump(),
    )


@auth_router.post(
    "/reset-password",
    response_class=APIResponse,
    summary="Change Password",
    description="Change user password",
)
async def reset_password_route(
    request: ResetPasswordRequest,
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse:
    return APIResponse(
        message="Password change successful",
        status_code=status.HTTP_200_OK,
        data=reset_password(request, user_dao).model_dump(),
    )
