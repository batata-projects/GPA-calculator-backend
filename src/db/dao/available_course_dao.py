from supabase import Client

from src.db.dao import BaseDAO
from src.db.models import AvailableCourse
from src.db.tables import SupabaseTables


class AvailableCourseDAO(BaseDAO[AvailableCourse]):
    def __init__(self, client: Client) -> None:
        super().__init__(client, SupabaseTables.AVAILABLE_COURSES, AvailableCourse)
