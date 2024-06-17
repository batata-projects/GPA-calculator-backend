from supabase import Client

from src.db.dao import BaseDAO
from src.db.models import Course
from src.db.tables import SupabaseTables


class CourseDAO(BaseDAO[Course]):
    def __init__(self, client: Client) -> None:
        super().__init__(client, SupabaseTables.COURSES, Course)
