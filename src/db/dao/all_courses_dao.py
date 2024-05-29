from supabase import Client

from src.db.models.all_courses import AllCourses
from src.db.models.utils import CourseCodeStr, CourseNameStr, TermStr, UuidStr
from src.db.tables import SupabaseTables


class AllCoursesDAO:
    def __init__(self, client: Client):
        self.client = client

    def get_all_courses_by_id(self, all_courses_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("id", all_courses_id)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def get_all_courses_by_course_name(self, course_name: CourseNameStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("course_name", course_name)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def get_all_courses_by_course_code(self, course_code: CourseCodeStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("course_code", course_code)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def get_all_courses_by_credit(self, credit: int):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("credit", credit)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def get_all_courses_by_term_name(self, term_name: TermStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .select("*")
            .eq("term_name", term_name)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def create_all_courses(self, all_courses: AllCourses):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .insert(all_courses.model_dump())
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def update_all_courses(self, all_courses_id: str, all_courses_data: dict):
        self.client.table(SupabaseTables.ALL_COURSES).update(all_courses_data).eq(
            "id", all_courses_id
        ).execute()

    def delete_all_courses(self, all_courses_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.ALL_COURSES)
            .delete()
            .eq("id", all_courses_id)
            .execute()
        )
        if not data.data:
            return None
        return AllCourses.model_validate(data.data[0])

    def get_all_all_courses(self) -> list[AllCourses]:
        data = self.client.table(SupabaseTables.ALL_COURSES).select("*").execute()
        if not data.data:
            return []
        return [AllCourses.model_validate(all_courses) for all_courses in data.data]
