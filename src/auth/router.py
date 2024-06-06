from fastapi import APIRouter, Depends, status

from src.auth.auth import register
from src.auth.schemas import Credentials
from src.common.responses import APIResponse, AuthResponse
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import get_user_dao_unauthenticated

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=APIResponse,
    summary="Login",
    description="Login to the system",
)
async def login_route():
    return APIResponse(message="Login successful", status=status.HTTP_200_OK)


@router.post(
    "/register",
    response_model=APIResponse[AuthResponse],
    summary="Register",
    description="Register a new user",
)
async def register_route(
    credentials: Credentials,
    user_dao: UserDAO = Depends(get_user_dao_unauthenticated),
):
    return APIResponse(
        message="Registration successful",
        status=status.HTTP_200_OK,
        data=register(credentials, user_dao),
    )
