from src.common.utils.data.ValidData import ValidData, ValidItems


class TestValidItems:
    def test_ValidItems(self) -> None:
        validItems = ValidItems()

        assert validItems.uuidStr == "00000000-0000-0000-0000-000000000000"
        assert validItems.termStr == "Fall 2023 - 2024"
        assert validItems.usernameStr == "username"
        assert validItems.courseNameStr == "ABCD"
        assert validItems.courseCodeStr == "1234"
        assert validItems.emailStr == "email@mail.aub.edu"
        assert validItems.courseGradeFloat == 1.0
        assert validItems.nonNegativeInt == 0
        assert validItems.nonNegativeFloat == 0.0
        assert validItems.boolean == True


class TestValidData:
    def test_available_course_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.AvailableCourse.id == validItems.uuidStr
        assert ValidData.AvailableCourse.term_id == validItems.uuidStr
        assert ValidData.AvailableCourse.name == validItems.courseNameStr
        assert ValidData.AvailableCourse.code == validItems.courseCodeStr
        assert ValidData.AvailableCourse.credits == validItems.nonNegativeInt
        assert ValidData.AvailableCourse.graded == validItems.boolean

    def test_course_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.Course.id == validItems.uuidStr
        assert ValidData.Course.available_course_id == validItems.uuidStr
        assert ValidData.Course.user_id == validItems.uuidStr
        assert ValidData.Course.grade == validItems.courseGradeFloat
        assert ValidData.Course.passed == validItems.boolean

    def test_term_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.Term.id == validItems.uuidStr
        assert ValidData.Term.name == validItems.termStr

    def test_user_valid_data(self) -> None:
        validItems = ValidItems()

        assert ValidData.User.id == validItems.uuidStr
        assert ValidData.User.email == validItems.emailStr
        assert ValidData.User.username == validItems.usernameStr
        assert ValidData.User.first_name == ""
        assert ValidData.User.last_name == ""
        assert ValidData.User.credits == validItems.nonNegativeInt
        assert ValidData.User.counted_credits == validItems.nonNegativeInt
        assert ValidData.User.grade == validItems.nonNegativeFloat
