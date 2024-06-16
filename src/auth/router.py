from fastapi import APIRouter, Depends, status

from src.auth.auth import login, register
from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.responses import APIResponse, AuthResponse
from src.db.dao import UserDAO
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
