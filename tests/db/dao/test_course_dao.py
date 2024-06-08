from unittest.mock import Mock

import pytest
from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao.course_dao import CourseDAO
from src.db.models.courses import Course
from src.db.tables import SupabaseTables


class TestCourseDAO:
    def test_get_course_by_id_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).select("*").eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.get_course_by_id(course1.id)

        assert result == course1

    def test_create_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).insert(
            course1.model_dump()
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.create_course(course1.model_dump())

        assert result == course1

    def test_update_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).update(course1.model_dump()).eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.update_course(course1.id, course1.model_dump())

        assert result == course1

    def test_delete_course_successful(self, course1: Course) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).delete().eq(
            "id", course1.id
        ).execute.return_value = APIResponse(data=[course1.model_dump()], count=None)

        assert course1.id is not None

        result = course_dao.delete_course(course1.id)

        assert result == course1

    @pytest.mark.parametrize(
        "method, method_arg, query_methods, query_return, attribute_name",
        [
            (
                "get_courses_by_user_id",
                ["courses_same_user_id[0].user_id"],
                ["select", "eq"],
                "courses_same_user_id",
                "user_id",
            ),
            (
                "get_courses_by_available_courses_id",
                ["courses_same_available_course_id[0].available_course_id"],
                ["select", "eq"],
                "courses_same_available_course_id",
                "available_course_id",
            ),
            (
                "get_courses_by_grade",
                ["courses_same_grade[0].grade", "users[0].id"],
                ["select", "eq", "eq"],
                "courses_same_grade",
                "grade",
            ),
        ],
    )
    def test_get_courses_by_attribute_successful(
        self,
        method: str,
        method_arg: list[str],
        query_methods: list[str],
        query_return: str,
        attribute_name: str,
        request: pytest.FixtureRequest,
    ) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_obj = mock_client.table(SupabaseTables.COURSES)

        for method_name in query_methods:
            mock_method = getattr(mock_obj, method_name)
            mock_obj = mock_method()

        mock_obj.execute.return_value = APIResponse(
            data=[
                course.model_dump() for course in request.getfixturevalue(query_return)
            ],
            count=None,
        )

        results = getattr(course_dao, method)(*method_arg)

        assert results == request.getfixturevalue(query_return)

        for result in results:
            assert getattr(result, attribute_name) is not None
            assert getattr(result, attribute_name) == getattr(
                results[0], attribute_name
            )

    def test_get_all_courses_successful(self, courses: list[Course]) -> None:
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).select("*").execute.return_value = (
            APIResponse(data=[course.model_dump() for course in courses], count=None)
        )

        results = course_dao.get_all_courses()

        assert results == courses

        for result in results:
            assert result.id is not None
            assert result.id == results[0].id
