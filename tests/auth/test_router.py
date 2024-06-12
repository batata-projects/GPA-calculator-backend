from unittest.mock import Mock

import pytest

from src.auth.router import login_route, register_route
from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.responses import AuthResponse
from src.db.dao.user_dao import UserDAO


# test register route and login route
@pytest.mark.asyncio
class TestRegisterRoute:
    async def test_register_route_successful(
        self, register_request: RegisterRequest
    ) -> None:
        user_dao = Mock(spec=UserDAO)
        # user_dao.return_value = register_request
        response = await register_route(register_request, user_dao)
        assert response.status == 200
        assert response.message == "Registration successful"
        assert isinstance(response.data, AuthResponse)


@pytest.mark.asyncio
class TestLoginRoute:
    async def test_login_route_successful(self, login_request: LoginRequest) -> None:
        user_dao = Mock(spec=UserDAO)

        response = await login_route(login_request, user_dao)
        assert response.status == 200
        assert response.message == "Login successful"
        assert isinstance(response.data, AuthResponse)
