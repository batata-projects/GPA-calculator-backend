from typing import Optional

from pydantic import NonNegativeFloat

from src.db.models.utils import BaseModelCustomized, UuidStr


class Course(BaseModelCustomized):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[NonNegativeFloat] = None
    passed: Optional[bool] = None
