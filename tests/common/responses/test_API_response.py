import pytest

from src.common.responses import APIResponse


class TestAPIResponse:
    def test_api_response_successful(self) -> None:
        response = APIResponse[int](status=200, message="OK", data=1)
        assert response.status == 200
        assert response.message == "OK"
        assert response.data == 1
        assert response.model_dump() == {"status": 200, "message": "OK", "data": 1}

    def test_api_response_no_data(self) -> None:
        response = APIResponse[int](status=200, message="OK")
        assert response.status == 200
        assert response.message == "OK"
        assert response.data is None
        assert response.model_dump() == {"status": 200, "message": "OK", "data": None}

    @pytest.mark.parametrize(
        "status, message, data",
        [
            (None, "OK", 1),
            (200, None, 1),
        ],
    )
    def test_api_response_invalid(
        self,
        status: int,
        message: str,
        data: int,
    ) -> None:
        with pytest.raises(ValueError):
            APIResponse[int](status=status, message=message, data=data)
