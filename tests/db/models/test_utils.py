import pytest

import src.db.models.utils as utils


class TestUtils:
    def test_validate_uuid_successful(self, valid_uuid):
        assert utils.validate_uuid(valid_uuid) == valid_uuid

    def test_validate_uuid_invalid(self, invalid_uuid):
        with pytest.raises(ValueError):
            utils.validate_uuid(invalid_uuid)

    def test_validate_email_str_successful(self, valid_email):
        assert utils.validate_email_str(valid_email) == valid_email

    def test_validate_email_str_invalid(self, invalid_email):
        with pytest.raises(ValueError):
            utils.validate_email_str(invalid_email)

    def test_validate_term_str_successful(self, valid_term):
        assert utils.validate_term_str(valid_term) == valid_term

    def test_validate_term_str_invalid(self, invalid_term):
        with pytest.raises(ValueError):
            utils.validate_term_str(invalid_term)

    def test_validate_course_name_successful(self, valid_course_name):
        assert utils.validate_course_name(valid_course_name) == valid_course_name

    def test_validate_course_name_invalid(self, invalid_course_name):
        with pytest.raises(ValueError):
            utils.validate_course_name(invalid_course_name)

    def test_validate_course_code_successful(self, valid_course_code):
        assert utils.validate_course_code(valid_course_code) == valid_course_code

    def test_validate_course_code_invalid(self, invalid_course_code):
        with pytest.raises(ValueError):
            utils.validate_course_code(invalid_course_code)
