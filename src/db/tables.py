from enum import Enum


class SupabaseTables(str, Enum):
    AVAILABLE_COURSES = "all_courses"
    COURSES = "courses"
    TERMS = "terms"
    USERS = "users"

    def __str__(self):
        return self.value
