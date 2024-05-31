from unittest.mock import MagicMock

import pytest
from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.models.available_courses import AvailableCourse
from src.db.tables import SupabaseTables


class TestAvailableCourseDAO:
    def test_get_available_course_successful(
        self, available_courses: list[AvailableCourse]
    ):
        available_course = available_courses[0]
        mock_client = MagicMock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_client.table(SupabaseTables.AVAILABLE_COURSES).select("*").eq(
            "id", available_course.id
        ).execute.return_value = APIResponse(
            data=[available_course.model_dump()], count=None
        )

        assert available_course.id is not None

        result = available_course_dao.get_available_course_by_id(available_course.id)

        assert result == available_course

    @pytest.mark.parametrize(
        "method, method_arg, query_methods, query_return, attribute_name",
        [
            (
                "get_available_courses_by_course_name",
                ["available_courses_same_course_name[0].name"],
                ["select", "eq"],
                "available_courses_same_course_name",
                "name",
            ),
            (
                "get_available_courses_by_credit",
                ["available_courses_same_credits[0].credits"],
                ["select", "eq"],
                "available_courses_same_credits",
                "credits",
            ),
            (
                "get_available_courses_by_graded",
                ["available_courses_same_graded[0].graded"],
                ["select", "eq"],
                "available_courses_same_graded",
                "graded",
            ),
            (
                "get_available_courses_by_terms_id",
                ["available_courses_same_terms[0].terms_id"],
                ["select", "eq"],
                "available_courses_same_terms",
                "terms_id",
            ),
        ],
    )
    def test_get_available_courses_successful(
        self,
        method,
        method_arg,
        query_methods,
        query_return,
        attribute_name,
        request: pytest.FixtureRequest,
    ):
        mock_client = MagicMock(spec=Client)
        available_course_dao = AvailableCourseDAO(mock_client)

        mock_obj = mock_client.table(SupabaseTables.AVAILABLE_COURSES)

        for method_name in query_methods:
            mock_method = getattr(mock_obj, method_name)
            mock_obj = mock_method()

        mock_obj.execute.return_value = APIResponse(
            data=[
                available_course.model_dump()
                for available_course in request.getfixturevalue(query_return)
            ],
            count=None,
        )

        results = getattr(available_course_dao, method)(*method_arg)

        assert results == request.getfixturevalue(query_return)

        for result in results:
            assert getattr(result, attribute_name) is not None
            assert getattr(result, attribute_name) == getattr(
                results[0], attribute_name
            )
