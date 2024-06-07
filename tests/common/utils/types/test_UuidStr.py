import pytest

from src.common.utils.types.UuidStr import UuidStr, validate_uuid


class TestUuidStr:
    def test_uuid_str_successful(self, valid_uuid: UuidStr):
        assert validate_uuid(valid_uuid) == valid_uuid

    def test_uuid_str_invalid(self, invalid_uuid: UuidStr):
        with pytest.raises(ValueError):
            validate_uuid(invalid_uuid)
