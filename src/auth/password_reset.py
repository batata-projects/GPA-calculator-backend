from fastapi import Depends, HTTPException, status

from src.auth.dependencies import decode_jwt, get_password_reset_token
from src.auth.schemas import ForgotPasswordRequest, ResetPasswordRequest
from src.db.dao.user_dao import UserDAO
from src.db.models.users import User


def forget_password(request: ForgotPasswordRequest, user_dao: UserDAO) -> str:
    user = user_dao.get_by_query(email=request.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    user_dao.client.auth.reset_password_email(request.email)
    return "Password reset email sent"


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


def reset_password(request: ResetPasswordRequest, user_dao: UserDAO) -> User:
    user_id = user_dao.client.auth.get_user().model_dump()["user"]["id"]
    user = user_dao.get_by_id(user_id)
    with open("test.txt", "w") as file:
        file.write(str(user))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    if user["password"] != request.old_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Old password is incorrect",
        )
    if user["password"] == request.new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from old password",
        )
    if request.new_password != request.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )
    return user_dao.update(user["id"], {"password": request.new_password})
    # user_dao.client.auth.sign_out()
