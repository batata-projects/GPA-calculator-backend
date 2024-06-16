from unittest.mock import Mock

import pytest
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue.types import Session as GoTrueSession  # type: ignore
from gotrue.types import User as GoTrueUser

from src.auth.router import login_route, register_route
from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.responses import AuthResponse


@pytest.mark.asyncio
class TestRegisterRoute:
    async def test_register_route_successful(
        self, register_request: RegisterRequest, gotrue_user: GoTrueUser
    ) -> None:
        user_dao = Mock()
        user_dao.get_user_by_email.return_value = None
        user_dao.client.auth.sign_up.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=None,
        )
        response = await register_route(register_request, user_dao)
        assert response.status == 200
        assert response.message == "Registration successful"
        assert isinstance(response.data, AuthResponse)


@pytest.mark.asyncio
class TestLoginRoute:
    async def test_login_route_successful(
        self,
        login_request: LoginRequest,
        gotrue_user: GoTrueUser,
        gotrue_session: GoTrueSession,
    ) -> None:
        user_dao = Mock()
        user_dao.client.auth.sign_in_with_password.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=gotrue_session,
        )
        response = await login_route(login_request, user_dao)
        assert response.status == 200
        assert response.message == "Login successful"
        assert isinstance(response.data, AuthResponse)
