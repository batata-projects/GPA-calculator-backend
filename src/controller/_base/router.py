from enum import Enum
from typing import Any, Callable, Generic, Optional, Type, TypeVar, Union

from fastapi import Depends, status
from fastapi.routing import APIRouter

from src.common.responses import APIResponse
from src.common.utils.types import UuidStr
from src.controller._base import BaseQuery, BaseResponse
from src.db.dao import BaseDAO
from src.db.models import BaseModel

BaseModelType = TypeVar("BaseModelType", bound=BaseModel)
ResponseType = TypeVar("ResponseType", bound=BaseResponse[BaseModel])


class BaseRouter(Generic[BaseModelType]):
    def __init__(
        self,
        prefix: str,
        tags: Optional[list[Union[str, Enum]]],
        name: str,
        model: Type[BaseModelType],
        get_dao: Callable[[], BaseDAO[BaseModelType]],
    ):
        self.prefix = prefix
        self.tags = tags
        self.name = name
        self.request = {
            field: field for field in model.model_fields.keys() if field != "id"
        }
        self.get_dao = get_dao

    async def get_by_query(
        self, query: BaseQuery[BaseModelType], dao: BaseDAO[BaseModelType]
    ) -> APIResponse[BaseResponse[BaseModelType]]:
        try:
            items = dao.get_by_query(*query)
            if items:
                return APIResponse(
                    status=status.HTTP_200_OK,
                    message=f"{self.name}s found",
                    data=BaseResponse[BaseModelType](items=items),
                )
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{self.name}s not found",
            )
        except Exception as e:
            return APIResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=str(e),
            )

    async def create(
        self,
        request: dict[str, Any],
        dao: BaseDAO[BaseModelType],
    ) -> APIResponse[BaseResponse[BaseModelType]]:
        try:
            item = dao.create(request)
            if item:
                return APIResponse(
                    status=status.HTTP_201_CREATED,
                    message=f"{self.name} created",
                    data=BaseResponse[BaseModelType](items=[item]),
                )
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{self.name} not created",
            )
        except Exception as e:
            return APIResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=str(e),
            )

    async def get_by_id(
        self, id: UuidStr, dao: BaseDAO[BaseModelType]
    ) -> APIResponse[BaseResponse[BaseModelType]]:
        try:
            item = dao.get_by_id(id)
            if item:
                return APIResponse(
                    status=status.HTTP_200_OK,
                    message=f"{self.name} found",
                    data=BaseResponse[BaseModelType](items=[item]),
                )
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{self.name} not found",
            )
        except Exception as e:
            return APIResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=str(e),
            )

    async def update(
        self,
        id: UuidStr,
        request: dict[str, Any],
        dao: BaseDAO[BaseModelType],
    ) -> APIResponse[BaseResponse[BaseModelType]]:
        try:
            item = dao.update(id, request)
            if item:
                return APIResponse(
                    status=status.HTTP_200_OK,
                    message=f"{self.name} updated",
                    data=BaseResponse[BaseModelType](items=[item]),
                )
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{self.name} not updated",
            )
        except Exception as e:
            return APIResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=str(e),
            )

    async def delete(
        self, id: UuidStr, dao: BaseDAO[BaseModelType]
    ) -> APIResponse[BaseResponse[BaseModelType]]:
        try:
            item = dao.delete(id)
            if item:
                return APIResponse(
                    status=status.HTTP_200_OK,
                    message=f"{self.name} deleted",
                    data=BaseResponse[BaseModelType](items=[item]),
                )
            return APIResponse(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{self.name} not deleted",
            )
        except Exception as e:
            return APIResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=str(e),
            )

    def build_router(self) -> APIRouter:
        router = APIRouter(
            prefix=self.prefix,
            tags=self.tags,
        )

        @router.get("/")
        async def get_by_query(
            query: BaseQuery[BaseModelType] = Depends(),
            dao: BaseDAO[BaseModelType] = Depends(self.get_dao),
        ) -> APIResponse[BaseResponse[BaseModelType]]:
            return await self.get_by_query(query, dao)

        @router.post("/")
        async def create(
            request: dict[str, Any] = self.request,
            dao: BaseDAO[BaseModelType] = Depends(self.get_dao),
        ) -> APIResponse[BaseResponse[BaseModelType]]:
            return await self.create(request, dao)

        @router.get("/{id}")
        async def get_by_id(
            id: UuidStr,
            dao: BaseDAO[BaseModelType] = Depends(self.get_dao),
        ) -> APIResponse[BaseResponse[BaseModelType]]:
            return await self.get_by_id(id, dao)

        @router.put("/{id}")
        async def update(
            id: UuidStr,
            request: dict[str, Any] = self.request,
            dao: BaseDAO[BaseModelType] = Depends(self.get_dao),
        ) -> APIResponse[BaseResponse[BaseModelType]]:
            return await self.update(id, request, dao)

        @router.delete("/{id}")
        async def delete(
            id: UuidStr,
            dao: BaseDAO[BaseModelType] = Depends(self.get_dao),
        ) -> APIResponse[BaseResponse[BaseModelType]]:
            return await self.delete(id, dao)

        return router
