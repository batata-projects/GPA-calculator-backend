from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    summary="Login",
    description="Login to the system",
)
async def login_route():
    return {"token": "dummy_token"}
