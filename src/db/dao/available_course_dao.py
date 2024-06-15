from typing import Optional, Union

from pydantic import NonNegativeInt
from supabase import Client

from src.common.utils.types.CourseCodeStr import CourseCodeStr
from src.common.utils.types.CourseNameStr import CourseNameStr
from src.common.utils.types.UuidStr import UuidStr
from src.db.models.available_courses import AvailableCourse
from src.db.tables import SupabaseTables


class AvailableCourseDAO:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get_available_course_by_id(
        self, available_course_id: UuidStr
    ) -> Optional[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .select("*")
            .eq("id", available_course_id)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def create_available_course(
        self,
        available_course_data: dict[
            str, Union[UuidStr, CourseNameStr, CourseCodeStr, NonNegativeInt, bool]
        ],
    ) -> Optional[AvailableCourse]:
        AvailableCourse.model_validate(available_course_data)
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .insert(available_course_data)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def update_available_course(
        self,
        available_course_id: str,
        available_course_data: dict[
            str,
            Union[UuidStr, CourseNameStr, CourseCodeStr, NonNegativeInt, bool, None],
        ],
    ) -> Optional[AvailableCourse]:
        AvailableCourse.model_validate_partial(available_course_data)
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .update(available_course_data)
            .eq("id", available_course_id)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def delete_available_course(
        self, available_course_id: UuidStr
    ) -> Optional[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .delete()
            .eq("id", available_course_id)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def get_available_courses_by_query(
        self,
        term_id: Optional[UuidStr],
        course_name: Optional[CourseNameStr],
        course_code: Optional[CourseCodeStr],
        credit: Optional[NonNegativeInt],
        graded: Optional[bool],
    ) -> list[AvailableCourse]:
        queries = self.client.table(SupabaseTables.AVAILABLE_COURSES).select("*")
        if term_id:
            queries = queries.eq("term_id", term_id)
        if course_name:
            queries = queries.eq("name", course_name)
        if course_code:
            queries = queries.eq("code", course_code)
        if credit:
            queries = queries.eq("credits", credit)
        if graded:
            queries = queries.eq("graded", graded)
        data = queries.execute()
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]
