from fastapi import APIRouter, status

from src.common.responses import APIResponse

router = APIRouter(
    prefix="/status",
    tags=["status"],
)


@router.get(
    "",
    response_model=APIResponse,
    response_description="Status check",
    responses={
        status.HTTP_200_OK: {"description": "Status check successful"},
        status.HTTP_404_NOT_FOUND: {"description": "Status check failed"},
    },
)
async def status_check():
    return APIResponse[None](
        status=status.HTTP_200_OK, message="Status check successful", data=None
    )
