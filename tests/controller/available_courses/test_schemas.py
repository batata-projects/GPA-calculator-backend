# import pytest

# from src.controller.available_courses.schemas import AvailableCourseResponse
# from src.db.models.available_courses import AvailableCourse


# class TestAvailableCourseResponse:
#     def test_available_course_response_successful(
#         self, available_course1: AvailableCourse
#     ) -> None:
#         available_course_response = AvailableCourseResponse(
#             available_courses=[available_course1]
#         )

#         assert available_course_response.available_courses == [available_course1]

#     def test_available_course_response_empty(self) -> None:
#         available_course_response = AvailableCourseResponse()

#         assert available_course_response.available_courses == []

#     def test_available_course_multiple_available_courses(
#         self, available_course1: AvailableCourse, available_course2: AvailableCourse
#     ) -> None:
#         available_course_response = AvailableCourseResponse(
#             available_courses=[available_course1, available_course2]
#         )

#         assert available_course_response.available_courses == [
#             available_course1,
#             available_course2,
#         ]

#     def test_available_course_response_invalid_available_course(self) -> None:
#         with pytest.raises(ValueError):
#             AvailableCourseResponse(available_courses=[{"name": "AvailableCourse 1"}])  # type: ignore
