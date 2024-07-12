import pytest
from fastapi import status
from pydantic import BaseModel as PydanticBaseModel

from src.common.utils.data import ValidItems
from src.controller.routers._base_router import BaseRouter
from tests.fixtures.db.dao._base_dao import TestDAO
from tests.fixtures.db.models._base_model import TestObject


@pytest.mark.asyncio
class TestGetByQuery:
    async def test_get_by_query_successful(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        test_query: PydanticBaseModel,
        test_object1: TestObject,
    ) -> None:
        response = await router_successful.get_by_query(test_query, test_dao_successful)
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "tests found",
            "data": {"items": [test_object1.model_dump()]},
        }

    async def test_get_by_query_not_found(
        self,
        router_empty: BaseRouter[TestObject],
        test_dao_empty: TestDAO,
        test_query: PydanticBaseModel,
    ) -> None:
        response = await router_empty.get_by_query(query=test_query, dao=test_dao_empty)
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert res == {"message": "tests not found", "data": {}}

    async def test_get_by_query_error(
        self,
        router_error: BaseRouter[TestObject],
        test_dao_error: TestDAO,
        test_query: PydanticBaseModel,
    ) -> None:
        response = await router_error.get_by_query(query=test_query, dao=test_dao_error)
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert res == {"message": "error", "data": {}}


@pytest.mark.asyncio
class TestCreate:
    async def test_create_successful(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        test_object1: TestObject,
    ) -> None:
        response = await router_successful.create(
            request={"name": "test_name"}, dao=test_dao_successful
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_201_CREATED
        assert res == {
            "message": "test created",
            "data": {"items": [test_object1.model_dump()]},
        }

    async def test_create_not_created(
        self, router_empty: BaseRouter[TestObject], test_dao_empty: TestDAO
    ) -> None:
        response = await router_empty.create(
            request={"name": "test_name"}, dao=test_dao_empty
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert res == {"message": "test not created", "data": {}}

    async def test_create_error(
        self, router_error: BaseRouter[TestObject], test_dao_error: TestDAO
    ) -> None:
        response = await router_error.create(
            request={"name": "test_name"}, dao=test_dao_error
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert res == {"message": "error", "data": {}}


@pytest.mark.asyncio
class TestGetById:
    async def test_get_by_id_successful(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        test_object1: TestObject,
    ) -> None:
        response = await router_successful.get_by_id(
            id=ValidItems().uuidStr, dao=test_dao_successful
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "test found",
            "data": {"items": [test_object1.model_dump()]},
        }

    async def test_get_by_id_not_found(
        self, router_empty: BaseRouter[TestObject], test_dao_empty: TestDAO
    ) -> None:
        response = await router_empty.get_by_id(
            id=ValidItems().uuidStr, dao=test_dao_empty
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert res == {"message": "test not found", "data": {}}

    async def test_get_by_id_error(
        self, router_error: BaseRouter[TestObject], test_dao_error: TestDAO
    ) -> None:
        response = await router_error.get_by_id(
            id=ValidItems().uuidStr, dao=test_dao_error
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert res == {"message": "error", "data": {}}


@pytest.mark.asyncio
class TestUpdate:
    async def test_update_successful(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        test_object1: TestObject,
    ) -> None:
        response = await router_successful.update(
            id=ValidItems().uuidStr,
            request={"name": "test_name"},
            dao=test_dao_successful,
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "test updated",
            "data": {"items": [test_object1.model_dump()]},
        }

    async def test_update_not_updated(
        self, router_empty: BaseRouter[TestObject], test_dao_empty: TestDAO
    ) -> None:
        response = await router_empty.update(
            id=ValidItems().uuidStr, request={"name": "test_name"}, dao=test_dao_empty
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert res == {"message": "test not updated", "data": {}}

    async def test_update_error(
        self, router_error: BaseRouter[TestObject], test_dao_error: TestDAO
    ) -> None:
        response = await router_error.update(
            id=ValidItems().uuidStr, request={"name": "test_name"}, dao=test_dao_error
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert res == {"message": "error", "data": {}}


@pytest.mark.asyncio
class TestDelete:
    async def test_delete_successful(
        self,
        router_successful: BaseRouter[TestObject],
        test_dao_successful: TestDAO,
        test_object1: TestObject,
    ) -> None:
        response = await router_successful.delete(
            id=ValidItems().uuidStr, dao=test_dao_successful
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "test deleted",
            "data": {"items": [test_object1.model_dump()]},
        }

    async def test_delete_not_deleted(
        self, router_empty: BaseRouter[TestObject], test_dao_empty: TestDAO
    ) -> None:
        response = await router_empty.delete(
            id=ValidItems().uuidStr, dao=test_dao_empty
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert res == {"message": "test not deleted", "data": {}}

    async def test_delete_error(
        self, router_error: BaseRouter[TestObject], test_dao_error: TestDAO
    ) -> None:
        response = await router_error.delete(
            id=ValidItems().uuidStr, dao=test_dao_error
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert res == {"message": "error", "data": {}}
