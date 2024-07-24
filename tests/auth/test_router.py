from unittest.mock import Mock

import pytest
from fastapi import status
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue.types import Session as GoTrueSession  # type: ignore
from gotrue.types import User as GoTrueUser

from src.auth.router import login_route, register_route, reset_password_route
from src.auth.schemas import LoginRequest, RegisterRequest, ResetPasswordRequest
from src.common.session import Session
from src.db.dao.user_dao import UserDAO
from src.db.models import User


@pytest.mark.asyncio
class TestRegisterRoute:
    async def test_register_route_successful(
        self, register_request: RegisterRequest, gotrue_user: GoTrueUser, user1: User
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None
        user_dao.client.auth.sign_up.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=None,
        )
        response = await register_route(register_request, user_dao)
        res = eval(response.body.decode("utf-8"), {"null": None})

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Registration successful",
            "data": {"user": user1.model_dump(), "session": None},
        }


@pytest.mark.asyncio
class TestLoginRoute:
    async def test_login_route_successful(
        self,
        login_request: LoginRequest,
        gotrue_user: GoTrueUser,
        gotrue_session: GoTrueSession,
        user1: User,
        session: Session,
    ) -> None:
        user_dao = Mock()
        user_dao.client.auth.sign_in_with_password.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=gotrue_session,
        )
        response = await login_route(login_request, user_dao)
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Login successful",
            "data": {
                "user": user1.model_dump(),
                "session": session.model_dump(),
            },
        }

@pytest.mark.asyncio
class TestResetPasswordRoute:
    async def test_reset_password_route_successful(
        self, reset_password_request: ResetPasswordRequest, gotrue_user: GoTrueUser, user1: User
    ) -> None:
        user_dao = Mock()
        user_dao.client.auth.reset_password.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=None,
        )
        response = await reset_password_route(reset_password_request, user_dao)
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Password change successful",
            "data": {"user" : user1.model_dump()},
        }