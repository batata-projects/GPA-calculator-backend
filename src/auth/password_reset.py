from fastapi import Depends, HTTPException, status

from src.auth.dependencies import decode_jwt, get_password_reset_token
from src.auth.schemas import ForgotPasswordRequest, ResetPasswordRequest
from src.common.responses import AuthResponse
from src.db.dao import UserDAO
from src.db.models import User


def forget_password(request: ForgotPasswordRequest, user_dao: UserDAO) -> AuthResponse:
    user = user_dao.get_by_query(email=request.email)[0]
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    user_dao.client.auth.reset_password_email(request.email)
    return AuthResponse(user=user)


def change_password(
    user_dao: UserDAO, token: str = Depends(get_password_reset_token)
) -> dict[str, str]:
    decoded_token = decode_jwt(token)
    email = decoded_token.get("email")
    user = user_dao.get_by_query(email=email)[0]
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    assert user.id is not None
    user_dao.update(user.id, {"password": decoded_token.get("password")})
    return {"message": "Password updated"}


def reset_password(request: ResetPasswordRequest, user_dao: UserDAO) -> AuthResponse:
    response = user_dao.client.auth.update_user({"password": request.password})
    user = User.validate_supabase_user(response.user)
    return AuthResponse(user=user)
