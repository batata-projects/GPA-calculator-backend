import pytest


@pytest.fixture
def valid_uuid():
    return "6f6c6d2b-4e4b-4c4f-8c8e-6c6d4e4b3a3b"


@pytest.fixture
def invalid_uuid():
    return "invalid-uuid"


@pytest.fixture
def valid_email():
    return "rmf04@mail.aub.edu"


@pytest.fixture
def invalid_email():
    return "invalid-email"


@pytest.fixture
def valid_term():
    return "Fall 2021 - 2022"


@pytest.fixture
def invalid_term():
    return "invalid-term"


@pytest.fixture
def valid_course_name():
    return "COMP"


@pytest.fixture
def invalid_course_name():
    return "invalid-course-name"


@pytest.fixture
def valid_course_code():
    return "202"


@pytest.fixture
def invalid_course_code():
    return "invalid-course-code"
