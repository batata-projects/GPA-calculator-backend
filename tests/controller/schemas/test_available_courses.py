from src.controller.schemas.available_courses import AvailableCourseQuery


def test_available_course_query() -> None:
    query = AvailableCourseQuery()
    assert query is not None
    assert query.model_dump() == {
        "term_id": None,
        "name": None,
        "code": None,
        "credits": None,
        "graded": None,
    }
