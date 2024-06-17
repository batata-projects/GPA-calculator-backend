from unittest.mock import Mock

from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao import CourseDAO
from src.db.models import Course
from src.db.tables import SupabaseTables


class TestCourseDAO:
    def test_get_course_by_id_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).select("*").eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.get_by_id(course1.id)

        assert result == course1

    def test_create_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).insert(
            course1.model_dump()
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.create(course1.model_dump())

        assert result == course1

    def test_update_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).update(course1.model_dump()).eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.update(course1.id, course1.model_dump())

        assert result == course1

    def test_delete_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).delete().eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.delete(course1.id)

        assert result == course1

    def test_get_courses_by_query_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).select("*").eq(
            "available_course_id", course1.available_course_id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        result = course_dao.get_by_query(
            available_course_id=course1.available_course_id
        )

        assert result == [course1]
