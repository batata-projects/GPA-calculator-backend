# test status in tests/controller/test_status.py:
import pytest
from fastapi import status

from src.controller.status import status_check


@pytest.mark.asyncio
async def test_status_check() -> None:
    response = await status_check()
    assert response.status == status.HTTP_200_OK
    assert response.message == "Status check successful"
    assert response.data == None
