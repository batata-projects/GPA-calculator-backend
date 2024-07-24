from unittest.mock import Mock

import pytest
from src.auth.password_reset import reset_password
from src.auth.schemas import ResetPasswordRequest
from src.common.utils.types import PasswordStr
from src.db.models.users import User
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue.types import User as GoTrueUser

class TestResetPassword:
    async def test_reset_password_successful(self, reset_password_request: ResetPasswordRequest, user1: User, gotrue_user: GoTrueUser) -> None:
        user_dao = Mock()
        user_dao.client.auth.update_user.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=None,
        )

        response = reset_password(reset_password_request, user_dao)

        assert user_dao.client.auth.update_user.called

        assert response.user == user1


    @pytest.mark.parametrize(
        "password",
        [
            "pas",
            "password",
            "PASSWORD",
            "Password",
            "password1",
            "PASSWORD1",
            "Password1",
            "password!",
            "PASSWORD!",
            "Password!",
            "password1!",
            "PASSWORD1!",
            "Password1!",
        ],
    )
    def test_reset_password_invalid_password(self, password: PasswordStr, reset_password_request: ResetPasswordRequest) -> None:
        user_dao = Mock()
        user_dao.client.auth.update_user.side_effect = Exception()

        with pytest.raises(Exception):
            reset_password(ResetPasswordRequest(password="password"), user_dao)

    def test_reset_password_user_not_auth(self) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None

        with pytest.raises(Exception):
            reset_password(ResetPasswordRequest(password="password"), user_dao)
