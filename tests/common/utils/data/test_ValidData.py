from src.common.utils.data.ValidData import ValidData, ValidItems
from src.db.models import Course, User


class TestValidItems:
    def test_ValidItems(self) -> None:
        validItems = ValidItems()

        assert validItems.uuidStr == "00000000-0000-0000-0000-000000000000"
        assert validItems.emailStr == "email@mail.com"
        assert validItems.courseGradeFloat == 1.0
        assert validItems.nonNegativeInt == 0
        assert validItems.nonNegativeFloat == 0.0
        assert validItems.courseStr == "EECE230"
        assert validItems.firstName == "First"
        assert validItems.lastName == "Last"
        assert validItems.termInt == 202310
        assert validItems.boolean == True


class TestValidData:
    def test_user_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.User.id == validItems.uuidStr
        assert ValidData.User.email == validItems.emailStr
        assert ValidData.User.first_name == validItems.firstName
        assert ValidData.User.last_name == validItems.lastName
        assert ValidData.User.credits == validItems.nonNegativeInt
        assert ValidData.User.counted_credits == validItems.nonNegativeInt
        assert ValidData.User.grade == validItems.nonNegativeFloat

        assert User(
            id=ValidData.User.id,
            email=ValidData.User.email,
            first_name=ValidData.User.first_name,
            last_name=ValidData.User.last_name,
            credits=ValidData.User.credits,
            counted_credits=ValidData.User.counted_credits,
            grade=ValidData.User.grade,
        )

    def test_course_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.Course.id == validItems.uuidStr
        assert ValidData.Course.user_id == validItems.uuidStr
        assert ValidData.Course.subject == validItems.courseStr
        assert ValidData.Course.course_code == validItems.courseStr
        assert ValidData.Course.term == validItems.termInt
        assert ValidData.Course.credits == validItems.nonNegativeInt
        assert ValidData.Course.grade == validItems.courseGradeFloat
        assert ValidData.Course.graded == validItems.boolean

        assert Course(
            id=ValidData.Course.id,
            user_id=ValidData.Course.user_id,
            subject=ValidData.Course.subject,
            course_code=ValidData.Course.course_code,
            term=ValidData.Course.term,
            credits=ValidData.Course.credits,
            grade=ValidData.Course.grade,
            graded=ValidData.Course.graded,
        )

    def test_test_object_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.TestObject.id == validItems.uuidStr
        assert ValidData.TestObject.name == ""
