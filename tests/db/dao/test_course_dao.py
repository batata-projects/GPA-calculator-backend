from unittest.mock import Mock

import pytest
from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao.course_dao import CourseDAO
from src.db.models.courses import Course
from src.db.tables import SupabaseTables


class TestCourseDAO:
    def test_get_course_by_id_successful(self, courses: list[Course]):
        course = courses[0]
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).select("*").eq(
            "id", course.id
        ).execute.return_value = APIResponse(data=[course.model_dump()], count=None)

        assert course.id is not None

        result = course_dao.get_course_by_id(course.id)

        assert result == course

    # TODO: reviwe the following test
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
                ["courses_same_available_courses_id[0].available_courses_id"],
                ["select", "eq"],
                "courses_same_available_courses_id",
                "available_courses_id",
            ),
            (
                "get_courses_by_grade",
                ["courses_same_grade[0].grade"],
                ["select", "eq"],
                "courses_same_grade",
                "grade",
            ),
        ],
    )
    def test_get_courses_by_attribute_successful(
        self,
        method,
        method_arg,
        query_methods,
        query_return,
        attribute_name,
        request: pytest.FixtureRequest,
    ):
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

    def test_get_all_courses_successful(self, courses: list[Course]):
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

    def test_create_course_successful(self, courses: list[Course]):
        course = courses[0]
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).insert(
            course.model_dump()
        ).execute.return_value = APIResponse(data=[course.model_dump()], count=None)

        result = course_dao.create_course(course.model_dump())

        assert result == course

    def test_update_course_successful(self, courses: list[Course]):
        course = courses[0]
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).update(course.model_dump()).eq(
            "id", course.id
        ).execute.return_value = APIResponse(data=[course.model_dump()], count=None)

        assert course.id is not None

        result = course_dao.update_course(course.id, course.model_dump())

        assert result == course

    def test_delete_course_successful(self, courses: list[Course]):
        course = courses[0]
        mock_client = Mock(spec=Client)
        course_dao = CourseDAO(mock_client)

        mock_client.table(SupabaseTables.COURSES).delete().eq(
            "id", course.id
        ).execute.return_value = APIResponse(data=[course.model_dump()], count=None)

        assert course.id is not None

        result = course_dao.delete_course(course.id)

        assert result == course
