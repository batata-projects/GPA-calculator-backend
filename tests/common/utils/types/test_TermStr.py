import pytest

from src.common.utils.types.TermStr import TermStr, validate_term_str


class TestTermStr:
    def test_term_str_successful(self, valid_term: TermStr):
        assert validate_term_str(valid_term) == valid_term

    def test_term_str_invalid(self, invalid_term: TermStr):
        with pytest.raises(ValueError):
            validate_term_str(invalid_term)
