from supabase import Client

from src.db.models.courses import Course
from src.db.models.utils import UuidStr
from src.db.tables import SupabaseTables


class CourseDAO:
    def __init__(self, client: Client):
        self.client = client

    def get_course_by_id(self, course_id: UuidStr):
        data = (
            (self.client.table(SupabaseTables.COURSES))
            .select("*")
            .eq("id", course_id)
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def get_courses_by_user_id(self, user_id: UuidStr) -> list[Course]:
        data = (
            (self.client.table(SupabaseTables.COURSES))
            .select("*")
            .eq("user_id", user_id)
            .execute()
        )
        if not data.data:
            return []
        return [Course.model_validate(course) for course in data.data]

    def get_courses_by_all_courses_id(self, all_courses_id: UuidStr) -> list[Course]:
        data = (
            (self.client.table(SupabaseTables.COURSES))
            .select("*")
            .eq("all_courses_id", all_courses_id)
            .execute()
        )
        if not data.data:
            return []
        return [Course.model_validate(course) for course in data.data]

    def create_course(self, course: Course):
        data = (
            (self.client.table(SupabaseTables.COURSES))
            .insert(course.model_dump())
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def update_course(self, course_id: UuidStr, course_data: dict):
        self.client.table(SupabaseTables.COURSES).update(course_data).eq(
            "id", course_id
        ).execute()

    def delete_course(self, course_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.COURSES)
            .delete()
            .eq("id", course_id)
            .execute()
        )
        if not data.data:
            return None
        return Course.model_validate(data.data[0])

    def get_all_courses(self) -> list[Course]:
        data = self.client.table(SupabaseTables.COURSES).select("*").execute()
        if not data.data:
            return []
        return [Course.model_validate(course) for course in data.data]
