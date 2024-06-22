import pytest

from src.common.utils.types.TermInt import TermInt, validate_term_int


class TestTermInt:
    def test_term_int_successful(self, valid_term: TermInt) -> None:
        assert validate_term_int(valid_term) == valid_term

    def test_term_int_invalid(self, invalid_term: TermInt) -> None:
        with pytest.raises(ValueError):
            validate_term_int(invalid_term)
