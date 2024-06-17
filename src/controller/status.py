from fastapi import APIRouter, status

from src.common.responses import APIResponse

status_router = APIRouter(
    prefix="/status",
    tags=["Status"],
)


@status_router.get(
    "",
    response_model=APIResponse[None],
    response_description="Status check",
    responses={
        status.HTTP_200_OK: {"description": "Status check successful"},
        status.HTTP_404_NOT_FOUND: {"description": "Status check failed"},
    },
)
async def status_check() -> APIResponse[None]:
    return APIResponse[None](
        status=status.HTTP_200_OK, message="Status check successful", data=None
    )
