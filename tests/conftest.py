from .fixtures.auth.schemas import login_request, register_request
from .fixtures.common.utils.types.CourseCodeStr import (
    invalid_course_code,
    valid_course_code,
)
from .fixtures.common.utils.types.CourseNameStr import (
    invalid_course_name,
    valid_course_name,
)
from .fixtures.common.utils.types.TermStr import invalid_term, valid_term
from .fixtures.common.utils.types.UsernameStr import (
    invalid_username1,
    invalid_username2,
    valid_username,
)
from .fixtures.common.utils.types.UuidStr import invalid_uuid, valid_uuid
from .fixtures.db.models.available_courses import (
    available_course1,
    available_course2,
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
from .fixtures.uuid import uuid4
