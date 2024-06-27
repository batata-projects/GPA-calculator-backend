from fastapi import APIRouter, Depends, status

from src.auth.auth import login, register
from src.auth.password_reset import forget_password
from src.auth.schemas import LoginRequest, RegisterRequest, ResetPasswordRequest
from src.common.responses import APIResponse, AuthResponse
from src.common.responses.API_response import APIResponse
from src.db.dao import UserDAO
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import get_user_dao_unauthenticated

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=APIResponse[AuthResponse],
    summary="Register",
    description="Register a new user",
)
async def register_route(
    request: RegisterRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse[AuthResponse]:
    return APIResponse[AuthResponse](
        message="Registration successful",
        status=status.HTTP_200_OK,
        data=register(request, user_dao),
    )


@router.post(
    "/login",
    response_model=APIResponse[AuthResponse],
    summary="Login",
    description="Login to the system",
)
async def login_route(
    request: LoginRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse[AuthResponse]:
    return APIResponse[AuthResponse](
        message="Login successful",
        status=status.HTTP_200_OK,
        data=login(request, user_dao),
    )


@router.post(
    "/forgot-password",
    response_model=APIResponse,
    summary="Reset Password",
    description="Reset user password",
)
async def forgot_password_route(
    request: ResetPasswordRequest,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
) -> APIResponse[None]:
    return APIResponse(
        message="Password reset successful",
        status=status.HTTP_200_OK,
        data=forget_password(request, user_dao)
    )
