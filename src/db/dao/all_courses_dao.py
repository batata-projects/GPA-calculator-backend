from supabase import Client

from src.db.models.all_courses import AvailableCourse
from src.db.models.utils import CourseCodeStr, CourseNameStr, TermStr, UuidStr
from src.db.tables import SupabaseTables


class AvailableCourseDAO:
    def __init__(self, client: Client):
        self.client = client

    def get_available_course_by_id(self, available_courses_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("id", available_courses_id)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def get_available_courses_by_course_name(
        self, course_name: CourseNameStr
    ) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("course_name", course_name)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]

    def get_available_courses_by_course_code(
        self, course_code: CourseCodeStr
    ) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("course_code", course_code)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]

    def get_available_courses_by_credit(self, credit: int) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("credit", credit)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]

    def get_available_courses_by_term_name(
        self, term_name: TermStr
    ) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("term_name", term_name)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]

    def get_available_courses_by_graded(self, graded: bool) -> list[AvailableCourse]:
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("graded", graded)
            .execute()
        )
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]

    def create_available_course(self, available_course: AvailableCourse):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .insert(available_course.model_dump())
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def update_available_courses(
        self, available_courses_id: str, available_courses_data: dict
    ):
        self.client.table(SupabaseTables.ALL_COURSES).update(available_courses_data).eq(
            "id", available_courses_id
        ).execute()

    def delete_available_courses(self, available_courses_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .delete()
            .eq("id", available_courses_id)
            .execute()
        )
        if not data.data:
            return None
        return AvailableCourse.model_validate(data.data[0])

    def get_all_available_courses(self) -> list[AvailableCourse]:
        data = self.client.table(SupabaseTables.ALL_COURSES).select("*").execute()
        if not data.data:
            return []
        return [
            AvailableCourse.model_validate(available_courses)
            for available_courses in data.data
        ]
