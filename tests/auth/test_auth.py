from unittest.mock import Mock

import pytest
from fastapi import HTTPException
from gotrue import AuthResponse as GoTrueAuthResponse  # type: ignore
from gotrue.types import Session as GoTrueSession  # type: ignore
from gotrue.types import User as GoTrueUser
from pydantic import EmailStr

from src.auth.auth import login, register
from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.session import Session
from src.common.utils.types import PasswordStr
from src.db.models import User


@pytest.mark.asyncio
class TestRegister:
    async def test_register_successful(
        self, register_request: RegisterRequest, user1: User, gotrue_user: GoTrueUser
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None
        user_dao.client.auth.sign_up.return_value = GoTrueAuthResponse(
            user=gotrue_user,
            session=None,
        )

        response = register(register_request, user_dao)

        assert user_dao.client.auth.sign_up.called

        assert response.user == user1
        assert response.session is None

    @pytest.mark.parametrize(
        "first_name, last_name, email",
        [
            ("", "Shaker", "user1.email"),
            ("Jad", "", "jad@mail.com"),
            ("Jad", "Shaker", ""),
            ("Jad", "Shaker", "jad@mail.com"),
        ],
    )
    async def test_register_no_attribute(
        self,
        register_request: RegisterRequest,
        user1: User,
        first_name: str,
        last_name: str,
        email: EmailStr,
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None
        user_dao.client.auth.sign_up.return_value = GoTrueAuthResponse(
            user=GoTrueUser(
                id=user1.id,
                email=email,
                user_metadata={
                    "first_name": first_name,
                    "last_name": last_name,
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

        with pytest.raises(Exception) as exc:
            register(register_request, user_dao)
            assert "First name and last name are required" in str(
                exc.value
            ) or "Email is required" in str(exc.value)

    async def test_register_email_in_use(
        self, register_request: RegisterRequest, user1: User
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = user1

        with pytest.raises(Exception) as exc:
            register(register_request, user_dao)
            assert "Email already in use" in str(exc.value)

    async def test_register_failed(
        self, register_request: RegisterRequest, user1: User
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None
        user_dao.client.auth.sign_up.side_effect = Exception()

        with pytest.raises(Exception) as exc:
            register(register_request, user_dao)
            assert "Registration failed, please check your credentials" in str(
                exc.value
            )

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
    async def test_register_password_too_short(
        self, register_request: RegisterRequest, password: PasswordStr
    ) -> None:
        user_dao = Mock()
        user_dao.client.auth.sign_up.side_effect = Exception()
        register_request.password = password
        with pytest.raises(Exception) as exc:
            register(register_request, user_dao)
            assert exc.type == HTTPException

    async def test_register_email_rate_limit_exceeded(
        self, register_request: RegisterRequest
    ) -> None:
        user_dao = Mock()
        user_dao.client.auth.sign_up.side_effect = Exception(
            "Email rate limit exceeded"
        )

        with pytest.raises(Exception) as exc:
            register(register_request, user_dao)
            assert "Email rate limit exceeded, please try again later" in str(exc.value)


@pytest.mark.asyncio
class TestLogin:
    async def test_login_successful(
        self,
        login_request: LoginRequest,
        user1: User,
        session: Session,
        gotrue_user: GoTrueUser,
        gotrue_session: GoTrueSession,
    ) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = user1
        user_dao.client.auth.sign_in_with_password.return_value = GoTrueAuthResponse(
            user=gotrue_user, session=gotrue_session
        )

        response = login(login_request, user_dao)

        assert user_dao.get_by_query.called
        assert user_dao.client.auth.sign_in_with_password.called

        assert response.user == user1
        assert response.session == session

    async def test_login_user_not_found(self, login_request: LoginRequest) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None

        with pytest.raises(Exception) as exc:
            login(login_request, user_dao)
            assert "User not found" in str(exc.value)

    async def test_login_failed(self, login_request: LoginRequest) -> None:
        user_dao = Mock()
        user_dao.get_by_query.return_value = None
        user_dao.client.auth.sign_in_with_password.side_effect = Exception()

        with pytest.raises(Exception) as exc:
            login(login_request, user_dao)
            assert "Login failed, please check your credentials" in str(exc.value)
