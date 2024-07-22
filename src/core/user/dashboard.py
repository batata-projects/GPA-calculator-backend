from src.db.models import User, Course
from typing import Any


def get_dashboard_data(user: User, courses: list[Course]) -> dict[str, Any]:
    ...
