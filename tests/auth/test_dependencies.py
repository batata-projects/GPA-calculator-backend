import time
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from jwt import ExpiredSignatureError, InvalidSignatureError

from src.auth.dependencies import decode_jwt, get_access_token, get_refresh_token


@patch("src.auth.dependencies.Config")
class TestDecodeJwt:
    def test_decode_jwt(
        self, mock_config: Mock, valid_jwt: str, valid_signature: str
    ) -> None:
        mock_config.JWT.SECRET = valid_signature
        mock_config.JWT.ALGORITHM = "HS256"
        mock_config.JWT.AUDIENCE = "authenticated"
        decoded_data = decode_jwt(valid_jwt)
        assert decoded_data["aud"] == "authenticated"
        assert int(decoded_data["exp"]) > int(time.time())
        assert int(decoded_data["iat"]) <= int(time.time())

    def test_decode_jwt_invalid(
        self, mock_config: Mock, invalid_signature: str, invalid_jwt: str
    ) -> None:
        mock_config.JWT.SECRET = invalid_signature
        mock_config.JWT.ALGORITHM = "HS256"
        mock_config.JWT.AUDIENCE = "authenticated"
        with pytest.raises(InvalidSignatureError):
            decode_jwt(invalid_jwt)

    def test_decode_jwt_expired(
        self, mock_config: Mock, valid_signature: str, invalid_jwt: str
    ) -> None:
        mock_config.JWT.SECRET = valid_signature
        mock_config.JWT.ALGORITHM = "HS256"
        mock_config.JWT.AUDIENCE = "authenticated"
        with pytest.raises(ExpiredSignatureError):
            decode_jwt(invalid_jwt)


class TestGetAccessToken:
    @pytest.mark.asyncio
    @patch("src.auth.dependencies.decode_jwt")
    async def test_get_access_token(
        self, mock_decode_jwt: Mock, valid_jwt: str
    ) -> None:
        mock_decode_jwt.return_value = {
            "aud": "authenticated",
            "exp": 1718519256,
            "iat": 1718515656,
        }
        bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=valid_jwt)
        token = await get_access_token(bearer)
        assert token == valid_jwt

    @pytest.mark.asyncio
    @patch("src.auth.dependencies.decode_jwt")
    async def test_get_access_token_invalid(
        self, mock_decode_jwt: Mock, invalid_jwt: str
    ) -> None:
        bearer = HTTPAuthorizationCredentials(scheme="Bearer", credentials=invalid_jwt)
        mock_decode_jwt.side_effect = InvalidSignatureError
        with pytest.raises(HTTPException) as e:
            await get_access_token(bearer)
        assert e.value.status_code == 401


class TestGetRefreshToken:
    @pytest.mark.asyncio
    async def test_get_refresh_token(self, valid_refresh_token: str) -> None:
        token = await get_refresh_token(valid_refresh_token)
        assert token == valid_refresh_token
