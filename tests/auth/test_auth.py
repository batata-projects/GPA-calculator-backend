# implement test method for login_route and register_route

# Solution
from unittest.mock import Mock

import pytest
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue import User as GoTrueUser

from src.auth.auth import register
from src.auth.schemas import LoginRequest, RegisterRequest
from src.db.models.users import User


# test register route and login route
@pytest.mark.asyncio
class TestRegister:
    async def test_register_route_successful(
        self, register_request: RegisterRequest, user1: User
    ) -> None:
        user_dao = Mock()
        user_dao.get_user_by_email.return_value = None
        user_dao.client.auth.sign_up.return_value = GoTrueAuthResponse(
            user=GoTrueUser(
                id=user1.id,
                email=user1.email,
                user_metadata={
                    "username": user1.username,
                    "first_name": user1.first_name,
                    "last_name": user1.last_name,
                    "credits": user1.credits,
                    "counted_credits": user1.counted_credits,
                    "grade": user1.grade,
                },
                aud="authenticated",
                app_metadata={},
                created_at="2021-10-10T10:10:10.000Z",
            ),
            session=None,
        )

        response = register(register_request, user_dao)

        assert user_dao.get_user_by_email.called
        assert user_dao.client.auth.sign_up.called

        assert response.user == user1
        assert response.session is None

    async def test_register_route_no_firstname(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_no_lastname(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_no_email(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_email_in_use(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_password_too_short(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_password_no_uppercase(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_password_no_lowercase(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_password_no_number(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_password_no_special_character(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_email_rate_limit_exceeded(
        self, register_request: RegisterRequest
    ) -> None: ...

    async def test_register_route_failed(
        self, register_request: RegisterRequest
    ) -> None: ...


@pytest.mark.asyncio
class TestLoginRoute:
    async def test_login_route_successful(
        self, login_request: LoginRequest
    ) -> None: ...

    async def test_login_route_user_not_found(
        self, login_request: LoginRequest
    ) -> None: ...

    async def test_login_route_failed(self, login_request: LoginRequest) -> None: ...
