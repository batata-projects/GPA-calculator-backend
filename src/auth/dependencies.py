from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError, decode

from src.config import Config


def decode_jwt(token: str) -> dict[str, str]:
    if Config.JWT.SECRET is None:
        raise ValueError("JWT_SECRET must be set in the environment")
    decoded_data: dict[str, str] = decode(
        token,
        key=Config.JWT.SECRET,
        algorithms=[Config.JWT.ALGORITHM],
        audience=Config.JWT.AUDIENCE,
    )
    return decoded_data


async def get_access_token(
    bearer: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    try:
        decode_jwt(bearer.credentials)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}"
        )
    return bearer.credentials


async def get_refresh_token(
    bearer: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    try:
        decode_jwt(bearer.credentials)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}"
        )
    return bearer.credentials
