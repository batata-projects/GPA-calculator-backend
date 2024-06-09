# test status in tests/controller/test_status.py:
from fastapi import status

from src.controller.status import router, status_check


def test_status_check():
    response = status_check()
    assert response.status == status.HTTP_200_OK
    assert response.message == "Status check successful"
    assert response.data is None