from typing import Optional

from pydantic import NonNegativeFloat

from src.db.models.utils.models.BaseModel import BaseModel
from src.db.models.utils.types.UuidStr import UuidStr


class Course(BaseModel):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[NonNegativeFloat] = None
    passed: Optional[bool] = None
