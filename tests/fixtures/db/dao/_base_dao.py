from unittest.mock import Mock

import pytest
from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao import BaseDAO
from tests.fixtures.db.models._base_model import TestObject


class TestDAO(BaseDAO[TestObject]):
    def __init__(self, client: Client) -> None:
        super().__init__(client, "TESTS", TestObject)


@pytest.fixture
def test_dao_successful(test_object1: TestObject, client: Client = Mock()) -> TestDAO:
    # TODO: Allow nested calls in the mocking
    client = Mock()
    response = APIResponse(data=[test_object1.model_dump()], count=None)
    client.table("").select("").execute.return_value = response
    client.table("").select("").eq("", "").execute.return_value = response
    client.table("").select("").eq("", "").eq("", "").execute.return_value = response
    client.table("").insert("").execute.return_value = response
    client.table("").update("").eq("", "").execute.return_value = response
    client.table("").delete().eq("", "").execute.return_value = response
    return TestDAO(client)


@pytest.fixture
def test_dao_empty(client: Client = Mock()) -> TestDAO:
    client = Mock()
    response: APIResponse[None] = APIResponse(data=[], count=None)
    client.table("").select("").execute.return_value = response
    client.table("").select("").eq("", "").execute.return_value = response
    client.table("").select("").eq("", "").eq("", "").execute.return_value = response
    client.table("").insert("").execute.return_value = response
    client.table("").update("").eq("", "").execute.return_value = response
    client.table("").delete().eq("", "").execute.return_value = response
    return TestDAO(client)


@pytest.fixture
def test_dao_error(test_object1: TestObject, client: Client = Mock()) -> TestDAO:
    client = Mock()
    client.table("").select("").execute.return_value = Exception("error")
    client.table("").select("").eq("", "").execute.side_effect = Exception("error")
    client.table("").select("").eq("", "").eq("", "").execute.return_value = Exception(
        "error"
    )
    client.table("").insert("").execute.side_effect = Exception("error")
    client.table("").update("").eq("", "").execute.side_effect = Exception("error")
    client.table("").delete().eq("", "").execute.side_effect = Exception("error")
    return TestDAO(client)
