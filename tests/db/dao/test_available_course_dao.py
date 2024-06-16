from unittest.mock import Mock

from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao import AvailableCourseDAO
from src.db.models import AvailableCourse
from src.db.tables import SupabaseTables


class TestAvailableCourseDAO:
    def test_get_available_course_by_id_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        mock_client = Mock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).select("*").eq(
            "id", available_course1.id
        ).execute.return_value = APIResponse(
            data=[available_course1.model_dump()], count=None
        )

        assert available_course1.id is not None

        result = available_course_dao.get_available_course_by_id(available_course1.id)

        assert result == available_course1

    def test_create_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        mock_client = Mock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).insert(
            available_course1.model_dump()
        ).execute.return_value = APIResponse(
            data=[available_course1.model_dump()], count=None
        )

        result = available_course_dao.create_available_course(
            available_course1.model_dump()
        )

        assert result == available_course1

    def test_update_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        mock_client = Mock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).update(
            available_course1.model_dump()
        ).eq("id", available_course1.id).execute.return_value = APIResponse(
            data=[available_course1.model_dump()], count=None
        )

        assert available_course1.id is not None

        result = available_course_dao.update_available_course(
            available_course1.id, available_course1.model_dump()
        )

        assert result == available_course1

    def test_delete_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        mock_client = Mock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).delete().eq(
            "id", available_course1.id
        ).execute.return_value = APIResponse(
            data=[available_course1.model_dump()], count=None
        )

        assert available_course1.id is not None

        result = available_course_dao.delete_available_course(available_course1.id)

        assert result == available_course1

    def test_get_available_courses_by_query_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        mock_client = Mock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).select("*").eq(
            "name", available_course1.name
        ).execute.return_value = APIResponse(
            data=[available_course1.model_dump()], count=None
        )

        result = available_course_dao.get_available_courses_by_query(
            name=available_course1.name
        )

        assert result == [available_course1]
