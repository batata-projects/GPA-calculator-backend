from .fixtures.db.models.available_courses import (
    available_courses,
    available_courses_same_course_name,
    available_courses_same_credits,
    available_courses_same_graded,
    available_courses_same_terms,
)
from .fixtures.db.models.courses import (
    courses,
    courses_same_available_course_id,
    courses_same_grade,
    courses_same_passed,
    courses_same_user_id,
)
from .fixtures.db.models.terms import terms, terms_same_name
from .fixtures.db.models.users import (
    users,
    users_same_counted_credits,
    users_same_credits,
    users_same_email,
    users_same_first_name,
    users_same_grade,
    users_same_last_name,
    users_same_username,
)
from .fixtures.db.models.utils import (
    invalid_course_code,
    invalid_course_name,
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
