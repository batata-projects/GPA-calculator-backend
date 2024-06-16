from typing import Optional, Union

from pydantic import NonNegativeFloat
from supabase import Client

from src.common.utils.types import CourseGradeFloat, UuidStr
from src.db.models import Course
from src.db.tables import SupabaseTables


class CourseDAO:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get_course_by_id(self, course_id: UuidStr) -> Optional[Course]:
        data = (
            (self.client.table(SupabaseTables.COURSES))
            .select("*")
            .eq("id", course_id)
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def create_course(
        self, course_data: dict[str, Union[UuidStr, NonNegativeFloat, bool, None]]
    ) -> Optional[Course]:
        Course.model_validate(course_data)
        data = (self.client.table(SupabaseTables.COURSES)).insert(course_data).execute()
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def update_course(
        self,
        course_id: UuidStr,
        course_data: dict[str, Union[UuidStr, NonNegativeFloat, bool, None]],
    ) -> Optional[Course]:
        Course.model_validate_partial(course_data)
        data = (
            self.client.table(SupabaseTables.COURSES)
            .update(course_data)
            .eq("id", course_id)
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def delete_course(self, course_id: UuidStr) -> Optional[Course]:
        data = (
            self.client.table(SupabaseTables.COURSES)
            .delete()
            .eq("id", course_id)
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def get_courses_by_query(
        self,
        available_course_id: Optional[UuidStr] = None,
        user_id: Optional[UuidStr] = None,
        grade: Optional[CourseGradeFloat] = None,
        passed: Optional[bool] = None,
    ) -> list[Course]:
        queries = self.client.table(SupabaseTables.COURSES).select("*")
        if available_course_id:
            queries = queries.eq("available_course_id", available_course_id)
        if user_id:
            queries = queries.eq("user_id", user_id)
        if grade:
            queries = queries.eq("grade", grade)
        if passed:
            queries = queries.eq("passed", passed)
        data = queries.execute()
        if not data.data:
            return []
        return [Course.model_validate(course) for course in data.data]
