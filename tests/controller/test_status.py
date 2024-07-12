import pytest
from fastapi import status

from src.controller.status import status_check


@pytest.mark.asyncio
async def test_status_check() -> None:
    response = await status_check()
    res = eval(response.body.decode("utf-8"))

    assert response.status_code == status.HTTP_200_OK
    assert res == {"message": "Status check successful", "data": {}}
