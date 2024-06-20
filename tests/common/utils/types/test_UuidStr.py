import pytest

from src.common.utils.types.UuidStr import UuidStr, validate_uuid_str


class TestUuidStr:
    def test_uuid_str_successful(self, valid_uuid: UuidStr) -> None:
        assert validate_uuid_str(valid_uuid) == valid_uuid

    def test_uuid_str_invalid(self, invalid_uuid: UuidStr) -> None:
        with pytest.raises(ValueError):
            validate_uuid_str(invalid_uuid)
