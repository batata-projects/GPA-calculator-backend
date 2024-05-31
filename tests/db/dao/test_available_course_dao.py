from unittest.mock import MagicMock

from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.models.available_courses import AvailableCourse
from src.db.tables import SupabaseTables


class TestAvailableCourseDAO:
    def test_get_available_course_by_id_successful(
        self, available_course: AvailableCourse
    ):
        mock_client = MagicMock(spec=Client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).select("*").eq(
            "id", available_course.id
        ).execute.return_value = APIResponse(
            data=[available_course.model_dump()], count=None
        )

        assert available_course.id is not None

        available_course_dao = AvailableCourseDAO(mock_client)
        result = available_course_dao.get_available_course_by_id(available_course.id)

        assert result == available_course
