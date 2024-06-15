from typing import Optional

from fastapi import APIRouter, Depends, Path, Query, status
from pydantic import EmailStr, PositiveFloat, PositiveInt

from src.common.responses import APIResponse
from src.common.utils.types.UsernameStr import UsernameStr
from src.common.utils.types.UuidStr import UuidStr
from src.controller.users.schemas import UserRequest, UserResponse
from src.db.dao.user_dao import UserDAO
from src.db.dependencies import get_user_dao

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/",
    response_model=APIResponse[UserResponse],
    response_description="Get users by query",
)
async def get_users_by_query(
    user_id: Optional[UuidStr] = Query(None, description="User ID"),
    username: Optional[UsernameStr] = Query(None, description="User username"),
    email: Optional[EmailStr] = Query(None, description="User email"),
    first_name: Optional[str] = Query(None, description="User first name"),
    last_name: Optional[str] = Query(None, description="User last name"),
    credits: Optional[PositiveInt] = Query(None, description="User credits"),
    counted_credits: Optional[PositiveInt] = Query(
        None, description="User counted credits"
    ),
    grade: Optional[PositiveFloat] = Query(None, description="User grade"),
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse[UserResponse]:
    try:
        users = user_dao.get_users_by_query(
            user_id, username, email, first_name, last_name, credits, grade
        )
        if users:
            return APIResponse[UserResponse](
                status=status.HTTP_200_OK,
                message="Users found",
                data=UserResponse(users=users),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Users not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.post(
    "/",
    response_model=APIResponse[UserResponse],
    response_description="Create a new user",
)
async def create_user(
    request: UserRequest,
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse[UserResponse]:
    try:
        user = user_dao.create_user(request.model_dump())
        if user:
            return APIResponse[UserResponse](
                status=status.HTTP_201_CREATED,
                message="User created",
                data=UserResponse(users=[user]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="User not created",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/{user_id}",
    response_model=APIResponse[UserResponse],
    response_description="Get user by ID",
)
async def get_user_by_id(
    user_id: UuidStr = Path(..., description="User ID"),
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse[UserResponse]:
    try:
        user = user_dao.get_user_by_id(user_id)
        if user:
            return APIResponse[UserResponse](
                status=status.HTTP_200_OK,
                message="User found",
                data=UserResponse(users=[user]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="User not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.put(
    "/{user_id}",
    response_model=APIResponse[UserResponse],
    response_description="Update a user",
)
async def update_user(
    user_id: UuidStr = Path(..., description="User ID"),
    username: Optional[UsernameStr] = Query(None, description="User username"),
    email: Optional[EmailStr] = Query(None, description="User email"),
    first_name: Optional[str] = Query(None, description="User first name"),
    last_name: Optional[str] = Query(None, description="User last name"),
    credits: Optional[PositiveInt] = Query(None, description="User credits"),
    counted_credits: Optional[PositiveInt] = Query(
        None, description="User counted credits"
    ),
    grade: Optional[PositiveFloat] = Query(None, description="User grade"),
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse[UserResponse]:
    try:
        user_data = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "credits": credits,
            "counted_credits": counted_credits,
            "grade": grade,
        }

        user_data = {k: v for k, v in user_data.items() if v is not None}

        user = user_dao.update_user(user_id, user_data)
        if user:
            return APIResponse[UserResponse](
                status=status.HTTP_200_OK,
                message="User updated",
                data=UserResponse(users=[user]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="User not updated",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.delete(
    "/{user_id}",
    response_model=APIResponse[UserResponse],
    response_description="Delete a user",
)
async def delete_user(
    user_id: UuidStr = Path(..., description="User ID"),
    user_dao: UserDAO = Depends(get_user_dao),
) -> APIResponse[UserResponse]:
    try:
        user = user_dao.delete_user(user_id)
        if user:
            return APIResponse[UserResponse](
                status=status.HTTP_200_OK,
                message="User deleted",
                data=UserResponse(users=[user]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="User not deleted",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )
