import pytest

from src.controller.routers._base_router import BaseRouter
from tests.fixtures.db.dao._base_dao import TestDAO
from tests.fixtures.db.models._base_model import TestObject


@pytest.fixture
def router_successful(test_dao_successful: TestDAO) -> BaseRouter[TestObject]:
    return BaseRouter[TestObject](
        prefix="/test",
        tags=["test"],
        name="test",
        model=TestObject,
        get_dao=lambda: test_dao_successful,
    )


@pytest.fixture
def router_empty(test_dao_empty: TestDAO) -> BaseRouter[TestObject]:
    return BaseRouter[TestObject](
        prefix="/test",
        tags=["test"],
        name="test",
        model=TestObject,
        get_dao=lambda: test_dao_empty,
    )


@pytest.fixture
def router_error(test_dao_error: TestDAO) -> BaseRouter[TestObject]:
    return BaseRouter[TestObject](
        prefix="/test",
        tags=["test"],
        name="test",
        model=TestObject,
        get_dao=lambda: test_dao_error,
    )
