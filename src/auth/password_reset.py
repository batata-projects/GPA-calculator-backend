from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.schemas import ResetPasswordRequest
from src.common.responses.API_response import APIResponse
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import get_user_dao_unauthenticated


router = APIRouter(prefix="/pass", tags=["Password Reset"])

@router.post(
    "/reset",
    response_model=APIResponse,
    summary="Reset Password",
    description="Reset user password",
)
async def forgot_password_route(request: ResetPasswordRequest, user_dao: UserDAO = Depends(get_user_dao_unauthenticated),) -> APIResponse:
    return APIResponse(
        message="Password reset successful",
        status=status.HTTP_200_OK,
        data=reset_password(request, user_dao)
    )

def reset_password(request: ResetPasswordRequest, user_dao: UserDAO):
    # Check if user exists
    user = user_dao.get_user_by_email(request.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # TODO: Generate reset password token
    # TODO: Send reset password email
    # TODO: Update user password
    
    return None
