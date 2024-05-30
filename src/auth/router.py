from fastapi import APIRouter, status

from src.common.responses import APIResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=APIResponse,
    summary="Login",
    description="Login to the system",
)
async def login_route():
    return APIResponse(
        message="Login successful",
        status=status.HTTP_200_OK,
    )
