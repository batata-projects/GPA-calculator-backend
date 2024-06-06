from .fixtures.db.models.available_courses import (
    available_courses,
    available_courses_data,
    available_courses_same_course_name,
    available_courses_same_credits,
    available_courses_same_graded,
    available_courses_same_terms,
    invalid_available_course_data,
)
from .fixtures.db.models.courses import (
    course1,
    course2,
    courses,
    courses_same_available_course_id,
    courses_same_grade,
    courses_same_user_id,
)
from .fixtures.db.models.terms import term1, term2, terms, terms_same_name
from .fixtures.db.models.users import (
    user1,
    user2,
    users,
    users_same_counted_credits,
    users_same_credits,
    users_same_first_name,
    users_same_grade,
    users_same_last_name,
)
from .fixtures.db.models.utils import (
    invalid_course_code,
    invalid_course_name,
    invalid_domain,
    invalid_email,
    invalid_term,
    invalid_uuid,
    valid_course_code,
    valid_course_name,
    valid_email,
    valid_term,
    valid_uuid,
)
from .fixtures.uuid import uuid4
