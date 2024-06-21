from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt

from src.common.utils.types import (
    CourseCodeStr,
    CourseGradeFloat,
    CourseNameStr,
    TermStr,
    UsernameStr,
    UuidStr,
)


class ValidItems(PydanticBaseModel):
    uuidStr: UuidStr = "00000000-0000-0000-0000-000000000000"
    termStr: TermStr = "Fall 2023 - 2024"
    usernameStr: UsernameStr = "username"
    courseNameStr: CourseNameStr = "ABCD"
    courseCodeStr: CourseCodeStr = "1234"
    emailStr: EmailStr = "email@mail.aub.edu"
    courseGradeFloat: CourseGradeFloat = 1.0
    nonNegativeInt: NonNegativeInt = 0
    nonNegativeFloat: NonNegativeFloat = 0.0
    boolean: bool = True


class ValidData:
    class AvailableCourse:
        id = ValidItems().uuidStr
        term_id = ValidItems().uuidStr
        name = ValidItems().courseNameStr
        code = ValidItems().courseCodeStr
        credits = ValidItems().nonNegativeInt
        graded = ValidItems().boolean

    class Course:
        id = ValidItems().uuidStr
        available_course_id = ValidItems().uuidStr
        user_id = ValidItems().uuidStr
        grade = ValidItems().courseGradeFloat

    class Term:
        id = ValidItems().uuidStr
        name = ValidItems().termStr

    class User:
        id = ValidItems().uuidStr
        email = ValidItems().emailStr
        username = ValidItems().usernameStr
        first_name = ""
        last_name = ""
        credits = ValidItems().nonNegativeInt
        counted_credits = ValidItems().nonNegativeInt
        grade = ValidItems().nonNegativeFloat

    class TestObject:
        id = ValidItems().uuidStr
        name = ""
