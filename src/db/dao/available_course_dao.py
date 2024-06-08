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

    def get_available_courses_by_course_name(
        self, course_name: CourseNameStr
    ) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .select("*")
            .eq("name", course_name)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]

    def get_available_courses_by_credit(self, credit: int) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .select("*")
            .eq("credits", credit)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]

    def get_available_courses_by_term_id(
        self, term_id: UuidStr
    ) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .select("*")
            .eq("term_id", term_id)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]

    def get_available_courses_by_graded(self, graded: bool) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.AVAILABLE_COURSES)
            .select("*")
            .eq("graded", graded)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]

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

    def get_all_available_courses(self) -> list[AvailableCourse]:
        data = self.client.table(SupabaseTables.AVAILABLE_COURSES).select("*").execute()
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_course)
            for available_course in data.data
        ]
