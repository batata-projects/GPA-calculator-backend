from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt

from src.common.utils.types import CourseGradeFloat, CourseStr, UuidStr


class ValidItems(PydanticBaseModel):
    uuidStr: UuidStr = "00000000-0000-0000-0000-000000000000"
    emailStr: EmailStr = "email@mail.aub.edu"
    courseGradeFloat: CourseGradeFloat = 1.0
    nonNegativeInt: NonNegativeInt = 0
    nonNegativeFloat: NonNegativeFloat = 0.0
    courseStr: CourseStr = "EECE230"
    firstName: str = "First"
    lastName: str = "Last"
    termInt: int = 202310
    boolean: bool = True


class ValidData:

    class User:
        id = ValidItems().uuidStr
        email = ValidItems().emailStr
        first_name = ValidItems().firstName
        last_name = ValidItems().lastName
        credits = ValidItems().nonNegativeInt
        counted_credits = ValidItems().nonNegativeInt
        grade = ValidItems().nonNegativeFloat

    class Course:
        id = ValidItems().uuidStr
        user_id = ValidItems().uuidStr
        subject = ValidItems().courseStr
        course_code = ValidItems().courseStr
        term = ValidItems().termInt
        credits = ValidItems().nonNegativeInt
        grade = ValidItems().courseGradeFloat
        graded = ValidItems().boolean

    class TestObject:
        id = ValidItems().uuidStr
        name = ""
