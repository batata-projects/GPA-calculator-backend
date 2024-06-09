from .fixtures.uuid import uuid4
from .fixtures.auth.schemas import register_request, login_request
from .fixtures.common.utils.types.CourseCodeStr import valid_course_code, invalid_course_code
from .fixtures.common.utils.types.CourseNameStr import valid_course_name, invalid_course_name
from .fixtures.common.utils.types.TermStr import valid_term, invalid_term
from .fixtures.common.utils.types.UsernameStr import valid_username, invalid_username1, invalid_username2
from .fixtures.common.utils.types.UuidStr import valid_uuid, invalid_uuid
from .fixtures.db.base import mock_config, mock_access_token, mock_refresh_token
from .fixtures.db.dependencies import mock_config, mock_authenticated_client, mock_unauthenticated_client
from .fixtures.db.models.available_courses import available_courses, available_course1, available_course2, available_courses_same_course_name, available_courses_same_credits, available_courses_same_terms, available_courses_same_graded, available_courses_data, invalid_available_course_data
from .fixtures.db.models.courses import courses, course1, course2, courses_same_available_course_id, courses_same_user_id, courses_same_grade
from .fixtures.db.models.terms import terms, term1, term2, terms_same_name
from .fixtures.db.models.users import users, user1, user2, users_same_first_name, users_same_last_name, users_same_credits, users_same_counted_credits, users_same_grade
