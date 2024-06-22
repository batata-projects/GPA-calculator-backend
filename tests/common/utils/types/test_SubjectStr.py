import pytest

from src.common.utils.types.SubjectStr import SubjectStr, validate_subject_str


class TestSubjectStr:
    def test_subject_str_successful(self, valid_subject: SubjectStr) -> None:
        assert validate_subject_str(valid_subject) == valid_subject

    def test_subject_str_invalid(self, invalid_subject: SubjectStr) -> None:
        with pytest.raises(ValueError):
            validate_subject_str(invalid_subject)
