class ValidItems:
    UuidStr = "00000000-0000-0000-0000-000000000000"
    TermStr = "Fall 2023 - 2024"
    UsernameStr = "username"
    CourseNameStr = "ABCD"
    CourseCodeStr = "1234"
    EmailStr = "email@mail.aub.edu"
    NonNegativeInt = 0
    NonNegativeFloat = 0.0
    Bool = True


class ValidData:
    class AvailableCourse:
        id = ValidItems.UuidStr
        term_id = ValidItems.UuidStr
        name = ValidItems.CourseNameStr
        code = ValidItems.CourseCodeStr
        credits = ValidItems.NonNegativeInt
        graded = ValidItems.Bool

    class Course:
        id = ValidItems.UuidStr
        available_course_id = ValidItems.UuidStr
        user_id = ValidItems.UuidStr
        grade = ValidItems.NonNegativeFloat
        passed = ValidItems.Bool

    class Term:
        id = ValidItems.UuidStr
        name = ValidItems.TermStr

    class User:
        id = ValidItems.UuidStr
        email = ValidItems.EmailStr
        username = ValidItems.UsernameStr
        first_name = ""
        last_name = ""
        credits = ValidItems.NonNegativeInt
        counted_credits = ValidItems.NonNegativeInt
        grade = ValidItems.NonNegativeFloat
