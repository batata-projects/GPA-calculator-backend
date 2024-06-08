from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.courses.router import (
    create_course,
    delete_course,
    get_all_courses,
    get_course_by_id,
    get_courses_by_available_courses_id,
    get_courses_by_grade,
    get_courses_by_user_id,
    update_course,
)
from src.controller.courses.schemas import CourseResponse
from src.db.dao.course_dao import CourseDAO
from src.db.models.courses import Course


@pytest.mark.asyncio
class TestGetCourseById:
    async def test_get_course_by_id_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_course_by_id.return_value = course1

        assert course1.id is not None

        response = await get_course_by_id(course_id=course1.id, course_dao=course_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Course found"
        assert response.data == CourseResponse(courses=[course1])

    async def test_get_course_by_id_not_found(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_course_by_id.return_value = None

        response = await get_course_by_id(course_id=str(uuid4()), course_dao=course_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Course not found"
        assert response.data is None

    async def test_get_course_by_id_error(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_course_by_id.side_effect = Exception("Error")

        response = await get_course_by_id(course_id=str(uuid4()), course_dao=course_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetCoursesByUserId:
    async def test_get_courses_by_user_id_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_user_id.return_value = [course1]

        assert course1.user_id is not None

        response = await get_courses_by_user_id(
            user_id=course1.user_id, course_dao=course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Courses found"
        assert response.data == CourseResponse(courses=[course1])

    async def test_get_courses_by_user_id_not_found(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_user_id.return_value = []

        response = await get_courses_by_user_id(
            user_id=str(uuid4()), course_dao=course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Courses not found"
        assert response.data is None

    async def test_get_courses_by_user_id_error(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_user_id.side_effect = Exception("Error")

        response = await get_courses_by_user_id(
            user_id=str(uuid4()), course_dao=course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetCoursesByAvailableCoursesId:
    async def test_get_courses_by_available_courses_id_successful(
        self, course1: Course
    ) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_available_courses_id.return_value = [course1]

        assert course1.available_course_id is not None

        response = await get_courses_by_available_courses_id(
            available_course_id=course1.available_course_id, course_dao=course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Courses found"
        assert response.data == CourseResponse(courses=[course1])

    async def test_get_courses_by_available_courses_id_not_found(
        self, uuid4: Mock
    ) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_available_courses_id.return_value = []

        response = await get_courses_by_available_courses_id(
            available_course_id=str(uuid4()), course_dao=course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Courses not found"
        assert response.data is None

    async def test_get_courses_by_available_courses_id_error(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_available_courses_id.side_effect = Exception("Error")

        response = await get_courses_by_available_courses_id(
            available_course_id=str(uuid4()), course_dao=course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetCoursesByGrade:
    async def test_get_courses_by_grade_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_grade.return_value = [course1]

        assert course1.grade is not None

        response = await get_courses_by_grade(
            grade=course1.grade, course_dao=course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Courses found"
        assert response.data == CourseResponse(courses=[course1])

    async def test_get_courses_by_grade_not_found(self) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_grade.return_value = []

        response = await get_courses_by_grade(grade=12, course_dao=course_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Courses not found"
        assert response.data is None

    async def test_get_courses_by_grade_error(self) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_courses_by_grade.side_effect = Exception("Error")

        response = await get_courses_by_grade(grade=12, course_dao=course_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetAllCourses:
    async def test_get_all_courses_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_all_courses.return_value = [course1]

        response = await get_all_courses(course_dao=course_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Courses found"
        assert response.data == CourseResponse(courses=[course1])

    async def test_get_all_courses_not_found(self) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_all_courses.return_value = []

        response = await get_all_courses(course_dao=course_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Courses not found"
        assert response.data is None

    async def test_get_all_courses_error(self) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.get_all_courses.side_effect = Exception("Error")

        response = await get_all_courses(course_dao=course_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestCreateCourse:
    async def test_create_course_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.create_course.return_value = course1

        response = await create_course(
            course1.available_course_id,
            course1.user_id,
            course1.grade,
            course1.passed,
            course_dao,
        )

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "Course created"
        assert response.data == CourseResponse(courses=[course1])

    async def test_create_course_error(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.create_course.side_effect = Exception("Error")

        response = await create_course(
            course1.available_course_id,
            course1.user_id,
            course1.grade,
            course1.passed,
            course_dao,
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestUpdateCourse:
    async def test_update_course_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.update_course.return_value = course1

        assert course1.id is not None

        response = await update_course(
            course1.id,
            course1.available_course_id,
            course1.user_id,
            course1.grade,
            course1.passed,
            course_dao,
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Course updated"
        assert response.data == CourseResponse(courses=[course1])

    async def test_update_course_not_found(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.update_course.return_value = None

        response = await update_course(
            str(uuid4()), str(uuid4()), str(uuid4()), 12, True, course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Course not updated"
        assert response.data is None

    async def test_update_course_error(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.update_course.side_effect = Exception("Error")

        response = await update_course(
            str(uuid4()), str(uuid4()), str(uuid4()), 12, True, course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestDeleteCourse:
    async def test_delete_course_successful(self, course1: Course) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.delete_course.return_value = course1

        assert course1.id is not None

        response = await delete_course(course_id=course1.id, course_dao=course_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Course deleted"
        assert response.data == CourseResponse(courses=[course1])

    async def test_delete_course_not_found(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.delete_course.return_value = None

        response = await delete_course(course_id=str(uuid4()), course_dao=course_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Course not deleted"
        assert response.data is None

    async def test_delete_course_error(self, uuid4: Mock) -> None:
        course_dao = Mock(spec=CourseDAO)
        course_dao.delete_course.side_effect = Exception("Error")

        response = await delete_course(course_id=str(uuid4()), course_dao=course_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None
