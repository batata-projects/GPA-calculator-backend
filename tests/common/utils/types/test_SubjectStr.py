from src.common.utils.types.SubjectStr import SubjectStr, validate_subject_str


class TestSubjectStr:
    def test_subject_str_successful(self, valid_subject: SubjectStr) -> None:
        assert validate_subject_str(valid_subject) == valid_subject
