from enum import Enum


class SupabaseTables(str, Enum):
    AVAILABLE_COURSES = "available_courses"
    COURSES = "courses"
    TERMS = "terms"
    USERS = "users"

    def __str__(self) -> str:
        return self.value
