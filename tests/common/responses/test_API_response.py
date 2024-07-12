import pytest
from fastapi import status

from src.common.responses import APIResponse


class TestAPIResponse:
    def test_api_response_successful(self) -> None:
        response = APIResponse(
            status_code=status.HTTP_200_OK, message="OK", data={"key": "value"}
        )
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "OK",
            "data": {"key": "value"},
        }

    def test_api_response_no_data(self) -> None:
        response = APIResponse(status_code=status.HTTP_200_OK, message="OK")
        res = eval(response.body.decode("utf-8"))

        assert response.status_code == status.HTTP_200_OK
        assert res == {"message": "OK", "data": {}}

    @pytest.mark.parametrize(
        "status_code, message, data",
        [
            (None, "OK", {"key": "value"}),
            (200, None, {"key": "value"}),
        ],
    )
    def test_api_response_invalid(
        self, status_code: int, message: str, data: dict[str, str]
    ) -> None:
        with pytest.raises(ValueError):
            APIResponse(status_code=status_code, message=message, data=data)
