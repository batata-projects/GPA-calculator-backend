from src.common.utils.data.ValidData import ValidData, ValidItems


class TestValidItems:
    def test_ValidItems(self):
        assert ValidItems.UuidStr == "00000000-0000-0000-0000-000000000000"
        assert ValidItems.TermStr == "Fall 2023 - 2024"
        assert ValidItems.UsernameStr == "username"
        assert ValidItems.CourseNameStr == "ABCD"
        assert ValidItems.CourseCodeStr == "1234"
        assert ValidItems.EmailStr == "email@mail.aub.edu"
        assert ValidItems.NonNegativeInt == 0
        assert ValidItems.NonNegativeFloat == 0.0
        assert ValidItems.Bool == True


class TestValidData:
    def test_available_course_valid_data(self):
        assert ValidData.AvailableCourse.id == ValidItems.UuidStr
        assert ValidData.AvailableCourse.term_id == ValidItems.UuidStr
        assert ValidData.AvailableCourse.name == ValidItems.CourseNameStr
        assert ValidData.AvailableCourse.code == ValidItems.CourseCodeStr
        assert ValidData.AvailableCourse.credits == ValidItems.NonNegativeInt
        assert ValidData.AvailableCourse.graded == ValidItems.Bool

    def test_course_valid_data(self):
        assert ValidData.Course.id == ValidItems.UuidStr
        assert ValidData.Course.available_course_id == ValidItems.UuidStr
        assert ValidData.Course.user_id == ValidItems.UuidStr
        assert ValidData.Course.grade == ValidItems.NonNegativeFloat
        assert ValidData.Course.passed == ValidItems.Bool

    def test_term_valid_data(self):
        assert ValidData.Term.id == ValidItems.UuidStr
        assert ValidData.Term.name == ValidItems.TermStr

    def test_user_valid_data(self):
        assert ValidData.User.id == ValidItems.UuidStr
        assert ValidData.User.email == ValidItems.EmailStr
        assert ValidData.User.username == ValidItems.UsernameStr
        assert ValidData.User.first_name == ""
        assert ValidData.User.last_name == ""
        assert ValidData.User.credits == ValidItems.NonNegativeInt
        assert ValidData.User.counted_credits == ValidItems.NonNegativeInt
        assert ValidData.User.grade == ValidItems.NonNegativeFloat
