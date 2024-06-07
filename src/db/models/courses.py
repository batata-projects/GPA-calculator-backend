from typing import Optional

from pydantic import NonNegativeFloat

from src.common.utils.models.BaseModel import BaseModel
from src.common.utils.types.UuidStr import UuidStr


class Course(BaseModel):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[NonNegativeFloat] = None
    passed: Optional[bool] = None
