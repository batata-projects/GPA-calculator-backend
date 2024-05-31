from unittest.mock import Mock

import pytest

from src.db.models.available_courses import AvailableCourse


@pytest.fixture
def available_course(uuid4: Mock) -> AvailableCourse:
    return AvailableCourse(
        id=str(uuid4()),
        terms_id=str(uuid4()),
        name="EECE",
        code="230",
        credits=3,
        graded=True,
    )
